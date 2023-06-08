# Quickstart

Eager to get started? This page give some introduction to the core concepts of Trackteroid. 
Follow [Installation](installation.md) and install Trackteroid first. Ideally you should also have a basic understanding of the [Ftrack Python API](https://ftrack-python-api.readthedocs.io/en/stable/index.html).

The following examples assumes you have [configured the api access for Ftrack](https://ftrack-python-api.readthedocs.io/en/stable/understanding_sessions.html) accordingly.

## Accessing Data From FTrack

```python
from trackteroid import (
    Query,
    AssetVersion
)

version_collection = Query(AssetVersion).get_first()
print(version_collection)

# output: EntityCollection[AssetVersion]{1}
```

### The Query

In order to receive data from the Ftrack server you need to perform queries. 
The `Query` class is the entry point for your data access and needs to be initialized with the entity type you want to receive: `Query(<Entity Type>)`.

In the prior example we want to receive any `AssetVersion`, but only take the first result from the server. Any `get_` method on the Query instance we do refer to as **terminators**. 
Terminators will send the resolved query instruction to the server and fetch the data. The result is a collection, namely an EntityCollection or an EmptyCollection instance. When printed this is being represented.

`EntityCollection[<Entity Type>]{<Number of Results>}` or `EmptyCollection[<Entity Type>]`

You can resolve the query without sending it to the server by just printing it or calling `str` on it.
```python
print(Query(AssetVersion))
# output: select id, asset.name, version from AssetVersion
```

#### Projections

When you want to access data on your resulting collection you have to ensure to that you _project_ the attributes you need to access later.
A typical resolved query looks like this:

`select <projections> from <entity type> where <criteria>`

If you take a look at the prior example you can see that `id`, `asset.name` and `version` have been included within the resolved query instruction. This is because some attributes are so common to access that it can be predefined for some entity types.

```python
print(AssetVersion.projections)
# output: ['id', 'asset.name', 'version']
```
Different to the Ftrack Python API the default Session within Trackteroid disables the auto-population feature. That means 
it will not automatically fetch missing data on attribute access on your query result.

```python
print(Query(AssetVersion).get_first().id)
# output: [u'00001180-b7e7-43cf-b0e5-a2df0cefe669']

print(Query(AssetVersion).get_first().comment)
# output: [Symbol(NOT_SET)]

print(Query(AssetVersion).get_first(projections=["comment"]).comment)
# output: [u'Hello World']
```
You will receive a `Symbol(NOT_SET)` when data wasn't fetched, but you're trying to access it. Nested relationships within the projections would be described via dot notation.

```python
print(
    Query(AssetVersion).get_first(
        projections=["comment", "asset.parent.project.name"]
    ).asset.parent.project.name
)
# output: [u'DummyProject']
```
As you can already guess knowing these relationships is not necessarily easy and written queries might become long. Luckily for many relationships there is a way shorter and easier alternative.
```python
from trackteroid import (
    Query,
    AssetVersion,
    Project
)

version_collection = Query(AssetVersion).get_first(projections=[Project.name])
# Performing query: "select asset.name, task.project.name, id, version from Asset"

# The abbreviation is not only working for projections, 
# but also via attribute access on the resulting collection
print(
    version_collection.task.project.name,
    version_collection.Project.name
)
# output: ([u'DummyProject'], [u'DummyProject'])
```

#### Filtering

To avoid fetching more data than you eventually needed and to keep your code as performant as possible you should try to narrow down the results directly via Query critiera.
Criteria methods are following a `by_` and `not_by_` name prefix and can be chained together. Different entity types expose different criteria methods but many share common ones.

```python
from trackteroid import (
    Query,
    AssetVersion
)

print(Query(AssetVersion).by_id("00001180-b7e7-43cf-b0e5-a2df0cefe669").get_all())
# output: EntityCollection[AssetVersion]{1}

# while you can technically also do 
# `Query(AssetVersion).by_id("00001180-b7e7-43cf-b0e5-a2df0cefe669").by_id("00001fd9-c8b8-4d84-8a8d-2c8fbbed46a0").get_all()`
print(
    Query(AssetVersion).by_id(
        "00001180-b7e7-43cf-b0e5-a2df0cefe669", 
        "00001fd9-c8b8-4d84-8a8d-2c8fbbed46a0"
    ).get_all()
)
# output: EntityCollection[AssetVersion]{2}

# get initial potential two AssetVersions of an Asset called 'SomeAsset'
print(Query(AssetVersion).by_name("SomeAsset").by_version(1, 2)).get_all()
# output: EntityCollection[AssetVersion]{2}

# get initial potential two AssetVersions of any Asset that is not called 'SomeAsset'
print(Query(AssetVersion).not_by_name("SomeAsset").by_version(1, 2)).get_all()
# output: EntityCollection[AssetVersion]{10}
```

It is also possible filtering via a pattern using the `%` placeholder representing "zero or more of any character".

```python
from trackteroid import (
    Query,
    Asset
)

print(Query(Asset).by_name("%Asset").get_all().name)
# output: [u'SomeAsset', u'SomeAsset', u'SomeAsset']

print(Query(Asset).by_name("Some%").get_all().name)
# output: [u'SomeAsset', u'SomeAsset', u'SomeAsset', u'SomeCharacter', u'SomeScene']

print(Query(Asset).by_name("%Asset%").get_all().name)
# output: [u'SomeAsset', u'SomeAsset', u'SomeAsset', u'AnAssetClone']
```


Often criteria describe the lookup of direct properties of an entity, like `id`, `name`, `metadata`. By default, they refer directly to the entity type that you want to receive as your results via `Query(<Entity Type>)`. 
But those criteria also support defining a so called **target** that allows you to specify for what entity type you want to refer to its property instead.

```python
from trackteroid import (
    Query,
    Asset,
    Project
)
print(Query(Asset).by_name("SomeAsset").get_all())
# output: EntityCollection[Asset]{3}
print(Query(Asset).by_name(Project, "DummyProject", "DummyProject2").get_all())
# output: EntityCollection[Asset]{10}
print(Query(Asset).by_name("SomeAsset").by_name(Project, "DummyProject", "DummyProject2").get_all())
# output: EntityCollection[Asset]{2}
```

Per criterion that enable target support, you can optionally provide exactly one target as the first positional argument to define the relationship for the property used within the criterion.

### Limiting and Ordering

The `get_all` terminator supports limiting and ordering results.

```python
from trackteroid import (
    Query,
    AssetVersion
)

# get all AssetVersions ordered descending by their version number across all Assets
print(Query(AssetVersion).get_all(limit=8, order="descending", order_by="version").version)
# output: [55, 43, 42, 22, 10, 10, 8, 7]
```

## Defining Relationships


## Collections

### Transforming, Filtering and Option handling

#### Set Operations

#### Transformation Methods


## Authoring

### CRUD (Create, Read, Update, Delete)



