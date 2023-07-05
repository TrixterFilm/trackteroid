import dataclasses
import uuid
from typing import List

import ftrack_api
import pytest

from trackteroid import SESSION


@dataclasses.dataclass
class TestScenario:
    project_id: str
    sequence_ids: List[str] = dataclasses.field(default_factory=list)
    shot_ids: List[str] = dataclasses.field(default_factory=list)
    assetbuild_ids: List[str] = dataclasses.field(default_factory=list)
    task_ids: List[str] = dataclasses.field(default_factory=list)
    asset_ids: List[str] = dataclasses.field(default_factory=list)
    version_ids: List[str] = dataclasses.field(default_factory=list)
    component_ids: List[str] = dataclasses.field(default_factory=list)

    def query_project(self, session, projections):
        return session.query(
            f"select {', '.join(projections)} from Project "
            f"where id is {self.project_id}"
        ).one()

    def grab(self, session, entity_type, required_fields):

        type_ids = {
            "Sequence": self.sequence_ids,
            "Shot": self.shot_ids,
            "AssetBuild": self.assetbuild_ids,
            "Task": self.task_ids,
            "Asset": self.asset_ids,
            "AssetVersion": self.version_ids,
            "Component": self.component_ids,
        }

        if entity_type not in type_ids:
            raise KeyError(entity_type)
        if not type_ids[entity_type]:
            raise ValueError(f"No entities of type {entity_type} exists in the scenario")

        query = f"select {', '.join(required_fields)} from {entity_type} where "
        for field in required_fields:
            query += f"{field} like '%' "
        query += f"and id in ({', '.join(type_ids[entity_type])})"
        return session.query(query).all()


@pytest.fixture(autouse=True)
def reconnect_session():
    return SESSION.reconnect()


@pytest.fixture()
def ftrack_session():
    with ftrack_api.Session() as session:
        yield session


@pytest.fixture(scope="session")
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
    return TestScenario(project_id=ftrack_project_id)


@pytest.fixture
def scenario_sequence(ftrack_session, scenario_project) -> TestScenario:
    project = scenario_project.query_project(ftrack_session, ["project_schema"])

    # Create sequences, shots and tasks.
    for sequence_number in range(1, 5):
        sequence = ftrack_session.create(
            "Sequence",
            {"name": "seq_{0}".format(uuid.uuid4()), "parent": project},
        )

        scenario_project.sequence_ids.append(sequence["id"])
    ftrack_session.commit()
    return scenario_project


@pytest.fixture
def scenario_assetbuild(ftrack_session, scenario_project) -> TestScenario:
    project = scenario_project.query_project(ftrack_session, ["project_schema"])

    for _ in range(4):
        sequence = ftrack_session.create(
            "AssetBuild",
            {"name": "ab_{0}".format(uuid.uuid4()), "parent": project},
        )

        scenario_project.assetbuild_ids.append(sequence["id"])
    ftrack_session.commit()
    return scenario_project


@pytest.fixture
def scenario_shot(ftrack_session, scenario_sequence) -> TestScenario:
    project = scenario_sequence.query_project(ftrack_session, ["project_schema"])
    project_schema = project["project_schema"]
    default_shot_status = project_schema.get_statuses("Shot")[0]

    for sequence_id in scenario_sequence.sequence_ids:
        sequence = ftrack_session.get("Sequence", sequence_id)
        for shot_number in range(1, 8):
            shot = ftrack_session.create(
                "Shot",
                {
                    "name": "shot_{}".format(uuid.uuid4()),
                    "parent": sequence,
                    "status": default_shot_status,
                },
            )
            scenario_sequence.shot_ids.append(shot["id"])
    ftrack_session.commit()
    return scenario_sequence


def _create_tasks(session, scenario, parent_ids):
    for id_ in parent_ids:
        parent = session.get("TypedContext", id_)
        for task_number in range(1, 5):
            task = session.create(
                "Task",
                {
                    "name": "task_{0}".format(uuid.uuid4()),
                    "parent": parent
                },
            )
            scenario.task_ids.append(task["id"])

    session.commit()
    return scenario


@pytest.fixture
def scenario_shot_task(ftrack_session, scenario_shot) -> TestScenario:
    return _create_tasks(ftrack_session, scenario_shot, scenario_shot.shot_ids)


@pytest.fixture
def scenario_assetbuild_task(ftrack_session, scenario_shot) -> TestScenario:
    return _create_tasks(ftrack_session, scenario_shot, scenario_shot.assetbuild_ids)


def _create_assets(session, scenario, parent_ids):
    for id_ in parent_ids:
        parent = session.get("TypedContext", id_)
        for task_number in range(1, 5):
            task = session.create(
                "Asset",
                {
                    "name": "asset_{0}".format(uuid.uuid4()),
                    "parent": parent
                },
            )
            scenario.asset_ids.append(task["id"])

    session.commit()
    return scenario


@pytest.fixture
def scenario_shot_asset(ftrack_session, scenario_shot) -> TestScenario:
    return _create_assets(ftrack_session, scenario_shot, scenario_shot.shot_ids)


@pytest.fixture
def scenario_assetbuild_asset(ftrack_session, scenario_assetbuild) -> TestScenario:
    return _create_assets(ftrack_session, scenario_assetbuild, scenario_assetbuild.assetbuild_ids)
