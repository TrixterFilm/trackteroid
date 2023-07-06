import dbm
import os
import platform
import shutil
import tempfile

import ftrack_api
import pytest


from trackteroid import (
    SESSION,
    Query,
    AssetVersion,
    User
)


@pytest.fixture
def dumped_operations_file():
    yield os.path.join(tempfile.gettempdir(), "operations.dbm")


@pytest.fixture
def initial_operations():
    # these contents need to match the operations in the given resource file
    test_data = {
        "username": "demo.user@example.com",
        "first_name": "demo",
        "last_name": "user",
        "is_active": True
    }
    yield (
        f"{os.path.dirname(__file__)}/resources/session"
        f"/operations_{'windows' if platform.platform().startswith('Windows') else 'linux'}.dbm",
        test_data
    )
    with ftrack_api.Session(auto_populate=False, auto_connect_event_hub=False) as session:
        demo_user = session.query(
            f"select first_name, last_name from User where username is \"{test_data['username']}\""
        ).first()
        if demo_user:
            session.delete(demo_user)
            session.commit()


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


def test_reconnect_and_commit(initial_operations):

    SESSION.reconnect_and_commit(initial_operations[0])

    user = Query(User).by_name(initial_operations[1]["username"]).get_one(
        projections=["first_name", "last_name", "is_active"]
    )
    assert initial_operations[1]["first_name"] == user.first_name[0]
    assert initial_operations[1]["last_name"] == user.last_name[0]
    assert initial_operations[1]["is_active"] is True


def test_get_cached_collections(initial_operations):
    SESSION.reconnect_and_commit(initial_operations[0])

    users = SESSION.get_cached_collections()[User].fetch_attributes("first_name", "last_name", "is_active")

    users_split = users.partition(lambda u: u.username[0] == initial_operations[1]["username"])
    assert users_split[0].first_name == [initial_operations[1]["first_name"]]
