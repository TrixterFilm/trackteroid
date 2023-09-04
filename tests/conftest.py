from collections import OrderedDict
import logging
import random
import uuid

import ftrack_api
from ftrack_api.collection import Collection
import pytest

from trackteroid import SESSION, Query
from trackteroid.entities import *
from trackteroid.entities.base import Entity, EntityCollection


class TestScenario:
    __test__ = False

    def __init__(self, project_ids=[]):
        self.entity_ids = {
            "Project": project_ids,
            "Folder": [],
            "Sequence": [],
            "Shot": [],
            "AssetBuild": [],
            "Task": [],
            "Asset": [],
            "AssetVersion": [],
            "Component": []
        }

    def query_project(self, session, projections):
        return session.query(
            f"select {', '.join(projections)} from Project "
            f"where id is {self.entity_ids['Project'][0]}"
        ).one()

    def create_entity(self, ftrack_session, entity_type, params):
        entity = ftrack_session.create(entity_type, params)
        self.entity_ids[entity_type].append(entity["id"])
        return entity["id"]

    def create_assets_tasks_versions(self, ftrack_session):

        for parent_id in self.entity_ids["AssetBuild"] + self.entity_ids["Shot"]:
            parent = ftrack_session.get("TypedContext", parent_id)
            for _ in range(3):
                params = {"name": "asset_{0}".format(uuid.uuid4()), "parent": parent}
                asset_id = self.create_entity(ftrack_session, "Asset", params)
                params = {"name": "task_{0}".format(uuid.uuid4()), "parent": parent}
                task_id = self.create_entity(ftrack_session, "Task", params=params)
                for version in range(1, 4):
                    asset = ftrack_session.get("Asset", asset_id)
                    task = ftrack_session.get("Task", task_id)
                    params = {"version": version, "asset": asset, "task": task}
                    self.create_entity(ftrack_session, "AssetVersion", params=params)

    def grab(self, session, entity_type, required_fields=[], limit=0):
        if entity_type not in self.entity_ids:
            raise KeyError(entity_type)
        if not self.entity_ids[entity_type]:
            raise ValueError(f"No entities of type {entity_type} exists in the scenario")

        query = ""
        if required_fields:
            query += f"select {', '.join(required_fields)} from "
        query += f"{entity_type} where "
        query += f"id in ({', '.join(self.entity_ids[entity_type])})"
        if limit > 0:
            query += f" limit {limit}"
        result = session.query(query).all()
        random.shuffle(result)
        return result

    def construct_collection_from_ftrack_entities(self, ftrack_entities):
        entities = []
        for ftrack_entity in ftrack_entities:
            entities.append(
                (ftrack_entity["id"], Entity(_cls=globals()[ftrack_entity.entity_type], ftrack_entity=ftrack_entity)))
        collection = EntityCollection(
            _cls=entities[0][1].__class__,
            entities=OrderedDict(entities),
            session=SESSION
        )
        collection.query = Query(entities[0][1].__class__).by_id(*[_["id"] for _ in ftrack_entities])
        return collection

    def construct_simple_collection(self, session, entity_type, limit=0, required_fields=[]):
        entities = self.grab(session, entity_type, limit=limit, required_fields=required_fields)
        return self.construct_collection_from_ftrack_entities(entities)

    def _assert_attributes(self, ftrack_entity, entity_collection):
        not_implemented_msg = "Skipped attribute testing for '{key}', because required Entity is not implemented"

        for key, value in ftrack_entity.items():
            if isinstance(value, Collection):
                try:
                    _collection_ids = []
                    if len(value) > 0:
                        for _ in value:
                            _collection_ids.append(_["id"])
                        logging.debug("Test for secondary")
                        assert _collection_ids ==  getattr(entity_collection, key).id
                except NotImplementedError:
                    logging.warning(not_implemented_msg.format(key=key))
            else:
                # testing primary attributes
                logging.debug("Testing against attribute '{}'".format(key))
                try:
                    _attribute_value = getattr(entity_collection, key)
                    if isinstance(_attribute_value, EntityCollection):
                        _ftrack_entities = [_.ftrack_entity for _ in _attribute_value._entities.values()]
                        assert [value] == _ftrack_entities
                    else:
                        assert [value] == getattr(entity_collection, key)
                except NotImplementedError:
                    logging.warning(not_implemented_msg.format(key=key))


@pytest.fixture(autouse=True)
def reconnect_session():
    return SESSION.reconnect()


@pytest.fixture()
def ftrack_session():
    with ftrack_api.Session() as session:
        yield session


@pytest.fixture
def ftrack_project_id():
    session = ftrack_api.Session()
    name = "unittests_{0}".format(uuid.uuid1().hex)

    # Naively pick the first project schema. For this example to work the
    # schema must contain `Shot` and `Sequence` object types.
    required_types = ["Sequence", "Shot"]
    project_schema = None
    for schema in session.query("ProjectSchema").all():
        types = [x["name"] for x in schema["object_types"]]
        if all([x in types for x in required_types]):
            project_schema = schema
            break

    if not project_schema:
        raise ValueError(
            f"A project schema with the following types could not be found on {session.server_url}:"
            f" {', '.join(required_types)}"
        )

    # Create the project with the chosen schema.
    project = session.create(
        "Project",
        {"name": name, "full_name": name + "_full", "project_schema": project_schema},
    )
    session.commit()

    yield project["id"]

    session.delete(project)
    session.commit()


@pytest.fixture
def scenario_project(ftrack_project_id) -> TestScenario:
    return TestScenario(project_ids=[ftrack_project_id])


@pytest.fixture
def scenario_sequence_folder(ftrack_session, scenario_project) -> TestScenario:
    project = scenario_project.query_project(ftrack_session, ["project_schema"])
    for _ in range(2):
        params = {"name": "seq_{0}".format(uuid.uuid4()), "parent": project}
        scenario_project.create_entity(ftrack_session=ftrack_session, entity_type="Sequence", params=params)
    params = {"name": "asset_builds".format(uuid.uuid4()), "parent": project}
    scenario_project.create_entity(ftrack_session=ftrack_session, entity_type="Folder", params=params)
    ftrack_session.commit()

    return scenario_project


@pytest.fixture
def scenario_assetbuild_shot(ftrack_session, scenario_sequence_folder) -> TestScenario:
    assetbuild_folder_id = scenario_sequence_folder.entity_ids["Folder"][0]
    assetbuild_folder = ftrack_session.get("Folder", assetbuild_folder_id)
    for _ in range(3):
        params = {"name": "asset_build_{0}".format(uuid.uuid4()), "parent": assetbuild_folder}
        scenario_sequence_folder.create_entity(ftrack_session, "AssetBuild", params=params)

    project = scenario_sequence_folder.query_project(ftrack_session, ["project_schema"])
    project_schema = project["project_schema"]
    default_shot_status = project_schema.get_statuses("Shot")[0]
    for sequence_id in scenario_sequence_folder.entity_ids["Sequence"]:
        sequence = ftrack_session.get("Sequence", sequence_id)
        for shot in range(3):
            params = {"name": "shot_{}".format(uuid.uuid4()), "parent": sequence, "status": default_shot_status}
            scenario_sequence_folder.create_entity(ftrack_session, "Shot", params=params)
    ftrack_session.commit()

    return scenario_sequence_folder


@pytest.fixture
def scenario_asset_task_version(ftrack_session, scenario_assetbuild_shot) -> TestScenario:
    scenario_assetbuild_shot.create_assets_tasks_versions(ftrack_session)
    ftrack_session.commit()

    return scenario_assetbuild_shot


@pytest.fixture
def scenario_components(ftrack_session, scenario_asset_task_version) -> TestScenario:
    for assetversion_id in scenario_asset_task_version.entity_ids["AssetVersion"]:
        assetversion = ftrack_session.get("AssetVersion", assetversion_id)
        params = {"name": "component_{}".format(uuid.uuid4()), "parent": assetversion}
        scenario_asset_task_version.create_entity(ftrack_session, "Component", params=params)
    ftrack_session.commit()

    return scenario_asset_task_version
