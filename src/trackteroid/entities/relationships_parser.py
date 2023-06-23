#  BSD 3-Clause License
#
#  Copyright (c) 2023, Trixter GmbH
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import itertools


# TODO: This need class/function docs
class TreeData:
    def __init__(self, type=None, parent_attr=None, parent=None):
        self.type = type
        self.parent_attr = parent_attr
        self.parent = parent


class TreeItem:
    def __init__(self, data=TreeData()):
        self.children = []
        self.data = data

    def get_parent(self):
        return self.data.parent


class RelationshipsParser(object):

    def __init__(self, ftrack_session=None):
        self._session = ftrack_session
        self._exclude_types = set()
        self._tmp_exclude_types = set()
        self._ref_key = "refs"
        self._entities = {}
        self._tmp_relations = {}
        self._include_types = set()
        self._attributes_blacklist = set()
        self._root_item = TreeItem()
        self._project_relations = {}
        self._relationships = {}
        self._all_array_types = {}

    def parse_session_schemas(self):
        for ftrack_entity in self._session.schemas:
            entity_id = ftrack_entity.get("id")
            self._entities[entity_id] = {}
            tmp_refs = {}
            tmp_array_refs = {}
            for prop, prop_data in ftrack_entity["properties"].items():
                items = prop_data.get("items")
                ref = prop_data.get("$ref", "")
                if ref:
                    tmp_refs[prop] = ref
                if items:
                    ref = prop_data.get("items").get("$ref", "")
                    if ref:
                        tmp_array_refs[prop] = ref
            self._entities[entity_id]["refs"] = tmp_refs
            self._entities[entity_id]["array_refs"] = tmp_array_refs

    def create_entity_network(self, ftrack_entity):
        self._tmp_exclude_types = set(self._exclude_types)
        # entity type must be excluded, as finding it in one of its children would lead to an endless recursion
        self._tmp_exclude_types.add(ftrack_entity)
        return self.recurse_entity_connections(ftrack_entity, ancestors=set())

    def recurse_entity_connections(self, ftrack_entity, ancestors=None):
        # ancestors are the entities, in sequence, linking to the current entity
        # the top entity of course has none
        if ancestors is None:
            ancestors = set()
        # refs - reference type attributes on the current entity
        # type - current entity's type
        network = {"refs": {}, "type": ftrack_entity}
        # return otherwise recursion will be endless
        if ftrack_entity in ancestors:
            return network

        # get all array or non-array reference attributes of the current entity
        refs = self._entities.get(ftrack_entity).get(self._ref_key)
        if refs:
            # first iteration - validate props
            valid_props = {}
            for prop_name, prop_type in refs.items():
                if prop_name not in self._attributes_blacklist and prop_type not in self._tmp_exclude_types and prop_type != ftrack_entity:
                    valid_props[prop_name] = prop_type
            # add valid prop types to exclude list for deeper recursions
            self._tmp_exclude_types.update(valid_props.values())

            # second iteration, recurse all valid props
            for prop_name, prop_type in valid_props.items():
                if prop_type in self._entities:
                    ancestors.add(ftrack_entity)
                    network["refs"][prop_name] = self.recurse_entity_connections(prop_type, ancestors)
        return network

    def extract_entity_relations(self, network):
        self._tmp_relations = {}
        self.recurse_entity_relations(network)
        return self._tmp_relations

    def recurse_entity_relations(self, network, path=None):
        if path is None:
            path = []
        if "refs" in network:
            for attr_name, attr_data in network.get("refs").items():
                prop_type = attr_data.get("type")
                if prop_type not in self._tmp_relations:
                    tmp_path = list(path)
                    tmp_path.append(attr_name)
                    self._tmp_relations[prop_type] = tmp_path
                    self.recurse_entity_relations(attr_data, tmp_path)

    def extract_all_entity_relations(self):
        for entity_name in self._entities:
            self._relationships[entity_name] = {}

            # create network of non-array references
            self.use_array_refs = False
            asset_network = self.create_entity_network(entity_name)

            # extract non-collection relations
            self._relationships[entity_name]["non_collection"] = self.extract_entity_relations(asset_network)

            # create network of array references
            self.use_array_refs = True
            asset_network = self.create_entity_network(entity_name)

            # extract collection relations
            self._relationships[entity_name]["collection"] = self.extract_entity_relations(asset_network)

    def parse_project_structure(self, project):
        root_data = TreeData(project.entity_type, None)
        self._root_item = TreeItem(root_data)
        self._project_relations = {}
        self.recurse_project_structure(self._root_item, project)

    def recurse_project_structure(self, structure_item=TreeItem(), ftrack_entity=None):
        entity_type = structure_item.data.type
        if entity_type in self._entities:
            refs = self._entities.get(entity_type).get("array_refs")
            for ref in refs:
                if ref in self._attributes_blacklist:
                    continue
                collection = ftrack_entity.get(ref)
                if collection and collection.__class__.__name__ == "Collection":
                    for child in collection:
                        if child.get("parent") == ftrack_entity:
                            child_data = TreeData(child.entity_type, "parent", structure_item)
                            child_item = TreeItem(child_data)
                            structure_item.children.append(child_item)
                            self.recurse_project_structure(child_item, child)
                        elif child.entity_type in self._include_types:
                            tmp_collection_parent_attr = self._relationships.get(child.entity_type).get("non_collection").get(entity_type)
                            if tmp_collection_parent_attr:
                                collection_parent = tmp_collection_parent_attr[-1]
                                if child.get(collection_parent) == ftrack_entity:
                                    child_data = TreeData(child.entity_type, collection_parent, structure_item)
                                    child_item = TreeItem(child_data)
                                    structure_item.children.append(child_item)
                                    self.recurse_project_structure(child_item, child)

    def print_project_structure(self, tree_item=TreeItem(), offset=""):
        print(offset, "Item:", tree_item.data.type, tree_item.data.parent_attr)
        offset = offset + "  "
        for child in tree_item.children:
            self.print_project_structure(child, offset)

    def extract_project_relations(self):
        self._project_relations = {}
        self.walk_tree_down(self._root_item)
        for entity_name, entity_data in self._project_relations.items():
            self._relationships[entity_name]["parent_attr"] = entity_data.get("parent_attr")
            entity_relations = entity_data.get("parent_paths")
            self._relationships[entity_name]["project"] = self.optimize_project_relations(entity_name, entity_relations)

    def walk_tree_down(self, tree_item=TreeItem()):
        for child in tree_item.children:
            child_data = child.data
            if child_data.type not in self._project_relations:
                self._project_relations[child_data.type] = {}
                self._project_relations[child_data.type]["parent_attr"] = child_data.parent_attr
                self._project_relations[child_data.type]["parent_paths"] = []
            tmp_paths = []
            self.walk_tree_up(tmp_paths, child)
            for path in tmp_paths:
                if path not in self._project_relations[child_data.type]["parent_paths"]:
                    self._project_relations[child_data.type]["parent_paths"].append(path)
            self.walk_tree_down(child)

    def walk_tree_up(self, tmp_paths, tree_item=TreeItem(), path=None):
        if path is None:
            path = []
        # top reached
        if tree_item.data.type not in self._project_relations:
            return
        parent = tree_item.get_parent()
        if parent:
            path.append({"type": parent.data.type, "attr": tree_item.data.parent_attr})
            tmp_paths.append(list(path))
            self.walk_tree_up(tmp_paths, parent, path)

    def optimize_project_relations(self, entity, relations):
        if not relations:
            return
        optimized_relations = []
        for relation_data in relations:
            relation = relation_data[-1].get("type")
            if len(relation_data) > 1: # can"t get shorter than 1
                original_path_length = len(relation_data)
                shortest_relation = []
                shorter_path_found = False
                for rel in relation_data[:original_path_length-1]: # now search up the relation to find even shorter ones
                    non_collection_relation = self._relationships.get(rel.get("type")).get("non_collection")
                    shortest_relation.append(rel)
                    if relation in non_collection_relation:
                        alternative_relation = non_collection_relation.get(relation)
                        if len(alternative_relation) <= len(shortest_relation) and len(alternative_relation) == 1:
                            for alt_relation in alternative_relation:
                                shortest_relation.append({"type": relation, "attr": alt_relation})
                                shorter_path_found = True
                            break
                if shorter_path_found:
                    optimized_relations.append(shortest_relation)
                    continue
            optimized_relations.append(relation_data)
        return optimized_relations

    @property
    def exclude_types(self):
        return self._exclude_types

    @exclude_types.setter
    def exclude_types(self, exclude_types):
        self._exclude_types = exclude_types

    @property
    def use_array_refs(self):
        return self._ref_key == "array_refs"

    @use_array_refs.setter
    def use_array_refs(self, use_array_refs):
        if use_array_refs:
            self._ref_key = "array_refs"
        else:
            self._ref_key = "refs"

    @property
    def include_types(self):
        return self._include_types

    @include_types.setter
    def include_types(self, include_types):
        self._include_types = include_types

    @property
    def attributes_blacklist(self):
        return self._attributes_blacklist

    @attributes_blacklist.setter
    def attributes_blacklist(self, attributes_blacklist):
        self._attributes_blacklist = attributes_blacklist

    @property
    def entities(self):
        return self._entities

    @property
    def project_relations(self):
        return self._project_relations

    @property
    def relationships(self):
        return self._relationships

    @property
    def array_attributes(self):
        array_refs = list(set(itertools.chain.from_iterable(_["array_refs"].keys() for _ in self.entities.values())))
        array_refs.sort()
        return array_refs