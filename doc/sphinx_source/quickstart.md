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

```{include} query/overview.md
```

### Defining Relationships

One of the main objectives of Trackteroid is to minimize the need for in-depth knowledge of the underlying database structure when working with queries and resulting collections. This goal is accomplished through two distinct approaches.

Firstly, it automatically derives relationships whenever possible by dynamically inspecting the schema of the current session. This capability allows for seamless handling of relationships without requiring explicit configuration.

However, Ftrack's dynamic nature means that certain entity types may require configuring relationships to align with specific requirements. Trackteroid provides the flexibility to describe and represent contextual relationships for such cases, enabling customization and adaptation to meet individual needs by implementing a [resolver](configuration.md#relationships-resolver).


All communication with an Ftrack server is facilitated through a `Session` object. By default, a Query is constructed using the _SESSION_ singleton and the _default_ schema. Here's an example:
```python
from trackteroid import (
    AssetVersion,
    Query,
    SESSION,
)
from trackteroid.query import SCHEMA

# same as Query(AssetVersion)
Query(AssetVersion, session=SESSION, schema=SCHEMA.default)
```

However, you also have the flexibility to initialize your own `Session` object and provide a different schema. Here's an example:

```python
from trackteroid import (
    AssetVersion,
    Query,
    SESSION,
)
from trackteroid.query import SCHEMA
from trackteroid.session import Session

my_session = Session(server_url="<some_ftrack_server>")

Query(AssetVersion, session=my_session, schema=SCHEMA.vfx)
```

## Collections

```{include} collections/overview.md
```

`````{admonition} **Iterables all the way down!**
:class: important

Regardless of the number of entities it contains, whether it's multiple, single, or none at all, a collection remains iterable. 
This holds true even when requesting attributes that result in a primitive data type, such as strings. This consistent behavior allows for uniform usage across different scenarios and helps avoid the need for excessive conditional statements.

````{admonition} **In practice...**
:class: dropdown

```python
from trackteroid import (
    Query,
    Component,
    ComponentLocation,
    TypedContext
)

print(
    Query(TypedContext).get_all(
        limit=1, projections=[Component.name, ComponentLocation.resource_identifier]
    )[Shot] \
    .filter(lambda shot: shot.Component.name[0] == "main") \
    .ComponentLocation.resource_identifier[0] \
    or "Not existing"
)

print(
    Query(TypedContext).get_all(
        limit=10, projections=[Component.name, ComponentLocation.resource_identifier]
    )[Shot] \
    .filter(lambda shot: shot.Component.name[0] == "main") \
    .ComponentLocation.resource_identifier \
    or "Still not existing, even for multiple results"
)
```

The provided code demonstrates some of the capabilities of Trackteroid in handling complex scenarios without the need for explicit loops or excessive conditional statements. 
Although the code may seem complex at first glance, the following explanations will break it down step by step.

In the first part of the code, a single _TypedContext_ sample is retrieved using the _Query_ class. 
The limit parameter is set to 1 to fetch only one sample. The projections parameter is used to specify the desired attributes (_Component.name_ and _ComponentLocation.resource_identifier_) to be included in the result.

Next, the retrieved _TypedContext_ sample is filtered using the _[Shot]_ filter. This filter selects only the subtypes of _TypedContext_ that match the _Shot_ entity and ensures that only _Shot_ entities are considered in the subsequent operations. 
Since we are limiting the result of the _TypedContext_ query to only one entity, there is a possibility that the retrieved entity may not be a _Shot_. It could be of a different entity type, such as _AssetBuild_, _Sequence_, or _Folder_.
Following the filter, the _Shot_ sample is further filtered using the _filter_ method. In this case, the filter condition checks if the _Component_ name of any of the _Shot's_ _AssetVersions_ is equal to "main". 
Finally, the _resource_identifier_ attribute of a single _ComponentLocation_ is accessed. As we are anticipating only one result, the value is accessed using the [0] index. If a value is present, it is utilized; otherwise, the fallback string _"Not existing"_ is used.

The second part of the code follows a similar structure, but this time the limit parameter is set to 10 to retrieve 10 potential _TypedContext_ samples. 

No need to worry if you haven't fully grasped the concepts yet. Subsequent sections will provide further clarification.
````
`````

### Transformation, Fetching and Option Handling

The `EntityCollection` provides you with a lot of convenience for accessing, filtering and transforming containing data. 


#### Item & Attribute Access

Retrieving items from a collection is straightforward and effortless. 
These examples illustrate the versatility of the item getter on an EntityCollection.
```python
from trackteroid import (
    Query,
    AssetVersion,
    Shot,
    TypedContext
)

av_collection = Query(AssetVersion).get_all(limit=10)
print(av_collection)
# output: EntityCollection[AssetVersion]{10}

# get a new collection only containing the first item
first_av_collection = av_collection[0]
print(first_av_collection)
# output: EntityCollection[AssetVersion]{1}

# get a new collection via slices
last_av_collection = av_collection[-1]
print(last_av_collection)
# output: EntityCollection[AssetVersion]{1}

range_av_collection = av_collection[2:5]
print(range_av_collection)
# output: EntityCollection[AssetVersion]{3}

# get a new collection via some entity id
last_av_id = last_av_collection.id[0]
last_av_collection_from_id = av_collection[last_av_id]
# output: EntityCollection[AssetVersion]{1}

tc_collection = Query(TypedContext).get_all(limit=100)
print(tc_collection)
# output: EntityCollection[TypedContext]{100}

# get a new collection that only contains `Shot` subtypes
sh_collection = tc_collection[Shot]
print(sh_collection)
# output: EntityCollection[Shot]{8}
```

Accessing related collections and primitive data is user-friendly. 
This example demonstrates the seamless navigation through nested collections and the retrieval of primitive data stored in the _resource_identifier_ attribute of associated _component_locations_.
```python
from trackteroid import (
    Query,
    AssetVersion,
    Shot,
    TypedContext
)

av_collection = Query(AssetVersion).get_all(
    limit=1, 
    projections=[
        ComponentLocation.resource_identifier
    ]
)

print(av_collection.ComponentLocation.resource_identifier)
# expanded attribute access would be like this and the result be the same
print(av_collection.components.component_locations.resource_identifier)
# output: 
# [u'/path/to/some_file1.jpg', u'/path/to/some_file2.mov'] 
# [u'/path/to/some_file1.jpg', u'/path/to/some_file2.mov'] 

```
You can conveniently access individual attributes within the custom_attributes field by utilizing the `custom_` prefix as a shortcut. This allows direct access to specific attributes without the need to explicitly refer to the _custom_attributes_ field and retrieve values by their corresponding keys.
```python
from trackteroid import (
    Query,
    Shot
)

print(
    Query(Shot).get_all(limit=2, projections=["custom_attributes"]).custom_frame_start
)
# output: [1009.0, 1006.0]
print(
    Query(Shot).get_all(limit=2, projections=["custom_attributes"]).custom_frame_end
)
# output: [1055.0, 1015.0]
```

#### Transformation Methods

While iterating through loops is a valid approach, leveraging transformations can provide enhanced convenience. 
The EntityCollection class provides higher-order methods that accept functions as arguments, aligning with the principles of functional programming. 
The presented example highlights a subset of the transformation methods available.
```python
from pprint import pprint

from tracteroid import (
    Query,
    Asset,
    AssetVersion
)

av_collection = Query(AssetVersion).get_all(limit=5, projections=[Asset.name, "version"])

for i, collection in enumerate(av_collection):
    print(i, collection, collection.id)
# output:
# (0, EntityCollection[AssetVersion]{1}, [u'00001180-b7e7-43cf-b0e5-a2df0cefe669'])
# (1, EntityCollection[AssetVersion]{1}, [u'00001fd9-c8b8-4d84-8a8d-2c8fbbed46a0'])
# (2, EntityCollection[AssetVersion]{1}, [u'00004585-b77e-4638-89dc-33ea4dfe7f73'])
# (3, EntityCollection[AssetVersion]{1}, [u'0000482d-f10c-4d00-b2b3-aec57ec8510f'])
# (4, EntityCollection[AssetVersion]{1}, [u'00004a1a-fdd2-11ec-a538-005056a76761'])

# construct a list of strings that are combining the name of the AssetVersion's Asset and it's version number
print(
    av_collection.map(
        lambda avc: "{}_v{:03d}".format(avc.Asset.name[0], avc.version[0])
    )
)
# output: ['SomeAsset_v001', 'SomeAsset_v002', 'SomeCharacter_v004', 'SomeScene_v010', 'AnAssetClone_v002']

# group together AssetVersions by the name of its Asset
pprint(av_collection.group(lambda avc: avc.Asset.name[0]))
# output: 
# {u'SomeAsset': EntityCollection[AssetVersion]{2},
#  u'SomeCharacter': EntityCollection[AssetVersion]{1},
#  u'SomeScene': EntityCollection[AssetVersion]{1},
#  u'AnAssetClone': EntityCollection[AssetVersion]{1}}

# group together AssetVersions by the name of its Asset and 
# associate all of its version numbers with it
pprint(
    av_collection.group_and_map(lambda avc: avc.Asset.name[0], lambda avc: avc.version)
)
# output:
# {u'SomeAsset': [1, 2],
#  u'SomeCharacter': [4],
#  u'SomeScene': [10],
#  u'AnAssetClone': [2]}

# get a tuple with two items
# the first representing a true matching condition and 
# the second the false matching condition
print(av_collection.partition(lambda avc: avc.version[0] == 2))
# output: 
# (EntityCollection[AssetVersion]{2}, EntityCollection[AssetVersion]{3})
```

#### Set Operations

Due to the immutability of collections, it is not possible to directly add or remove entities. However, you can utilize the identical set operations available in Python's `set` class to obtain new collections.
```python
from trackteroid import (
    Query,
    AssetVersion
)

collection_a = Query(AssetVersion).get(limit=3)
collection_b = Query(AssetVersion).get(limit=3, offset=1)

print(f"a = {collection_a.version}")
# output: 'a = [2, 10, 2]'
print(f"b = {collection_b.version}")
# output: 'b = [10, 2, 9])'

# union
print(f"a + b = {collection_a.union(collection_b).version}")
# output: 'a + b = [2, 10, 2, 9]'

# difference
print(f"a - b = {collection_a.difference(collection_b).version}")
# output: 'a - b = [2]'
print(f"b - a = ", collection_b.difference(collection_a).version)
# output: 'b - a = [9]'

# symmetric difference
print(f"(a - b) + (b - a) = {collection_a.symmetric_difference(collection_b).version}")
# output: '(a - b) + (b - a) = [2, 9]'

# intersection
print(f"(a + b) - ((a - b) + (b - a)) = {collection_a.intersection(collection_b).version}")
# output: '(a + b) - ((a - b) + (b - a)) = [10, 2]'
```

#### Fetching Attributes

As Trackteroid's default Sessions disable the _autopolulate_ feature, it is possible to work with unprojected data. In such cases, you may need to fetch missing attributes when required. This can be accomplished using the `fetch_attributes` method on your collection.
```python
from trackteroid import (
    Asset,
    Query,
    Task
)

# assuming you receive a collection from somewhere
some_asset_collection = Query(Asset).by_name(Task, "%").get_all(limit=10)
print(some_asset_collection)
# output: EntityCollection[Asset]{10}

print(
    some_asset_collection.
    fetch_attributes(Task.State.name, "versions").
    filter(
        lambda a: a.versions and a.Task.State.name[0] == "Blocked"
    )
    .Task.State.name
)
# output: ['Blocked']
```


#### Fallback Concept

## Authoring

### CRUD (Create, Read, Update, Delete)



