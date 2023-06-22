# Quickstart

Eager to get started? This page give some introduction to the core concepts of Trackteroid. 
Follow [Installation](installation.md) and install Trackteroid first. Ideally you should also have a basic understanding of the [Ftrack Python API](https://ftrack-python-api.readthedocs.io/en/stable/index.html).

The following examples assumes you have [configured the api access for Ftrack](https://ftrack-python-api.readthedocs.io/en/stable/understanding_sessions.html) accordingly.

## Accessing Data From FTrack

```{include} query/examples.md
:start-after: example minimal start
:end-before: example minimal end

```

### The Query

```{include} query/overview.md
```
### Defining Relationships

One of the main objectives of Trackteroid is to minimize the need for in-depth knowledge of the underlying database structure when working with queries and resulting collections. This goal is accomplished through two distinct approaches.

Firstly, it automatically derives relationships whenever possible by dynamically inspecting the schema of the current session. This capability allows for seamless handling of relationships without requiring explicit configuration.

However, Ftrack's dynamic nature means that certain entity types may require configuring relationships to align with specific requirements. Trackteroid provides the flexibility to describe and represent contextual relationships for such cases, enabling customization and adaptation to meet individual needs by implementing a [resolver](configuration.md#relationships-resolver).

All communication with an Ftrack server is facilitated through a `Session` object. By default, a Query is constructed using the _SESSION_ singleton and the _default_ schema. Here's an example:

```{include} query/examples.md
:start-after: example session start
:end-before: example session end
```

However, you also have the flexibility to initialize your own `Session` object and provide a different schema. Here's an example:

```python
from trackteroid import (
    AssetVersion,
    Query,
    SCHEMA
)
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

```{include} collections/examples.md
:start-after: example practice start
:end-before: example practice end
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


#### Item and Attribute Access

Retrieving items from a collection is straightforward and effortless. 
These examples illustrate the versatility of the item getter on an EntityCollection.
```{include} collections/examples.md
:start-after: example item access1 start
:end-before: example item access1 end
```

Accessing related collections and primitive data is user-friendly. 
This example demonstrates the seamless navigation through nested collections and the retrieval of primitive data stored in the _resource_identifier_ attribute of associated _component_locations_.

```{include} collections/examples.md
:start-after: example attribute access1 start
:end-before: example attribute access1 end
```

You can conveniently access individual attributes within the custom_attributes field by utilizing the `custom_` prefix as a shortcut. This allows direct access to specific attributes without the need to explicitly refer to the _custom_attributes_ field and retrieve values by their corresponding keys.
```{include} collections/examples.md
:start-after: example custom attribute access start
:end-before: example custom attribute access end
```

#### Transformation Methods

While iterating through loops is a valid approach, leveraging transformations can provide enhanced convenience. 
The EntityCollection class provides higher-order methods that accept functions as arguments, aligning with the principles of functional programming. 
The presented example highlights a subset of the transformation methods available.

```{include} collections/examples.md
:start-after: example transformation methods overview start
:end-before: example transformation methods overview end
```

#### Set Operations

Due to the immutability of collections, it is not possible to directly add or remove entities. However, you can utilize the identical set operations available in Python's `set` class to obtain new collections.
```{include} collections/examples.md
:start-after: example set operations overview start
:end-before: example set operations overview end
```

#### Fetching Attributes

As Trackteroid's default Sessions disable the _autopolulate_ feature, it is possible to work with unprojected data. In such cases, you may need to fetch missing attributes when required. This can be accomplished using the `fetch_attributes` method on your collection.
```{include} collections/examples.md
:start-after: example fetch attributes1 start
:end-before: example fetch attributes1 end
```

#### Fallback Concept

```{include} collections/emptycollection.md
```

## Authoring

### CRUD (Create, Read, Update, Delete)

[Collections](collections.md) provide a user interface for performing CRUD operations, which include creating, reading, updating, and deleting data. 
The sections below are organized in a logical order to guide you through these operations.

#### Read

The listed page references will provide you will all the information when it comes to requesting and accessing data from Ftrack and how the data is being exposed on collections.

- [Querying](#the-query): Learn how to construct queries to retrieve specific data
- [Attribute Access](#item-and-attribute-access): Understand how to access attributes of items in collections.

#### Update

##### Setting Attributes

##### Linking 

#### Create

#### Delete

