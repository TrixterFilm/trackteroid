import random
import uuid
from collections import OrderedDict

import pytest

from trackteroid import (
    Query,
    Sequence,
    Project,
    Shot,
    Task,
    PROJECT_SCHEMAS,
    TASK_TYPES,
    NoteCategory,
    Note,
)
from trackteroid.entities.base import EntityCollection, Entity


def test_link_inputs(scenario_sequence):
    sequences = (
        Query(Sequence).by_id(*scenario_sequence.sequence_ids).get_all(order_by="name")
    )
    sequence1 = sequences[0]
    sequence2 = sequences[1]
    sequence3 = sequences[2:4]

    after_link1 = sequence1.link_inputs(sequence2)
    after_link2 = sequence2.link_inputs(sequence3)

    assert isinstance(after_link1, EntityCollection)
    assert "Sequence" == after_link1._entity.__class__.__name__
    assert isinstance(after_link2, EntityCollection)
    assert "Sequence" == after_link2._entity.__class__.__name__

    sequence1.commit()

    assert (
            Query(Sequence)
            .by_id(*sequence1.id)
            .get_one(projections=["incoming_links.from_id"])
            .incoming_links.from_id
            == sequence2.id
    )

    assert (
        Query(Sequence)
        .by_id(*sequence2.id)
        .get_one(projections=["incoming_links.from_id"])
        .incoming_links.from_id
        == sequence3.id,
    )


def test_create(scenario_project, ftrack_session):
    project = Query(Project).by_id(scenario_project.project_id).get_one()

    test_entities = []

    # create a sequence
    sequence = project.children[Sequence].create(name="Sequence")
    test_entities.append(("Sequence", sequence.id[0]))

    # create some shots
    shot1 = sequence.children[Shot].create(name="Shot1")
    shot2 = sequence.children[Shot].create(name="Shot2")
    test_entities.append(("Shot", shot1.id[0]))
    test_entities.append(("Shot", shot2.id[0]))

    # create some tasks["name
    shot1_task1, shot1_task2 = shot1.children[Task].create_batch(
        {"name": "Modeling", "type": "Modeling"},
        {"name": "Rigging", "type": "Rigging"},
    )
    shot2_tasks = shot2.children[Task].create_batch(
        {"name": "Modeling", "type": "Modeling"},
    )
    shot2_tasks2 = shot2_tasks.create_batch(
        {"name": "Rigging", "type": "Rigging"},
        {"name": "Animation", "type": "Animation"},
    )
    tasks = [
        shot1_task1,
        shot1_task2,
        shot2_tasks,
        shot2_tasks2,
    ]
    for task in tasks:
        for id in task.id:
            test_entities.append(("Task", id))

    asset_types = ftrack_session.query("AssetType").all()

    # create some assets
    asset1 = shot1.assets.create(name="Asset1", type=asset_types[0]["name"])
    asset2 = shot1.assets.create(name="Asset2", type=asset_types[1]["name"])
    test_entities.append(("Asset", asset1.id[0]))
    test_entities.append(("Asset", asset2.id[0]))

    # create some versions
    assetversion1 = asset1.versions.create(task=shot1_task1)
    assetversion2 = asset2.versions.create(task=shot1_task2)
    test_entities.append(("AssetVersion", assetversion1.id[0]))
    test_entities.append(("AssetVersion", assetversion2.id[0]))

    # link some versions
    assetversion1.link_outputs(assetversion2)

    # push to server
    project.commit()

    retrieved_entities = []
    for entity in test_entities:
        retrieved_entities.append(ftrack_session.get(*entity))
    assert all(retrieved_entities), "Some entities were not created"


def test_create_project(ftrack_session):
    some_project = Query(Project).get_first()

    with pytest.raises(AssertionError):
        some_project.create()

    with pytest.raises(AssertionError):
        some_project.create(name="Foobar")

    with pytest.raises(AssertionError):
        some_project.create(name="Foobar", project_schema="DuDoedl")

    created_project = some_project.create(
        name=str(uuid.uuid4()),
        project_schema=random.choice(list(PROJECT_SCHEMAS.types.keys())),
    )

    try:
        assert isinstance(created_project, EntityCollection)
        assert "Project" == created_project._entity.__class__.__name__

        created_project.commit()

        assert Query(Project).by_id(*created_project.id).get_one() == created_project
    finally:
        ftrack_session.delete(ftrack_session.get("Project", created_project.id[0]))
        ftrack_session.commit()


def test_create_sequence(scenario_project):
    test_project = Query(Project).by_id(scenario_project.project_id).get_one()

    with pytest.raises(AssertionError):
        test_project.children[Sequence].create()

    created_sequence = test_project.children[Sequence].create(name=str(uuid.uuid4()))

    assert isinstance(created_sequence, EntityCollection)
    assert "Sequence" == created_sequence._entity.__class__.__name__

    test_project.commit()

    queried_sequence = Query(Sequence).by_id(*created_sequence.id).get_one()
    assert isinstance(queried_sequence, EntityCollection)
    assert test_project.id == queried_sequence.parent_id


def test_create_shot(scenario_sequence):
    test_sequence = (
        Query(Sequence).by_id(Project, scenario_sequence.project_id).get_all()
    )

    with pytest.raises(AssertionError):
        test_sequence.children[Shot].create()

    with pytest.raises(AssertionError) as excinfo:
        test_sequence.children[Shot].create(name=str(uuid.uuid4()))

    assert "Ambiguous context" in str(excinfo.value)

    test_sequence = (
        Query(Sequence).by_id(Project, scenario_sequence.project_id).get_first()
    )
    created_shot = test_sequence.children[Shot].create(name=str(uuid.uuid4()))

    assert isinstance(created_shot, EntityCollection)
    assert "Shot" == created_shot._entity.__class__.__name__

    test_sequence.commit()

    queried_shot = Query(Shot).by_id(*created_shot.id).get_one()
    assert queried_shot == created_shot
    assert test_sequence.id == queried_shot.parent_id


def test_create_task(scenario_shot):
    test_shot = (
        Query(Shot)
        .by_id(Project, scenario_shot.project_id)
        .get_all(projections=["project.project_schema._task_type_schema.types.name"])
    )
    task_types = [
        TASK_TYPES._to_camel_case(_)
        for _ in test_shot.project.project_schema._task_type_schema.types.name
    ]

    with pytest.raises(AssertionError) as context:
        test_shot.children[Task].create()

    with pytest.raises(AssertionError) as context:
        test_shot.children[Task].create(name=str(uuid.uuid4()))

    with pytest.raises(AssertionError) as context:
        test_shot.children[Task].create(
            name=str(uuid.uuid4()), type=random.choice(task_types)
        )
    assert "Ambiguous context" in str(context.value)

    test_shot = Query(Shot).by_id(Project, scenario_shot.project_id).get_first()

    created_task = test_shot.children[Task].create(
        name=str(uuid.uuid4()), type=random.choice(task_types)
    )

    assert isinstance(created_task, EntityCollection)
    assert "Task" == created_task._entity.__class__.__name__

    test_shot.commit()

    queried_task = Query(Task).by_id(*created_task.id).get_one()

    assert queried_task == created_task
    assert test_shot.id == queried_task.parent_id


def _construct_collection_from_ftrack_entities(ftrack_entities, session):
    import trackteroid.entities
    assert ftrack_entities

    if not isinstance(ftrack_entities, list):
        ftrack_entities = [ftrack_entities]
    entities = []

    for ftrack_entity in ftrack_entities:
        entities.append(
            (
                ftrack_entity["id"],
                Entity(
                    _cls=getattr(trackteroid.entities, ftrack_entity.entity_type),
                    ftrack_entity=ftrack_entity,
                ),
            )
        )

    collection = EntityCollection(
        _cls=entities[0][1].__class__, entities=OrderedDict(entities), session=session
    )
    collection.query = Query(entities[0][1].__class__).by_id(*[_["id"] for _ in ftrack_entities])
    return collection


def test_create_on_ambigious_context(scenario_shot_asset, scenario_assetbuild_asset, ftrack_session):
    shots = scenario_shot_asset.grab(ftrack_session, "Shot", ["assets.id"])
    asset_builds = scenario_assetbuild_asset.grab(ftrack_session, "AssetBuild", ["assets.id"])

    mix = [shots[0]["assets"][0], asset_builds[0]["assets"][0]]

    collection4 = _construct_collection_from_ftrack_entities(mix, ftrack_session)

    collection5 = _construct_collection_from_ftrack_entities(
        shots[1]["assets"][0], ftrack_session
    )

    asset_type = ftrack_session.query("AssetType").first()
    with pytest.raises(AssertionError) as context:
        collection4.intersection(collection5).create(
            name=str(uuid.uuid4()), type=asset_type["name"]
        )
    assert "Ambiguous context" in str(context.value)


def test_create_note(scenario_shot):
    categories = Query(NoteCategory).get_all()
    # Run it three times, once on an empty collection, another in a collection
    # with a single entity and then two (this last one will test that the parent
    # ambiguity error is not raised)
    for i in range(3):
        chosen_category = random.choice(categories)
        # Query every time to ensure the cache is not fooling the tests
        test_shot = Query(Shot).by_id(*scenario_shot.shot_ids).get_first(projections=["notes.content"])

        assert (
                len(test_shot.notes) == i
        ), "Expected shot to have {} notes, {} found".format(i, len(test_shot.notes))

        with pytest.raises(AssertionError):
            test_shot.notes.create(contents="A note", category="A String")

        note = test_shot.notes.create(content="A note", category=chosen_category)
        note.commit()

        # For some unknown reason, note.commit() converts parent_type to "Resource", so we can ignore testing
        # the parent_type, as it'll be wrong anyway
        assert (
                note.parent_id[0] == test_shot.id[0]
        ), "Expected parent id {!r}, got {!r}".format(
            test_shot.id[0], note.parent_id[0]
        )

        # To ensure it's on the entity and not only on the session cache, a new query
        # should do the trick
        notes = Query(Note).inject("parent_id is {}".format(test_shot.id[0])).get_all()
        assert len(notes) == (i + 1), "Expected {} notes, {} found".format(
            i + 1, len(notes)
        )
        assert (
                notes.filter(lambda x: x.id[0] == note.id[0]).category.name[0]
                == chosen_category.name[0]
        )
