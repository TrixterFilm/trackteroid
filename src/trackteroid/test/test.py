import sys
from pprint import pprint

from trackteroid import (
    Query
)
from trackteroid.entities import *

def uprint(*msg):
    print(" ".join([str(_) for _ in msg]))
    sys.stdout.flush()

def upprint(msg):
    pprint(msg)
    sys.stdout.flush()

def SEPARATOR______________(message="", separator="#"):
    _ = "\n" + "{}".format(separator)*30 + "\n"
    if message:
        _ = _[:15] + " {} ".format(message) + _[15:]
    print(_)

#print(Query(AssetVersion).get_all(limit=10, projections=[Sequence.name, ComponentLocation.resource_identifier]).ComponentLocation.resource_identifier)

assetversions1 = Query(AssetVersion).get(limit=10, order_by="id")
assetversions2 = Query(AssetVersion).get(limit=8, order_by="id")
assets = Query(Asset).get(limit=3)
project = Query(Project).by_name("Sy%").get_first()

### EntityCollection (an Ordered Immutable Set i.e. not changeable and only contains unique elements)

## string representation
SEPARATOR______________("String Representation")
uprint(assetversions1)
uprint(assetversions2)
uprint(assets)

SEPARATOR______________("Equality vs Identity")
## equality vs identity
# equality based on ftrack entity ids
uprint(assetversions1 == assetversions1[:])
uprint(assetversions1 != assetversions2)

uprint(assetversions1 is assetversions1[:])
uprint(id(assetversions1) == id(assetversions2))

SEPARATOR______________("Contains")
# contains
uprint(assetversions1 in assetversions1)
uprint(assetversions2 in assetversions1)
uprint(assetversions1 in assetversions2)
uprint(assetversions1.id[0] in assetversions1)
uprint(assetversions1[0] in assetversions1)

SEPARATOR______________("Item Getters")
# item getter
uprint(assetversions1[0].id)
uprint(assetversions1[assetversions1.id[0]].id)

SEPARATOR______________("Attribute Getters")
# attribute getter

uprint(assets.name)
uprint(assetversions1.version)
assetversions1.fetch_attributes("version")
uprint(assetversions1.version)

assetversions1.fetch_attributes("asset.parent.parent.project.name")
uprint(assetversions1.asset.parent.parent.project.name)
upprint(Query(AssetVersion).by_metadata({"%":"%"}).get_first(projections=["metadata"]).metadata[0])

SEPARATOR______________("Relative Terminators")
# relative terminators
uprint(assetversions1.get(Project, projections=["full_name"]).full_name)
uprint(assetversions1.get(Asset).versions)
uprint(assetversions1.get(Asset, projections=["versions"]).versions)

SEPARATOR______________("Iteration")
# iteration
for idx, collection in enumerate(assetversions1):
    uprint(idx, collection, collection.id)
SEPARATOR______________(separator="-")
asset1, asset2, asset3 = assets
uprint(asset1, asset2, asset3)

for asset in asset1:
    uprint(asset.id)
    uprint(asset == asset1)
    uprint(asset is asset1)


# children (attribute getter on TypedContext)
SEPARATOR______________("Children")
uprint(project.children[Folder].children[Sequence].children[Shot].children[Task])

## Set operations (create a new collection by combining multiple collections)
SEPARATOR______________("Set Operations")
assets1 = Query(AssetVersion).get(limit=3)
assets2 = Query(AssetVersion).get(limit=3, offset=1)

uprint("a = ", assets1.version)
uprint("b = ", assets2.version)

# union
SEPARATOR______________("Union", separator="-")
uprint("a + b", assets1.union(assets2).version)

# difference
SEPARATOR______________("Difference", separator="-")
uprint("a - b", assets1.difference(assets2).version)
uprint("b - a", assets2.difference(assets1).version)

# symmetric_difference
SEPARATOR______________("Symmetric Difference", separator="-")
uprint("(a - b) + (b - a)", assets1.symmetric_difference(assets2).version)

# intersection
SEPARATOR______________("Intersection", separator="-")
uprint("(a + b) - ((a - b) + (b - a))", assets1.intersection(assets2).version)

## Transformation methods (create a new collection from a single input collection)
SEPARATOR______________("Transformation Methods")
# filter
SEPARATOR______________("Filter", separator="-")
uprint(assetversions1.version)
uprint(assetversions1.filter(lambda x: x.version[0] == 1).version)

SEPARATOR______________(separator="-")
uprint(assets.name)
assets.fetch_attributes("versions.task.status.name")
uprint(assets.filter(lambda x: "In Progress" in x.versions.task.status.name).name)

# partition
SEPARATOR______________("Partition", separator="-")
assetversions1.fetch_attributes("task.status.name")
approved, rejected = assetversions1.partition(lambda x: x.task.status.name[0] == "Internal Approved")
uprint(approved, rejected)

# group_by
SEPARATOR______________("Group By", separator="-")
assetversions2.fetch_attributes("status.name")
upprint(assetversions1.group(lambda x: x.asset.name[0]))
SEPARATOR______________("Partition", separator="-")
upprint(assetversions2.group(lambda x: x.status.name[0]))

# max_by, min_by
SEPARATOR______________("Max and Min By", separator="-")
uprint("All Versions", assetversions1.version)
uprint("Highest Version", assetversions1.max(lambda x: x.version).version)
uprint("Lowest Version", assetversions1.min(lambda x: x.version).version)

# sort_by
SEPARATOR______________("Sort By", separator="-")
uprint("Sorted by version", assetversions1.sort(lambda x: x.version).version)

sorted_by_name = assetversions1.sort(lambda x: x.asset.name)
uprint("Sorted by Assetname: ")
upprint(
    zip(
        sorted_by_name.fold([], lambda x, y: x + y.asset.name),
        sorted_by_name.version
    )
)

# fold
SEPARATOR______________("Fold", separator="-")
assets.fetch_attributes("versions.components.size")
filesize = assets[0].versions.components.fold(0, lambda x, y: x + y.size[0])
if filesize:
    uprint(filesize / 1024 / 1024, "MB")

SEPARATOR______________("Count", separator="-")
# count
uprint("Assets with 'comp' in name: ", assets.count(lambda x: "comp" in x.name[0]))

# map
SEPARATOR______________("Map", separator="-")
assetversions1.fetch_attributes("user.username")
uprint(assetversions1.map(lambda x: "{}_{}_v{:03d}".format(x.asset.name[0], x.user.username[0], x.version[0])))

# group_by_and_map
SEPARATOR______________("Group and Map", separator="-")
upprint(assetversions2.group_and_map(lambda x: x.status.name[0], lambda x: (x.user.username, x.version)))


SEPARATOR______________("Create Read Update Delete")
## CRUD
SEPARATOR______________("Create", separator="-")
# create
project = Query(Project).get_first()
demo_project = project.create(name="DemoProject", project_schema="Animation")
asset = demo_project.assets.create(name="BrennenderFurz", type="Geometry")
task = demo_project.children[Task].create(name="Modeling", type="Modeling")
avs = asset.versions.create(task=task)
component = avs.components.create(name="main")
location = component.component_locations.create(resource_identifier="/path/to/asset.abc")

project.commit()

# create_batch
SEPARATOR______________("Create in batch", separator="-")
sequences = demo_project.children[Sequence].create_batch(
    {"name": "Holy"},
    {"name": "Moly"},
    {"name": "AxelFoley"}
)

project.commit()

SEPARATOR______________("Update", separator="-")
# update
sequences.metadata = [
    {"furz1": "testen"},
    {"furz2": "testen"},
    {"furz3": "testen"}
]

project.commit()

# Linking
SEPARATOR______________("Linking", separator="-")
more_avs = asset.versions.create_batch(
    {"task": task,
     "version": 5
     },
    {"task": task,
     "version": 6
     }
)

avs.link_inputs(more_avs)

named_sequences = sequences.group(lambda x: x.name[0])

named_sequences["Holy"].link_outputs(named_sequences["Moly"])
named_sequences["AxelFoley"].link_inputs(named_sequences["Moly"])

project.commit()

#sequences.unlink_inputs(sequences)

project.commit()


# delete
SEPARATOR______________("Delete", separator="-")
Query(AssetVersion).by_name(Project, *demo_project.name).get_all().delete()
project.commit()
# Query(TypedContext).by_name(Project, *demo_project.name).get_all().delete()
#project.commit()

demo_project.delete()
project.commit()

### EmptyCollection
SEPARATOR______________("EmptyCollection")
# attribute forwarding to avoid errors (poor mans Optional)
# union, create + create_batch

empty_collection = Query(Asset).by_name("ThisDoesntExist123").get_first()
entity_collection = Query(Asset).get_first(projections=["versions.components.component_locations.resource_identifier"])

for collection in [empty_collection, entity_collection]:
    result = collection.versions.components.component_locations.resource_identifier
    if result:
        uprint("Result: ", result)
    else:
        uprint("NO Result", result)

    result = collection.versions.get(ComponentLocation).resource_identifier
    if result:
        uprint("Result: ", result)
    else:
        uprint("NO Result", result)

