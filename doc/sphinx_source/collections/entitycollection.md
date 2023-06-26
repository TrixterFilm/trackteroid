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

`group_and_map(group_predicate, map_predicate)` runs a [group](#group) first and then runs [map](#map) on all the collections in the resulting dictionary values.

**Example1:** Provide a status -> last note overview for versions created by a given user.
```{include} collections/examples.md
:start-after: example group_and_map1 start
:end-before: example group_and_map1 end
```

#### map

#### max

#### min

#### partition

#### sort


### Set Operations

