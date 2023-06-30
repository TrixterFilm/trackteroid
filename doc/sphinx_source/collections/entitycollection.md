### Higher-Order Methods

The EntityCollection class provides higher-order methods that accept functions as arguments, aligning with the principles of functional programming.

#### apply

`apply(predicate, attribute_name=None)` applies a given predicate function to each element in the collection and assigns the generated value to the specified attribute. 
If no attribute name is provided, the value is directly assigned to the calling collection.

**Example 1:** Override status of all tasks associated to an AssetVersion collection.
```{include} collections/examples.md
:start-after: example apply1 start
:end-before: example apply1 end
```

**Example 1:** Extend the comment field of items within an AssetVersion collection.
```{include} collections/examples.md
:start-after: example apply2 start
:end-before: example apply2 end
```

#### count

`count(predicate)` returns the number of elements for which a given predicate function returns `True`.

**Example 1:** Count the occurrences of assets that contain "character" and "environment".
```{include} collections/examples.md
:start-after: example count1 start
:end-before: example count1 end
```

#### filter

`filter(predicate)` is used to selectively filter a collection based on a given predicate function. 
The predicate function is applied to each element in the collection, and its return value, which is expected to be a boolean or coercible to a boolean, determines whether the element is included in the resulting collection. Elements for which the predicate returns `True` are added to the filtered collection, while those for which it returns `False` are excluded.

**Example 1:** Generate a new collection that only contains elements with "prop" in the name.
```{include} collections/examples.md
:start-after: example filter1 start
:end-before: example filter1 end
```

**Example 2:** Generate a new collection that only contains the assets which have 10 or more versions associated.
```{include} collections/examples.md
:start-after: example filter2 start
:end-before: example filter2 end
```

#### fold

`fold(start_value, predicate)` accumulates the value starting with an initial value and applying an operation from the first to the last element in a collection.

**Example 1:** Determine the total filesize of all components for one Asset.
```{include} collections/examples.md
:start-after: example fold1 start
:end-before: example fold1 end
```

#### group

`group(predicate)` returns a dictionary with keys given by the predicate. All entities from the original collection will be mapped to their corresponding key.

**Example 1:** Group all AssetVersion collections via name of their asset.
```{include} collections/examples.md
:start-after: example group1 start
:end-before: example group1 end
```

**Example 2:** Group all AssetVersion collections via state name of their status.
```{include} collections/examples.md
:start-after: example group2 start
:end-before: example group2 end
```

#### group_and_map

`group_and_map(group_predicate, map_predicate)` runs a [group](#group) first and then runs the map predicate function on all the collections in the resulting dictionary values.

**Example1:** Provide a status -> last note overview for versions created by a given user.
```{include} collections/examples.md
:start-after: example group_and_map1 start
:end-before: example group_and_map1 end
```

#### map

`map(predicate)` generates a sequence of results by applying a given predicate function to each element in the collection. The predicate function is invoked for each element, and its return value is included in the generated sequence.

**Example1:** Generate a formatted representation of the AssetVersion combining the version number and the Asset name.
```{include} collections/examples.md
:start-after: example map1 start
:end-before: example map1 end
```

#### max

`max(predicate)` returns the first element yielding the largest value of the given function.

**Example1:** Get the AssetVersion collection with the largest version number for one asset.
```{include} collections/examples.md
:start-after: example max1 start
:end-before: example max1 end
```

**Example2:** Get the Asset collection that holds an AssetVersion with the largest version number.
```{include} collections/examples.md
:start-after: example max2 start
:end-before: example max2 end
```

```{attention}
The result of `max` will always be a single element collection even if multiple elements yield the same largest value. 
If multiple entities have the same max value, we follow Python's max implementation by returning the last occurence of this value. 
```

#### min

`min(predicate)` returns the first element yielding the smallest value of the given function.

**Example1:** Get the AssetVersion collection with the smallest version number for one asset.
```{include} collections/examples.md
:start-after: example min1 start
:end-before: example min1 end
```

**Example2:** Get the Asset collection that holds an AssetVersion with the smallest version number.
```{include} collections/examples.md
:start-after: example min2 start
:end-before: example min2 end
```

```{attention}
The result of `min` will always be a single element collection even if multiple elements yield the same smallest value. 
If multiple entities have the same min value, we follow Python's min implementation by returning the first occurence of this value. 
```

#### partition

`partition(predicate)` splits the collection into tuple of EntityCollections/EmptyCollections, where the first item contains a collection with elements for which the predicate returned `True`, while the second items contains a collection with elements for which the predicate returned `False`.

**Example1:** Split the AssetVersion collection based on a potential "Done" state of the elements.
```{include} collections/examples.md
:start-after: example partition1 start
:end-before: example partition1 end
```

#### sort

`sort(predicate)` returns a collection sorted by the given predicate.

**Example1:** Sort the AssetVersion collection based on version number of the individual elements.
```{include} collections/examples.md
:start-after: example sort1 start
:end-before: example sort1 end
```

**Example1:** Sort the AssetVersion collection based on the asset name of the individual elements.
```{include} collections/examples.md
:start-after: example sort2 start
:end-before: example sort2 end
```

### Set Operations

#### difference 

`difference(*collections)` computes the difference between two or more collections.

```{include} collections/examples.md
:start-after: example difference1 start
:end-before: example difference1 end
```

#### intersection

`intersection(*collections)` computes the intersection of two or more collections.

```{include} collections/examples.md
:start-after: example intersection1 start
:end-before: example intersection1 end
```

#### symmetric_difference

`symmetric_difference(*collections)` computes the [symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) between collections.

```{include} collections/examples.md
:start-after: example symmetric difference1 start
:end-before: example symmetric difference1 end
```

#### union

`union(*collections)` computes the union of two or more collections.

```{include} collections/examples.md
:start-after: example union1 start
:end-before: example union1 end
```

### Type Coercion

Certain entity types, such as `Component` and `TypedContext` subtypes, can be coerced to their respective base types. This allows for performing [set operations](#set-operations) between multiple types that inherit from the same base type. 
Additionally, when creating new entities, the type of the collection determines the type of entity that will be created.

To perform type coercion, you can use the constructor of the desired entity type.

```{include} collections/examples.md
:start-after: example type coercion1 start
:end-before: example type coercion1 end
```

```{attention}
In certain cases, attributes like _parent_, _ancestors_, _children_, _descendants_, and _components_ will undergo automatic type coercion, as these collections can contain entities of multiple types. 
```

`````{important}
Although `Project` is not a subtype of `TypedContext`, accessing the _parent_ or _ancestors_ attributes may include `Project` entities. 
The coercion performed on these attributes ensures that `Project` entities are considered, allowing for proper access and attribute fetching in a cohesive manner. 

````{admonition} See the following example that demonstrates it:
:class: dropdown

```{include} collections/examples.md
:start-after: example type filtering1 start
:end-before: example type filtering1 end
```
````
`````

### Type Filtering

Contrary to [type coercion](#type-coercion), filtering for subtypes is straightforward using the implemented item getter.

`````{tip}
````{admonition} Use the [group_and_map](#group-and-map) to identify exising types.
:class: dropdown

```{include} collections/examples.md
:start-after: example type filtering2 start
:end-before: example type filtering2 end
```
````
`````