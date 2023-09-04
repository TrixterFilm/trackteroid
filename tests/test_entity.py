import logging
import pytest

from arrow.arrow import Arrow
from collections import OrderedDict, Counter
from datetime import datetime
from itertools import chain

from trackteroid import (
    SESSION,
    Query
)
from trackteroid.entities.base import (
    Entity,
    EmptyCollection,
    EntityCollection
)
from trackteroid.entities.schematypes import CUSTOM_ATTRIBUTE_TYPE_COMPATIBILITY
from trackteroid.entities import *


# TODO: tests missing for `count()`, ` map()`, ` group_by_an_map`


def test_fetch_attributes(scenario_asset_task_version, ftrack_session):
    assetversion = scenario_asset_task_version.grab(ftrack_session, "AssetVersion")[0]
    query = SESSION.query("AssetVersion where id is {}".format(assetversion["id"]))
    assert not query.one()["asset"]
    collection = scenario_asset_task_version.construct_collection_from_ftrack_entities([assetversion])
    collection.fetch_attributes("asset")
    assert query.one()["asset"]

def test_get_attributes(scenario_asset_task_version, ftrack_session):
    assetversion = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", ["asset.versions"])[0]

    # first pass without auto population
    assetversion_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities([assetversion])
    scenario_asset_task_version._assert_attributes(assetversion, assetversion_collection)

    # second with auto population
    setattr(SESSION, "auto_populate", True)
    scenario_asset_task_version._assert_attributes(assetversion, assetversion_collection)
    setattr(SESSION, "auto_populate", False)

    # test nested attribute access
    versions = []
    for _assetversion in assetversion["asset"]["versions"]:
        versions.append(_assetversion["version"])
    assert versions == assetversion_collection.asset.versions.version

def test_get_custom_attributes(scenario_asset_task_version, ftrack_session):
    task = scenario_asset_task_version.grab(ftrack_session, "Task", ["custom_attributes"])[0]
    task_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities([task])

    for key, value in task["custom_attributes"].items():
        assert [value] == getattr(task_collection, "custom_{}".format(key))

    setattr(SESSION, "auto_populate", True)
    for key, value in task["custom_attributes"].items():
        assert [value] == getattr(task_collection, "custom_{}".format(key))
    setattr(SESSION, "auto_populate", False)

def test_get_item(scenario_asset_task_version, ftrack_session):
    assetversions = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    assetversion_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(assetversions)
    for i, assetversion in enumerate(assetversions):
        collections = [
            assetversion_collection[assetversion["id"]],
            assetversion_collection[i],
            assetversion_collection[i:len(assetversions)]
        ]

        # ensure result is an EntityCollection
        assert any([isinstance(_, EntityCollection) for _ in collections])

        # ensure it holds the proper entities
        assert [assetversion] == [_.ftrack_entity for _ in collections[0]._entities.values()]
        assert [assetversion] == [_.ftrack_entity for _ in collections[1]._entities.values()]
        assert assetversions[i:len(assetversions)] == [_.ftrack_entity for _ in collections[2]._entities.values()]

def test_contains(scenario_asset_task_version, ftrack_session):
    assetversion_collection = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=10)

    for _id, entity in assetversion_collection._entities.items():
        assert _id in assetversion_collection
        assert entity in assetversion_collection

def test_equality(scenario_asset_task_version, ftrack_session):
    assetversion_collection_1 = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=20)
    assetversion_collection_2 = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=20)

    assetversion_collection_3 = EntityCollection(
        _cls=AssetVersion,
        entities=assetversion_collection_1._entities
    )
    assetversion_collection_3.query = Query(AssetVersion).by_id(
        *[_.ftrack_entity["id"] for _ in assetversion_collection_3._entities.values()]
    )

    assert assetversion_collection_1 != assetversion_collection_2
    assert assetversion_collection_1 == assetversion_collection_3

def test_length(scenario_asset_task_version, ftrack_session):
    assert 3 == len(scenario_asset_task_version.construct_simple_collection(ftrack_session, "AssetVersion", limit=3))
    assert 10 == len(scenario_asset_task_version.construct_simple_collection(ftrack_session, "Task", limit=10))
    assert 1 == len(scenario_asset_task_version.construct_simple_collection(ftrack_session, "Project", limit=1))

def test_from_entities(scenario_asset_task_version, ftrack_session):
    entities = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=10)._entities.values()
    ftrack_entities = [_.ftrack_entity for _ in entities]

    collection = EntityCollection(
        _cls=AssetVersion,
        entities=OrderedDict(
            [(ftrack_entities[0]["id"], entities)]
        )
    )
    collection.query = Query(AssetVersion).by_id(*[_["id"] for _ in ftrack_entities])
    new_collection = collection.from_entities(entities)

    assert ftrack_entities == [_.ftrack_entity for _ in new_collection._entities.values()]

def test_is_attribute_compatible_with_value(scenario_asset_task_version, ftrack_session):
    assetversion_collection = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=1, required_fields=["version", "task"])

    # all cases where receiver collection has only a single entity
    assert assetversion_collection._is_attribute_compatible_with_value("version", 5)[0]
    assert assetversion_collection._is_attribute_compatible_with_value("version", [5])[0]
    assert assetversion_collection._is_attribute_compatible_with_value(
            "task", scenario_asset_task_version.construct_simple_collection(ftrack_session, "Task", limit=1))[0]
    assert not assetversion_collection._is_attribute_compatible_with_value("version", "foobar")[0]
    assert not assetversion_collection._is_attribute_compatible_with_value("version", [5, 10])[0]
    assert not assetversion_collection._is_attribute_compatible_with_value("version", ["5"])[0]

    # receiver collection has multiple entries
    assert not scenario_asset_task_version.construct_simple_collection(
            ftrack_session, "AssetVersion", limit=2)._is_attribute_compatible_with_value("version", 5)[0]
    assert not scenario_asset_task_version.construct_simple_collection(
            ftrack_session, "AssetVersion", limit=2, required_fields=["version"])._is_attribute_compatible_with_value(
            "version", [5])[0]
    assert not scenario_asset_task_version.construct_simple_collection(
            ftrack_session, "AssetVersion", limit=2, required_fields=["version"])._is_attribute_compatible_with_value(
            "version", [5, 10, 15])[0]
    assert not assetversion_collection._is_attribute_compatible_with_value(
            "task", scenario_asset_task_version.construct_simple_collection(ftrack_session, "Task", limit=2))[0]
    assert not assetversion_collection._is_attribute_compatible_with_value(
            "task", scenario_asset_task_version.construct_simple_collection(
            ftrack_session, "AssetVersion", limit=1))[0]

    # rebuild our test collection
    new_assetversion_collection = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=3, required_fields=["version", "task"])

    assert new_assetversion_collection._is_attribute_compatible_with_value("version", [5, 6, 7])[0]
    assert not new_assetversion_collection._is_attribute_compatible_with_value("version", [5])[0]
    assert not new_assetversion_collection._is_attribute_compatible_with_value("version", [5, 6])[0]
    assert not new_assetversion_collection._is_attribute_compatible_with_value("version", "foobar")[0]
    assert new_assetversion_collection._is_attribute_compatible_with_value("task",
            scenario_asset_task_version.construct_simple_collection(ftrack_session, "Task", limit=3))[0]
    assert not new_assetversion_collection._is_attribute_compatible_with_value("task",
            scenario_asset_task_version.construct_simple_collection(ftrack_session, "Task", limit=1))[0]
    assert not new_assetversion_collection._is_attribute_compatible_with_value("task",
            scenario_asset_task_version.construct_simple_collection(ftrack_session, "AssetVersion", limit=1))[0]
    assert not new_assetversion_collection._is_attribute_compatible_with_value("task", EmptyCollection())[0]

def test_is_custom_attribute_compatible_with_value(scenario_components, ftrack_session):
    # test custom attributes
    # test each type for each custom attribute for each entity type
    for entity_type in scenario_components.entity_ids.keys():
        entity_cls = globals()[entity_type]
        if issubclass(entity_cls, Entity):
            try:
                entity_collection = scenario_components.construct_simple_collection(
                    ftrack_session, entity_type, limit=1, required_fields=["custom_attributes"])
            except:
                logging.info("No custom attributes found for entity type '{}'. Skipping.".format(entity_type))
                continue
            entity = list(entity_collection._entities.values())[0].ftrack_entity
            if entity["custom_attributes"]:
                for attribute in entity["custom_attributes"]:
                    for _type in getattr(CUSTOM_ATTRIBUTE_TYPE_COMPATIBILITY, attribute).types:
                        attribute = "custom_{}".format(attribute)
                        assert not entity_collection._is_attribute_compatible_with_value(attribute, None)[0]
                        assert not entity_collection._is_attribute_compatible_with_value(attribute, type)[0]
                        assert not entity_collection._is_attribute_compatible_with_value(attribute, [None])[0]
                        if _type is str:
                            assert entity_collection._is_attribute_compatible_with_value(attribute, "foobar")[0]
                            assert entity_collection._is_attribute_compatible_with_value(
                                    attribute, u"anderes wort ohne umlaut ... stupid pycharm")[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, ["bla"])[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, [5])[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, ["bla", "blubb"])[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, 5)[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, {"furz": "testen"})[0]
                        elif _type in (int, float):
                            assert entity_collection._is_attribute_compatible_with_value(attribute, 42)[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, 0)[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, 11.12)[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, [42])[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, [42.24])[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, "hallo")[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, True)[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, ["bla", "blubb"])[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, [5, 2])[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, {"furz": "testen"})[0]
                        elif _type in (bool,):
                            assert entity_collection._is_attribute_compatible_with_value(attribute, True)[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, False)[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, [True])[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, [False])[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, 0)[0]
                            assert not entity_collection._is_attribute_compatible_with_value(attribute, 1)[0]
                        elif _type in (Arrow, datetime):
                            assert entity_collection._is_attribute_compatible_with_value(attribute, datetime.now())[0]
                            assert entity_collection._is_attribute_compatible_with_value(attribute, Arrow.now())[0]

def test_setattr(scenario_asset_task_version, ftrack_session):
    # test POD
    def set_and_assert_equal(collection, attributes, value):
        attribute_tokens = attributes.split(".")
        current = collection
        idx = 0
        while idx < len(attribute_tokens) - 1:
            # we want to break just before the last token to call setattr
            # instead of getattr
            current = getattr(current, attribute_tokens[idx])
            idx += 1

        setattr(current, attribute_tokens[-1], value)

        after_value = getattr(current, attribute_tokens[-1])

        if isinstance(value, EntityCollection):
            value_list = [entity.ftrack_entity for entity in after_value._entities.values()]
            expected_list = [entity.ftrack_entity for entity in value._entities.values()]
            assert value_list == expected_list
        elif isinstance(value, list):
            assert after_value == value
        else:
            assert after_value == [value]

    assetversion = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=1, required_fields=["version", "asset.name"])
    assetversions = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=5, required_fields=["version", "asset.name", "task"])

    set_and_assert_equal(assetversion, "version", 5)
    set_and_assert_equal(assetversion, "asset.name", "foobar")

    set_and_assert_equal(assetversions, "version", [1, 2, 99, 4, 5])

    assets = assetversions.asset
    assetnames = ["new_assetname_{}".format(idx) for idx in range(len(assets))]
    set_and_assert_equal(assets, "name", assetnames)

    task = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=1, required_fields=["task"]).task
    set_and_assert_equal(assetversion, "task", task)

    tasks = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "Task", limit=5, required_fields=["name"])
    set_and_assert_equal(assetversions, "task", tasks)

    assetversions_with_links = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=2, required_fields=["uses_versions"])
    set_and_assert_equal(assetversions_with_links[0], "uses_versions", assetversions_with_links[1])

    #assetversions_with_links = self.construct_simple_collection(AssetVersion, 2, ["used_in_versions"])
    #set_and_assert_equal(assetversions_with_links[0], "used_in_versions", assetversions_with_links[1])
    # TODO(T13213): this does not work, as ftrack seemingly only updates these connections
    # once we commit
    # self.assertIn(assetversions_with_links[0], assetversions_with_links[1].used_in_versions)

def test_group(scenario_asset_task_version, ftrack_session):
    assetversion_collection = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=5)
    expected_keys = assetversion_collection._entities.keys()
    grouped = assetversion_collection.group(lambda x: x.id[0])

    assert isinstance(grouped, dict)
    assert expected_keys == grouped.keys()

    for key, value in grouped.items():
        assert [key] == [_.ftrack_entity["id"] for _ in value._entities.values()]

def test_fold(scenario_asset_task_version, ftrack_session):
    assetversion_collection = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "AssetVersion", limit=1, required_fields=["asset.versions.user.username", "user.username"])

    user_assetversions = {}
    all_assetversions = []

    for assetversion in assetversion_collection._entities.values():
        for asset_assetversion in assetversion.ftrack_entity["asset"]["versions"]:
            user = asset_assetversion["user"]["username"]
            if user not in user_assetversions:
                user_assetversions[user] = 1
            else:
                user_assetversions[user] += 1
            all_assetversions.append(asset_assetversion)

    for user in user_assetversions:
        assert user_assetversions[user] == scenario_asset_task_version.construct_collection_from_ftrack_entities(
            all_assetversions).fold(0, lambda x, y: x + 1 if y.user.username == [user] else x)

def test_keys(scenario_asset_task_version, ftrack_session):
    ftrack_entities = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    assetversion_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    assert list(assetversion_collection.keys()) == [_["id"] for _ in ftrack_entities]

def test_values(scenario_asset_task_version, ftrack_session):
    ftrack_entities = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    assetversion_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    assert [_.ftrack_entity for _ in assetversion_collection.values()] == ftrack_entities

def test_max(scenario_asset_task_version, ftrack_session):
    ftrack_entities = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", ["version"], 10)
    assetversion_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)

    assert [_.ftrack_entity["version"] for _ in assetversion_collection.max(lambda x: x.version).values()] \
           == [max([_["version"] for _ in ftrack_entities])]

    ftrack_entities = scenario_asset_task_version.grab(
        ftrack_session, "Asset", ["versions.version", "versions.asset"], 10)
    all_assetversions = []
    for asset in ftrack_entities:
        for assetversion in asset["versions"]:
            all_assetversions.append(assetversion)
    all_assetversions.sort(key=lambda x: x["version"])
    asset_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    assert [_.ftrack_entity for _ in asset_collection.max(lambda x: x.versions.version).values()] \
        == [all_assetversions[-1]["asset"]]

def test_min(scenario_asset_task_version, ftrack_session):
    ftrack_entities = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", ["version"], 10)
    assetversion_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    assert [_.ftrack_entity["version"] for _ in assetversion_collection.min(lambda x: x.version).values()] \
           == [min([_["version"] for _ in ftrack_entities])]

    ftrack_entities = scenario_asset_task_version.grab(
        ftrack_session, "Asset", ["versions.version", "versions.asset"], 10)
    all_assetversions = []
    for asset in ftrack_entities:
        for assetversion in asset["versions"]:
            all_assetversions.append(assetversion)
    all_assetversions.sort(key=lambda x: x["version"])
    asset_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    assert [_.ftrack_entity for _ in asset_collection.min(lambda x: x.versions.version).values()] \
        == [all_assetversions[0]["asset"]]

def test_sort_by(scenario_asset_task_version, ftrack_session):
    ftrack_entities = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", ["version"], 10)

    # section sort by version
    sorted_ftrack_entities = sorted(ftrack_entities, key=lambda x: x["version"])
    unsorted_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    sorted_collection = unsorted_collection.sort(lambda x: x.version)
    assert sorted_ftrack_entities == [_.ftrack_entity for _ in sorted_collection._entities.values()]

    # section sort by id
    sorted_ftrack_entities = sorted(ftrack_entities, key=lambda x: x["id"])
    sorted_collection = unsorted_collection.sort(lambda x: x.id)
    assert sorted_ftrack_entities == [_.ftrack_entity for _ in sorted_collection._entities.values()]
    simple_task_collection = scenario_asset_task_version.construct_simple_collection(
        ftrack_session, "Task", 10)
    sorted_ftrack_entities = sorted(
        [_.ftrack_entity for _ in simple_task_collection.values()],
        key=lambda x: x["id"])
    sorted_collection = simple_task_collection.sort(lambda x: x.id)
    assert sorted_ftrack_entities == [_.ftrack_entity for _ in sorted_collection._entities.values()]

def test_filter(scenario_asset_task_version, ftrack_session):
    repeat = True
    while repeat:
        ftrack_entities = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", ["version"], 10)
        filtered_ftrack_entities = [_ for _ in ftrack_entities if 1 < _["version"] < 20]
        # we can only test filtering properly if our result differs
        if len(filtered_ftrack_entities) != len(ftrack_entities):
            repeat = False

    # section sort by id
    unfiltered_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    filtered_collection = unfiltered_collection.filter(lambda x: 1 < x.version[0] < 20)
    assert filtered_ftrack_entities == [_.ftrack_entity for _ in filtered_collection._entities.values()]

def test_partition(scenario_asset_task_version, ftrack_session):
    ftrack_entities = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", ["version"], 20)
    assetversion_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(ftrack_entities)
    versions_one = [_ for _ in ftrack_entities if _["version"] == 1]
    versions_not_one = [_ for _ in ftrack_entities if _["version"] != 1]
    collection_one, collection_not_one = assetversion_collection.partition(lambda x: x.version[0] == 1)
    assert versions_one ==  [_.ftrack_entity for _ in collection_one._entities.values()]
    assert versions_not_one == [_.ftrack_entity for _ in collection_not_one._entities.values()]

def test_union(scenario_asset_task_version, ftrack_session):
    entities_a = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    entities_b = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    entities_c = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    entities_d = entities_c[0:2]

    ftrack_entities_union = []
    for ftrack_entities in [entities_a, entities_b, entities_c, entities_d]:
        for ftrack_entity in ftrack_entities:
            if not ftrack_entity in ftrack_entities_union:
                ftrack_entities_union.append(ftrack_entity)

    collection_a = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_a)
    collection_b = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_b)
    collection_c = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_c)
    collection_d = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_d)
    collection_union = collection_a.union(collection_b, collection_c, collection_d)

    assert ftrack_entities_union == [_.ftrack_entity for _ in collection_union._entities.values()]

    typedcontext = scenario_asset_task_version.grab(ftrack_session, "Shot", limit=100)
    typedcontext_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(typedcontext)
    # Ftrack will never return a generic TypedContext. To recreate a situation
    # that we encounter in our API, we have to set the type explicitly.
    typedcontext_collection._entity = TypedContext()
    emptycollection = EmptyCollection(_type=Task())

    task = scenario_asset_task_version.grab(ftrack_session, "Task", limit=10)
    task_collection = scenario_asset_task_version.construct_collection_from_ftrack_entities(task)
    emptycollection.union(task_collection)

def test_symmetric_difference(scenario_asset_task_version, ftrack_session):
    entities_a = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=18)
    entities_b = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=15)
    entities_c = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=12)
    entities_d = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    all_entities = [set(entities_a), set(entities_b), set(entities_c), set(entities_d)]

    ftrack_entities_difference = {key for key, val in Counter(chain.from_iterable(all_entities)).items() if val == 1}

    collection_a = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_a)
    collection_b = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_b)
    collection_c = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_c)
    collection_d = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_d)
    collection_difference = collection_a.symmetric_difference(collection_b, collection_c, collection_d)
    assert ftrack_entities_difference == {_.ftrack_entity for _ in collection_difference._entities.values()}

def test_difference(scenario_asset_task_version, ftrack_session):
    entities_a = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=18)
    entities_b = scenario_asset_task_version.grab(ftrack_session, "Task", limit=15)
    entities_c = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=12)
    entities_d = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=10)
    all_entities = entities_a + entities_b + entities_c + entities_d

    ftrack_entities_difference = [
        _ for _ in all_entities if _ in
        list(set(entities_a).difference(entities_b).difference(entities_c).difference(entities_d))
    ]

    collection_a = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_a)
    collection_b = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_b)
    collection_c = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_c)
    collection_d = scenario_asset_task_version.construct_collection_from_ftrack_entities(entities_d)
    collection_difference = collection_a.difference(collection_b, collection_c, collection_d)
    assert ftrack_entities_difference == [_.ftrack_entity for _ in collection_difference._entities.values()]


def test_intersection(scenario_asset_task_version, ftrack_session):
    all_versions = scenario_asset_task_version.grab(ftrack_session, "AssetVersion", limit=50)
    expected_versions = all_versions[:10]
    additional_versions = all_versions[10:]

    collection1 = scenario_asset_task_version.construct_collection_from_ftrack_entities(
        expected_versions + additional_versions[5:30])
    collection2 = scenario_asset_task_version.construct_collection_from_ftrack_entities(
        list(reversed(expected_versions)) + additional_versions[15:20])
    collection3 = scenario_asset_task_version.construct_collection_from_ftrack_entities(
        expected_versions + additional_versions[1:9])

    collection_intersection = collection1.intersection(collection2, collection3)
    assert expected_versions == [_.ftrack_entity for _ in collection_intersection._entities.values()]

    # test with ambiguous parent context
    shots = scenario_asset_task_version.grab(ftrack_session, "Shot", ["assets"], 2)
    asset_build = scenario_asset_task_version.grab(ftrack_session, "AssetBuild", ["assets"])

    mix = [shots[0]["assets"][0], asset_build[0]["assets"][0]]
    collection4 = scenario_asset_task_version.construct_collection_from_ftrack_entities(mix)
    collection5 = scenario_asset_task_version.construct_collection_from_ftrack_entities([shots[1]["assets"][0]])
    assert not collection4.intersection(collection5)

def test_type_coercion(scenario_components, ftrack_session):
    collection1 = scenario_components.construct_simple_collection(ftrack_session, "Component", limit=10)
    coerced_collection1 = Component(collection1)
    collection2 = scenario_components.construct_simple_collection(ftrack_session, "Sequence", limit=2)
    coerced_collection2 = TypedContext(collection2)
    collection_packet = [
        (collection1, coerced_collection1, Component),
        (collection2, coerced_collection2, TypedContext)]

    for collection, coerced_collection, _type in collection_packet:
        assert isinstance(coerced_collection, EntityCollection)
        assert [_.id for _ in collection.values()] == [_.id for _ in coerced_collection.values()]
        assert coerced_collection.entity_type == _type
        with pytest.raises(AssertionError):
            AssetVersion(collection)
