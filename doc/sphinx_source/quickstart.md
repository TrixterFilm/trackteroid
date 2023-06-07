# Quickstart

Eager to get started? This page give some introduction to the core concepts of Trackteroid. 
Follow [Installation](installation.md) and install Trackteroid first. Ideally you also have a basic understanding of the [Ftrack Python API](https://ftrack-python-api.readthedocs.io/en/stable/index.html).


## A Minimal Example
This example assumes you have [configured the api access for Ftrack](https://ftrack-python-api.readthedocs.io/en/stable/understanding_sessions.html) accordingly.

### Accessing Data From FTrack

```python
from trackteroid import (
    Query,
    AssetVersion
)

version_collection = Query(AssetVersion).get_first()
print(version_collection)

# output: EntityCollection[AssetVersion]{1}
```

#### The Query

In order to receive data from the Ftrack Server you need to perform queries. 
The `Query` class is the entry point for your data access and needs to be initialized with the entity type you want to receive: `Query(<Entity>)`.

In the prior example we want to receive any `AssetVersion`, but only take the first we will get from the server. Any `get_` method on the Query instance we do refer to as 
**terminators**. Terminators will do send the resolved query instruction to the server to fetch the data.

You can also resolve the query without actually sending it to the server by just printing it or calling `str` on it.
```python
print(Query(AssetVersion))

# output: select id, asset.name, version from AssetVersion
```

#### Projections

When you want to access data on your query result you have to ensure to that you project the attributes you need to access later.
A typical resolved query looks like this:

`select <projections> from <entity type> where <criteria>`

If you take a look at the prior example you can see that this included `id`, `asset.name` and `version`. This is because 
some attributes are so common to access that it can be predefined for some entity types.

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
You will receive a `Symbol(NOT_SET)` when data wasn't already fetched, but you're trying to access it. 
Nested relationships within the attributes are described via dot notation.

```python
print(Query(AssetVersion).get_first(projections=["comment", "asset.parent.project.name"]).asset.parent.project.name)

# output: [u'DummyProject']
```
As you can already guess knowing these relationships is not necessarily easy and writing queries can become long. Luckily for many relationships there is a way shorter and easier alternative.
```python
from trackteroid import (
    Query,
    AssetVersion,
    Project
)

version_collection = Query(AssetVersion).get_first(projections=[Project.name])

# output: trackteroid.query> INFO | Performing query: "select asset.name, task.project.name, id, version from Asset"

# The abbreviation is not only working for projections, but also via attribute access on the resulting collection
print(
    version_collection.task.project.name,
    version_collection.Project.name
)

# output: ([u'DummyProject'], [u'DummyProject'])
```

#### Filtering


#### Collections


#### Defining Relationships


### Transforming, Filtering and Option handling

#### Set Operations

#### Transformation Methods


### Authoring

#### CRUD (Create, Read, Update, Delete)



