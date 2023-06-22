example practice start
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
example practice end

example item access1 start
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
example item access1 end

example attribute access1 start
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
example attribute access1 end

example custom attribute access start
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
example custom attribute access end

example transformation methods overview start
```python
from pprint import pprint

from trackteroid import (
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
example transformation methods overview end

example set operations overview start
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
example set operations overview end

example fetch attributes1 start
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
example fetch attributes1 end

example fallback1 start
```python
from trackteroid import (
    Asset,
    Query
)

asset_collection = Query(Asset).by_name("DOESNT_EXIST").get_all()
print(asset_collection)
# output: EmptyCollection[Asset]

print(not asset_collection)
# output: True

print(asset_collection or "Oh vey... no results found.")
# output: Oh vey... no results found.
```
example fallback1 end

example fallback2 start
```python
from trackteroid import (
    Asset,
    Query
)

print(
    # The Query result could already be empty.
    # This is more likely when using criteria to filter results when querying.
    Query(Asset).get_first(
        projections=[
            "versions.is_published",
            "versions.user.username"
        ]
    ).
    # An asset could have no versions or at least no versions that have been marked as `is_published`.
    versions.filter(
        lambda avc: avc.is_published[0]
    ).
    user.username
    # Finally, we retrieve the username of the user associated with the filtered versions.
    # If at any point we encounter no results, we can gracefully handle it by providing an empty list as a fallback.
    or []
)
```
example fallback2 end