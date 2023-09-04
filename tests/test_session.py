import dbm
import os
import platform
import tempfile

import ftrack_api
import pytest


from trackteroid import (
    Query,
    Shot,
    User
)

from trackteroid.session import Session


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
    session = Session()
    operations_count = len(session.recorded_operations)
    query_result = Query(Shot).get_first(projections=["name"])

    # do a query -> cache a result
    with session.deferred_operations(dumped_operations_file):
        assert 0 == len(session.recorded_operations)

        shot = Query(Shot).by_id(*query_result.id).get_one(projections=["name"])
        print(shot)
        shot.name = "first shot"
        shot2 = shot.create(name="second shot")  # -> create entity, update task, update asset
        shot2.name = "second shot renamed"

        assert 4 == len(session.recorded_operations)

    assert operations_count == len(session.recorded_operations)
    # check the created file database
    database = dbm.open(dumped_operations_file, "r")

    def make_keys(entity_collection):
        return entity_collection.map(
            lambda x: "('{}', ['{}'])".format(x.entity_type.__name__, x.id[0])
        )

    expected_keys = make_keys(shot.union(shot2)) + ["__operations__"]
    assert expected_keys, database.keys()


def test_reconnect_and_commit(initial_operations):
    session = Session()
    session.reconnect_and_commit(initial_operations[0])

    user = Query(User).by_name(initial_operations[1]["username"]).get_one(
        projections=["first_name", "last_name", "is_active"]
    )
    assert initial_operations[1]["first_name"] == user.first_name[0]
    assert initial_operations[1]["last_name"] == user.last_name[0]
    assert initial_operations[1]["is_active"] is True


def test_get_cached_collections(initial_operations):
    session = Session()
    session.reconnect_and_commit(initial_operations[0])

    cached_users = session.get_cached_collections()[User]
    for cached_user in cached_users:
        user = Query(User).by_id(cached_user.id[0]).get_first(projections=["username", "first_name"])
        assert user, "Cached user does not exist: {}".format(cached_user.id[0])
        users_split = user.partition(lambda u: u.username[0] == initial_operations[1]["username"])
        assert users_split[0].first_name == [initial_operations[1]["first_name"]]
