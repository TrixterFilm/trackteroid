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

example apply1 start
```python
from trackteroid import (
    Query,
    AssetVersion,
    Status,
    Task
)
assetversion_collection = Query(AssetVersion).get_all(
    limit=5,
    projections=[Task, Task.Status, Task.Status.name]
)
print(
    assetversion_collection.Task,
    assetversion_collection.Task.Status.name
)
# output: EntityCollection[Task]{5} ['Done', 'Internal Approved', 'Not Started', 'Tweak', 'Final']

status_collection = Query(Status).by_name("In Progress").get_first(projections=["name"])
print(status_collection.name)
# output: ['In Progress']

assetversion_collection.Task.Status.apply(lambda avc: status_collection)
print(
    assetversion_collection.Task,
    assetversion_collection.Task.Status.name
)
# output: EntityCollection[Task]{5} ['In Progress']
```
example apply1 end

example apply2 start
```python
from trackteroid import (
    Query,
    AssetVersion
)
assetversion_collection = Query(AssetVersion).get_all(
    limit=1, 
    projections=["comment"]
)
print(assetversion_collection.comment)
# output: ['submit version for review']

assetversion_collection.apply(lambda avc: avc.comment[0] + " (edited)", attribute_name="comment")
print(assetversion_collection.comment)
# output: ['submit version for review (edited)']
```
example apply2 end

example count1 start
```python
from trackteroid import (
    Query,
    Asset
)

asset_collection = Query(Asset).by_name("%character%", "%environment%").get_all(
    limit=100,
    projections=["name"]
)
print(asset_collection)
# output: EntityCollection[Asset]{100}

print(
    asset_collection.count(lambda ac: "character" in ac.name[0]),
    asset_collection.count(lambda ac: "environment" in ac.name[0]),
)
# output: 65 18
```
example count1 end

example filter1 start
```python
from trackteroid import (
    Query,
    Asset
)
asset_collection = Query(Asset).get_all(
    limit=100,
    projections=["name"]
)
print(asset_collection)
# output: EntityCollection[Asset]{100}

prop_asset_collection = asset_collection.filter(lambda ac: "prop" in ac.name[0])
print(prop_asset_collection)
# output: EntityCollection[Asset]{1}
```
example filter1 end

example filter2 start
```python
from trackteroid import (
    Query,
    Asset,
    AssetVersion
)
asset_collection = Query(Asset).get_all(
    limit=100,
    projections=[AssetVersion]
)
print(asset_collection)
# output: EntityCollection[Asset]{100}

frequent_asset_collection = asset_collection.filter(lambda ac: len(ac.AssetVersion) >= 10)
print(frequent_asset_collection)
# output: EntityCollection[Asset]{11}
```
example filter2 end

example fold1 start
```python
from trackteroid import (
    Query,
    Asset,
    Component
)

asset_collection = Query(Asset).get_first(
    projections=[
        Component,
        Component.size
    ]
)

print(asset_collection.Component.size)
# output: [1572543, 1940586, 4921736, ...]

print(
    "Asset's components total size: {:.2f} MB".format(
        asset_collection.Component.fold(
            0, lambda current, cc: current + cc.size[0]
        ) / 1024**2
    )
)
# output: Asset's components total size: 77.43 MB
```
example fold1 end

example group1 start
```python
from pprint import pprint

from trackteroid import (
    Query,
    AssetVersion,
    Asset
)

pprint(
    Query(AssetVersion).get_all(
        limit=10,
        projections=[Asset.name]
    ).group(lambda avc: avc.Asset.name[0])
)
# output:
# {'Animation': EntityCollection[AssetVersion]{3},
#  'bc0040_comp': EntityCollection[AssetVersion]{1},
#  'classic_console_01': EntityCollection[AssetVersion]{1},
#  'classic_nightstand_01': EntityCollection[AssetVersion]{1},
#  'coffee_table_01': EntityCollection[AssetVersion]{1},
#  'gothic_bed_01': EntityCollection[AssetVersion]{1},
#  'gothic_console_01': EntityCollection[AssetVersion]{1},
#  'wooden_table_03': EntityCollection[AssetVersion]{1}}

```
example group1 end

example group2 start
```python
from pprint import pprint

from trackteroid import (
    Query,
    AssetVersion,
    State
)

pprint(
    Query(AssetVersion).get_all(
        limit=10,
        projections=[State.name]
    ).group(lambda avc: avc.State.name[0])
)
# output:
# {'Done': EntityCollection[AssetVersion]{1},
#  'In Progress': EntityCollection[AssetVersion]{9}}
```
example group2 end

example group_and_map1 start
```python
from pprint import pprint

from trackteroid import (
    Query,
    AssetVersion,
    Note,
    Status
)

pprint(
    Query(AssetVersion).by_publisher(
        "leandra.rosa@example.com"
    ).get_all(
        limit=10,
        projections=[
            Status.name,
            Note.content,
            "version"
        ]
    ).group_and_map(
        lambda avc: f"{avc.Asset.name[0]}_v{str(avc.version[0]).zfill(3)}",
        lambda avc: f"{avc.Status.name[0]} - {avc.Note.content[0] or 'No notes provided yet.'}"
    )
)
# output:
# {'Animation_v001': 'Revise - I think we will still have him approach sooner. '
#                    'revised expression.',
#  'Animation_v002': "Revise - Isn't his left eyebrow too low? 2: I think we can "
#                    'improve his expression at the end of the shot. Make the '
#                    'expression a little more asymmetrical.',
#  'Animation_v003': 'Approved - Good job, Approved!',
#  'bc0040_layout_v001': 'Revise - Is this the approved camera? Seems way too '
#                        'wide. Scale is off as well',
#  'bc0040_layout_v002': 'Approved - Approved'}
```
example group_and_map1 end

example group_and_map2 start
```python
from trackteroid import (
    Query,
    ObjectType,
    Project,
    TypedContext,
)

typedcontext_collection = Query(TypedContext).by_name(Project, "showroom").get_all(
    projections=[ObjectType.name]
)
grouped_by_type = typedcontext_collection.group(
    lambda tcc: tcc.ObjectType.name[0],
)

print(
    f"All existing object types in this context: "
    f"{', '.join(grouped_by_type.keys())}."
)
```
example group_and_map2 end

example map1 start
```python
from trackteroid import (
    Query,
    Asset,
    AssetVersion
)

print(
    Query(AssetVersion).get_all(
        limit=2,
        projections=[Asset.name, "version"]
    ).map(lambda avc: f"{avc.Asset.name[0]}:v{str(avc.version[0]).zfill(3)}")
)
# output: ['bc0040_comp:v003', 'classic_console_01:v001']
```
example map1 end

example max1 start
```python
from trackteroid import (
    Query,
    AssetVersion
)

assetversion_collection = Query(AssetVersion).by_name("bc0050_comp").get_all(projections=["version"])
max_version_collection = assetversion_collection.max(lambda avc: avc.version)
print(
    assetversion_collection.version,
    max_version_collection,
    max_version_collection.version
)
# output: [1, 2, 3] EntityCollection[AssetVersion]{1} [3]
```
example max1 end

example max2 start
```python
from trackteroid import (
    Query,
    Asset,
    AssetVersion
)

asset_collection = Query(Asset).\
    by_name("bc0050_comp", "classic_console_01").\
    get_all(
    projections=[
        AssetVersion,
        AssetVersion.version
    ]
)
print(asset_collection.max(lambda ac: ac.AssetVersion.version).name)
# ['classic_console_01']
```
example max2 end

example min1 start
```python
from trackteroid import (
    Query,
    AssetVersion
)

assetversion_collection = Query(AssetVersion).by_name("bc0050_comp").get_all(projections=["version"])
max_version_collection = assetversion_collection.min(lambda avc: avc.version)
print(
    assetversion_collection.version,
    max_version_collection,
    max_version_collection.version
)
# output: [1, 2, 3] EntityCollection[AssetVersion]{1} [1]
```
example min1 end

example min2 start
```python
from trackteroid import (
    Query,
    Asset,
    AssetVersion
)

asset_collection = Query(Asset).\
    by_name("bc0050_comp", "classic_console_01").\
    get_all(
    projections=[
        AssetVersion,
        AssetVersion.version
    ]
)
print(asset_collection.min(lambda ac: ac.AssetVersion.version).name)
# ['bc0050_comp']
```
example min2 end

example partition1 start
```python
from trackteroid import (
    Query,
    AssetVersion,
    State
)

print(
    Query(AssetVersion).get_all(limit=100, projections=[State.name]).\
    partition(lambda avc: avc.State.name[0] == "Done")
)
# (EntityCollection[AssetVersion]{11}, EntityCollection[AssetVersion]{89})
```
example partition1 end

example sort1 start
```python
from trackteroid import (
    Query,
    AssetVersion
)

asset_version_collection = Query(AssetVersion).get_all(limit=10, projections=["version"])

print(
    f"{asset_version_collection.version}\n"
    f"{asset_version_collection.sort(lambda avc: avc.version).version}\n"
    f"{asset_version_collection.sort(lambda avc: avc.version, reverse=True).version}"
)
# output:
# [3, 1, 1, 2, 3, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1, 2, 3, 3]
# [3, 3, 2, 1, 1, 1, 1, 1, 1, 1]
```
example sort1 end

example sort2 start
```python
from trackteroid import (
    Query,
    AssetVersion,
    Asset
)

asset_version_collection = Query(AssetVersion).get_all(limit=5, projections=[Asset.name, "version"])
asset_version_collection_sorted = asset_version_collection.sort(lambda avc: avc.Asset.name)


print(
    list(
        zip(
            asset_version_collection.fold([], lambda x, y: x + y.asset.name),
            asset_version_collection.version
        )
    )
)
print(
    list(
        zip(
            asset_version_collection_sorted.fold([], lambda x, y: x + y.asset.name),
            asset_version_collection_sorted.version
        )
    )
)
# output:
# [('bc0040_comp', 3), ('classic_console_01', 1), ('classic_nightstand_01', 1), ('Animation', 2), ('Animation', 3)]
# [('Animation', 2), ('Animation', 3), ('bc0040_comp', 3), ('classic_console_01', 1), ('classic_nightstand_01', 1)]
```
example sort2 end

example union1 start
```python
from trackteroid import (
    Query,
    AssetVersion
)

collection_a = Query(AssetVersion).get(limit=3)
collection_b = Query(AssetVersion).get(limit=3, offset=1)
collection_c = Query(AssetVersion).get(limit=3, offset=2)

print(f"a = {collection_a.version}")
# output: 'a = [3, 6, 7]'
print(f"b = {collection_b.version}")
# output: 'b = [6, 7, 19]'
print(f"c = {collection_c.version}")
# output: 'c = [7, 19, 12]'

# union
print(f"a + b = {collection_a.union(collection_b).version}")
# output: 'a + b = [3, 6, 7, 19]'
print(f"a + b + c = {collection_a.union(collection_b, collection_c).version}")
# output: 'a + b + c = [3, 6, 7, 19, 12]'
```
example union1 end

example difference1 start
```python
from trackteroid import (
    Query,
    AssetVersion
)

collection_a = Query(AssetVersion).get(limit=3)
collection_b = Query(AssetVersion).get(limit=3, offset=1)
collection_c = Query(AssetVersion).get(limit=3, offset=2)

print(f"a = {collection_a.version}")
# output: 'a = [3, 6, 7]'
print(f"b = {collection_b.version}")
# output: 'b = [6, 7, 19]'
print(f"c = {collection_c.version}")
# output: 'c = [7, 19, 12]'

# difference
print(f"a - b = {collection_a.difference(collection_b).version}")
# output: 'a - b = [3]'
print(f"b - a = ", collection_b.difference(collection_a).version)
# output: 'b - a =  [19]'
print(f"c - b - a = ", collection_c.difference(collection_a, collection_b).version)
# output: 'c - b - a =  [12]'
print(f"b - c - a = ", collection_b.difference(collection_c, collection_a).version)
# output: 'b - c - a =  EmptyCollection[AssetVersion]'
```
example difference1 end

example symmetric difference1 start
```python
from trackteroid import (
    Query,
    AssetVersion
)

collection_a = Query(AssetVersion).get(limit=3)
collection_b = Query(AssetVersion).get(limit=3, offset=1)

print(f"a = {collection_a.version}")
# output: 'a = [3, 6, 7]'
print(f"b = {collection_b.version}")
# output: 'b = [6, 7, 19]'

# symmetric_difference
print(f"(a - b) + (b - a) = {collection_a.symmetric_difference(collection_b).version}")
# output: '(a - b) + (b - a) = [3, 19]'
```
example symmetric difference1 end

example intersection1 start
```python
from trackteroid import (
    Query,
    AssetVersion
)

collection_a = Query(AssetVersion).get(limit=3)
collection_b = Query(AssetVersion).get(limit=3, offset=1)

print(f"a = {collection_a.version}")
# output: 'a = [3, 6, 7]'
print(f"b = {collection_b.version}")
# output: 'b = [6, 7, 19]'

# intersection
print(f"(a + b) - ((a - b) + (b - a)) = {collection_a.intersection(collection_b).version}")
# output: '(a + b) - ((a - b) + (b - a)) = [6, 7]'
```
example intersection1 end

example setattr1 start
```python
from trackteroid import (
    Query,
    AssetVersion,
    ComponentLocation,
    SESSION
)

collection = Query(AssetVersion).get_all(limit=1, projections=[ComponentLocation.resource_identifier])

print(collection.ComponentLocation.resource_identifier)
# output:
# ['729e05c2-2722-4cc2-97d0-37b4522671d1', 'e26d1b56-c72b-4b9d-8177-6faf47992375', 'ec2203a2-8b5f-11eb-80be-c2ffbce28b68']

collection.ComponentLocation[0].resource_identifier = "new value"
print(collection.ComponentLocation.resource_identifier)
# output:
# ['new value', 'e26d1b56-c72b-4b9d-8177-6faf47992375', 'ec2203a2-8b5f-11eb-80be-c2ffbce28b68']

collection.ComponentLocation.resource_identifier = ["newer value"] * len(collection.ComponentLocation)
print(collection.ComponentLocation.resource_identifier)
# output:
# ['newer value', 'newer value', 'newer value']

# changes are only present in the sessions recorded operation
# in order to send the updates to the Ftrack server you have to commit
collection.commit()

# prove that we updated the Ftrack database accordingly by reconnecting our session instance
SESSION.reconnect()

print(
    Query(AssetVersion).get_all(limit=1, projections=[ComponentLocation.resource_identifier]).
    ComponentLocation.resource_identifier
)
# output: ['newer value', 'newer value', 'newer value']
```
example setattr1 end

example linking1 start
```python
from trackteroid import (
    Query,
    AssetBuild,
    SESSION
)

assetbuild_collection = Query(AssetBuild).get_all(
    limit=3,
    projections=[
        "name",
        "incoming_links.from",
        "incoming_links.from.name",
        "outgoing_links.to"]
)
another_assetbuild_collection = Query(AssetBuild).get_all(
    limit=1,
    offset=3,
    projections=["name"]
)

print(
    f"assetbuilds: {assetbuild_collection.name}\n"
    f"another assetbuild: {another_assetbuild_collection.name}\n"
    f"incoming: {getattr(assetbuild_collection[1].incoming_links, 'from').name or 'nothing linked as input yet'}\n"
    f"outgoing: {getattr(assetbuild_collection[1].outgoing_links, 'to').name or 'nothing linked as output yet'}\n"
)
# output:
# assetbuilds: ['Small Round Wooden Table 01', 'Side Table Tall 01', 'Steel Frame Shelves 02']
# another assetbuild: ['Steel Frame Shelves 01']
# incoming: nothing linked as input yet
# outgoing: nothing linked as output yet

# create links with proper assignment and commit changes to database
assetbuild_collection[1].\
    link_inputs(assetbuild_collection[0]).\
    link_outputs(assetbuild_collection[2]).\
    commit()

SESSION.reconnect()

assetbuild_collection = Query(AssetBuild).get_all(
    limit=3,
    projections=[
        "name",
        "incoming_links.from",
        "incoming_links.from.name",
        "outgoing_links.to"
    ]
)
# verify our changes arrived properly in the database
print(
    f"incoming: {getattr(assetbuild_collection[1].incoming_links, 'from').name or 'nothing linked as input yet'}\n"
    f"outgoing: {getattr(assetbuild_collection[1].outgoing_links, 'to').name or 'nothing linked as output yet'}\n"
)
# # output:
# incoming: ['Small Round Wooden Table 01']
# outgoing: ['Steel Frame Shelves 02']

# extend links
assetbuild_collection[1].link_inputs(another_assetbuild_collection).commit()

SESSION.reconnect()

assetbuild_collection = Query(AssetBuild).get_all(
    limit=3,
    projections=[
        "name",
        "incoming_links.from",
        "incoming_links.from.name",
        "outgoing_links.to"
    ]
)

# verify our changes arrived properly in the database
print(
    f"incoming: {getattr(assetbuild_collection[1].incoming_links, 'from').name or 'nothing linked as input yet'}\n"
)
# output:
# incoming: ['Small Round Wooden Table 01', 'Steel Frame Shelves 01']
```
example linking1 end

example note creation1 start
```python
from trackteroid import (
    Query,
    AssetVersion,
    Note,
    NoteCategory,
    User
)

user = Query(User).by_name("aniela.morin@example.com").get_all(projections=["username"])
category = Query(NoteCategory).by_name("Internal").get_all(projections=["name"])

assetversion = Query(AssetVersion).by_id("6a229598-6596-11ed-a73a-92ba0fc0dc3d").get_one(
    projections=[Note, Note.content, Note.NoteCategory.name]
)

print(
    assetversion.Note.group_and_map(
        lambda note: note.NoteCategory.name[0],
        lambda note: note.content
    )
)
# output:
# {'Client feedback': ['The direction looks good!']}

new_note = assetversion.Note.create(
    author=user,
    content="Thanks!",
    is_todo=False,
    category=category
)
assetversion.Note = assetversion.Note.union(new_note)
print(
    assetversion.Note.group_and_map(
        lambda note: note.NoteCategory.name[0],
        lambda note: note.content
    )
)
# output:
# {'Client feedback': ['The direction looks good!'], 'Internal': ['Thanks!']}

assetversion.commit()
```
example note creation1 end


example type coercion1 start
```python
from trackteroid import (
    Query,
    Folder,
    Shot,
    TypedContext
)

folder_collection = Query(Folder).get_all()
shot_collection = Query(Shot).get_all()

print(folder_collection, shot_collection)
# output:
# EntityCollection[Folder]{6} EntityCollection[Shot]{10}

print(
    TypedContext(folder_collection),
    TypedContext(shot_collection)
)
# output:
# EntityCollection[TypedContext]{6} EntityCollection[TypedContext]{10}

# can be used with set operations now
typedcontext_collection = TypedContext(folder_collection).union(TypedContext(shot_collection))
print(typedcontext_collection)
# output: EntityCollection[TypedContext]{16}

```
example type coercion1 end

example type filtering1 start
```python
from trackteroid import (
    Query,
    ObjectType,
    Project,
    TypedContext
)

typedcontext_collection = Query(TypedContext).get_all(projections=["parent"])
print(
    typedcontext_collection.parent,
    typedcontext_collection.parent[Project]
)
# output:
# EntityCollection[TypedContext]{39} EntityCollection[Project]{3}

# this only works for `TypeContext`, but not for `Project`
print(
    typedcontext_collection.
        parent.
        fetch_attributes(ObjectType.name).
        ObjectType.name
)
# output:
# ['Folder', 'Asset Build', 'Shot', 'Sequence']
```
example type filtering1 end

example type filtering2 start
```python
from trackteroid import (
    Query,
    AssetBuild,
    Folder,
    Project,
    TypedContext,
)

typedcontext_collection = Query(TypedContext).by_name(Project, "showroom").get_all()

print(
    typedcontext_collection[Folder],
    typedcontext_collection[AssetBuild]
)
# EntityCollection[Folder]{4} EntityCollection[AssetBuild]{17}
```
example type filtering2 end

example delete start
```python
from trackteroid import (
    Query,
    AssetVersion,
    SESSION
)

_id = "405c569e-8bfa-11eb-ae63-c2ffbce28b68"

Query(AssetVersion).by_id(_id).get_one().delete().commit()

SESSION.reconnect()

# will result in error as the entity doesn't exist anymore
# ftrack_api.exception.NoResultFoundError: 
# No result found for 'select id, asset.name, version from AssetVersion where (id is "405c569e-8bfa-11eb-ae63-c2ffbce28b68")'
#
Query(AssetVersion).by_id(_id).get_one()
```
example delete end