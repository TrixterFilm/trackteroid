import os
import shutil
import tempfile

import pytest

from trackteroid import SESSION, Query, AssetVersion
import dbm


@pytest.fixture
def dumped_operations_file():
    temp = tempfile.gettempdir()
    yield os.path.join(temp, "operations.dbm")
    # TODO: This fails as it's in use when it reaches teardown. Why?
    # shutil.rmtree(temp)


@pytest.fixture
def initial_operations_file():
    return os.path.join(tempfile.gettempdir(), "operations.dbm")


def test_deferred_operations(dumped_operations_file):
    # case 1. clear an existing cache temporarily
    query_result = Query(AssetVersion).get_first(projections=["task", "version"])
    operations_count = len(SESSION.recorded_operations)

    # do a query -> cache a result
    with SESSION.deferred_operations(dumped_operations_file):
        assert 0 == len(SESSION.recorded_operations)

        avs = Query(AssetVersion).by_id(*query_result.id).get_one(projections=["task"])
        avs.version = avs.version[0] + 10
        avs2 = avs.create(task=avs.task)  # -> create entity, update task, update asset
        avs2.version = avs.version[0] + 10

        assert 5 == len(SESSION.recorded_operations)

    assert operations_count == len(SESSION.recorded_operations)
    # check the created file database
    database = dbm.open(dumped_operations_file, "r")

    def make_keys(entity_collection):
        return entity_collection.map(
            lambda x: "('{}', ['{}'])".format(x.entity_type.__name__, x.id[0])
        )

    expected_keys = make_keys(avs.union(avs2)) + make_keys(avs.task) + make_keys(avs.asset) + ["__operations__"]
    assert expected_keys, database.keys()


def test_reconnect_and_commit(initial_operations_file):



    SESSION.reconnect_and_commit(initial_operations_file)

    assetversion = Query(AssetVersion).by_id("fbb682b6-e9e6-4111-8edb-38d0797c9ffe").get_one(
        projections=["components.name"]
    )
    assert 99 == assetversion.version[0]
    assert "pymelle" == assetversion.components.name[0]


def test_get_cached_collections(initial_operations_file):
    SESSION.reconnect_and_commit(initial_operations_file)

    avs = SESSION.get_cached_collections()[AssetVersion]
    avs.fetch_attributes("asset.versions")

    v99, rest = avs.asset.versions.partition(lambda x: x.version[0] == 99)
    v99.uses_versions = rest

    SESSION.commit()