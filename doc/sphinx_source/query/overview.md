To retrieve data from the Ftrack server, you need to perform queries using the Query class. This class serves as the entry point for accessing data and should be initialized with the desired entity type: `Query(<Entity Type>)`.

In the previous example, we wanted to retrieve any `AssetVersion` but only fetched the first result from the server. Any `get_` method on the Query instance we do refer to as **terminators**. 
These terminators are responsible for executing the resolved query instruction, sending it to the Ftrack server, and fetching the corresponding data. 

The result is returned as a collection, specifically an instance of either EntityCollection or EmptyCollection, depending on the outcome. When printed, the collection is represented as:

`EntityCollection[<Entity Type>]{<Number of Results>}` or `EmptyCollection[<Entity Type>]`

If you wish to preview the resolved query without sending it to the server, you can simply print the collection or call str on it.

```python
print(Query(AssetVersion))
# output: select id, asset.name, version from AssetVersion
```

#### Projections

When accessing data from the resulting collection, it is important to _project_ (specify) the attributes that you will need to access later. 
A resolved query typically takes the form:

```sql
select <projections> from <entity type> where <criteria>
```

Looking back at the previous example, you can observe that the attributes _id_, _asset.name_, and _version_ were included in the resolved query instruction. 
This was done because these attributes are commonly accessed and can be predefined for certain entity types.

By projecting the necessary attributes in the query, you ensure that the resulting collection includes the specific data you require.

```python
print(AssetVersion.projections)
# output: ['id', 'asset.name', 'version']
```
In contrast to the Ftrack Python API, the default Session within Trackteroid disables the auto-population feature. This means that the Session will not automatically fetch missing data when accessing attributes on your collections. Instead, the data is fetched only for the attributes that were explicitly projected in the query.
This behavior provides a more controlled and optimized approach to data retrieval. By avoiding unnecessary data fetching, disabled auto-population minimizes network requests and might improve performance significantly. 

When working with Trackteroid, it is important to be aware of this behavior and ensure that you project all the attributes you need in your queries. 

```python
print(Query(AssetVersion).get_first().id)
# output: [u'00001180-b7e7-43cf-b0e5-a2df0cefe669']

print(Query(AssetVersion).get_first().comment)
# output: [Symbol(NOT_SET)]

print(Query(AssetVersion).get_first(projections=["comment"]).comment)
# output: [u'Hello World']
```
When attempting to access the comment attribute without projecting it, the output contains `Symbol(NOT_SET)`, indicating that the data for the comment attribute was not fetched.
However, by modifying the query to include the comment attribute in the projections list (projections=["comment"]) and accessing it, the output becomes [u'Hello World'], providing the retrieved value of the comment.

```python
print(
    Query(AssetVersion).get_first(
        projections=["comment", "asset.parent.project.name"]
    ).asset.parent.project.name
)
# output: [u'DummyProject']
```
Knowing these relationships and constructing written queries can be challenging, leading to long and complex queries. However, Trackteroid provides a shorter and easier alternative for many relationships
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

This concise and intuitive approach simplifies querying and attribute retrieval for complex relationships.

#### Filtering

To ensure optimal performance and avoid fetching unnecessary data, it's recommended to narrow down the query results directly using Query criteria. Criteria methods in Trackteroid follow a `by_` and `not_by_` name prefix convention and can be chained together. While different entity types may have different criteria methods available, many share common ones.
By utilizing criteria methods, you can specify filtering conditions directly in the query construction process, reducing the amount of data retrieved. This approach helps improve code performance and efficiency.

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

# get all AssetVersions with version number 1 or 2 of an Asset called 'SomeAsset'
print(Query(AssetVersion).by_name("SomeAsset").by_version(1, 2)).get_all()
# output: EntityCollection[AssetVersion]{2}

# get all AssetVersions with version number 1 or 2 of any Asset that is NOT called 'SomeAsset'
print(Query(AssetVersion).not_by_name("SomeAsset").by_version(1, 2)).get_all()
# output: EntityCollection[AssetVersion]{10}
```

Moreover, the query mechanism allows for pattern-based filtering using the % placeholder, which denotes "zero or more of any character". This feature enhances the flexibility and sophistication of your filtering options within queries.
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

Frequently, criteria in the query mechanism involve searching for direct properties of an entity, such as _id_, _name_, or _metadata_. By default, those criteria are associated with the entity type specified in the Query, representing the desired results. However, criteria can also offer the flexibility to define a target, allowing you to specify the entity type for which you want to reference its property instead.
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

For criteria that support target specification, you have the option to provide exactly one target as the first positional argument. This target defines the relationship for the property used within the criterion.

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