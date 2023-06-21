To retrieve data from the Ftrack server, you need to perform queries using the `Query` class. This class serves as the entry point for accessing data and should be initialized with the desired entity type: `Query(<Entity Type>)`.

In the previous example, we wanted to retrieve any `AssetVersion` but only fetched the first result from the server. Any `get_` prefixed method on the `Query` instance we do refer to as **terminators**. 
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

```{include} query/examples.md
:start-after: example projections1 start
:end-before: example projections1 end
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
```{include} query/examples.md
:start-after: example projections shortcut start
:end-before: example projections shortcut end
```

This concise and intuitive approach simplifies querying and attribute retrieval for complex relationships.

#### Filtering

To ensure optimal performance and avoid fetching unnecessary data, it's recommended to narrow down the query results directly using Query criteria. Criteria methods in Trackteroid follow a `by_` and `not_by_` name prefix convention and can be chained together. While different entity types may have different criteria methods available, many share common ones.
By utilizing criteria methods, you can specify filtering conditions directly in the query construction process, reducing the amount of data retrieved. This approach helps improve code performance and efficiency.

```{include} query/examples.md
:start-after: example criteria1 start
:end-before: example criteria1 end
```

Moreover, the query mechanism allows for pattern-based filtering using the % placeholder, which denotes "zero or more of any character". This feature enhances the flexibility and sophistication of your filtering options within queries.
```{include} query/examples.md
:start-after: example criteria like start
:end-before: example criteria like end
```

Frequently, criteria in the query mechanism involve searching for direct properties of an entity, such as _id_, _name_, or _metadata_. By default, those criteria are associated with the entity type specified in the Query, representing the desired results. However, criteria can also offer the flexibility to define a target, allowing you to specify the entity type for which you want to reference its property instead.
```{include} query/examples.md
:start-after: example criteria target start
:end-before: example criteria target end
```

For criteria that support target specification, you have the option to provide exactly one target as the first positional argument. This target defines the relationship for the property used within the criterion.

### Limiting and Ordering

The `get_all` terminator supports limiting and ordering results.

```{include} query/examples.md
:start-after: example limiting start
:end-before: example limiting end
```