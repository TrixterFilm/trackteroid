example minimal start
```python
from trackteroid import (
    Query,
    AssetVersion
)

version_collection = Query(AssetVersion).get_first()
print(version_collection)

# output: EntityCollection[AssetVersion]{1}
```
example minimal end

example projections1 start
```python
print(Query(AssetVersion).get_first().id)
# output: [u'00001180-b7e7-43cf-b0e5-a2df0cefe669']

print(Query(AssetVersion).get_first().comment)
# output: [Symbol(NOT_SET)]

print(Query(AssetVersion).get_first(projections=["comment"]).comment)
# output: [u'Hello World']
```
example projections1 end

example projections shortcut start
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
example projections shortcut end

example criteria1 start
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
example criteria1 end

example criteria like start
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
example criteria like end

example criteria target start
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
example criteria target end

example limiting start
```python
from trackteroid import (
    Query,
    AssetVersion
)

# get all AssetVersions ordered descending by their version number across all Assets
print(Query(AssetVersion).get_all(limit=8, order="descending", order_by="version").version)
# output: [55, 43, 42, 22, 10, 10, 8, 7]
```
example limiting end

example session start
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
example session end

example reuse query results start
```python
import logging
import sys

from trackteroid import (
    Query,
    AssetVersion,
    Project,
    SESSION
)

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


with SESSION.reusing_query_results():
    # will perform a query and logs:
    # INFO:trackteroid.query:Performing query: "select id, asset.name, version from AssetVersion"
    all_assetversions = Query(AssetVersion).get_all()

    # will not perform the query again - nothing will be logged
    all_assetversions_again = Query(AssetVersion).get_all()

    print(
        f"result contains same entities: {all_assetversions == all_assetversions_again}\n",
        f"result is same collection: {all_assetversions is all_assetversions_again}"

    )
    # output:
    # result contains same entities: True
    # result is same collection: True

    # as the resolved query will be different this will not be picked from the cache
    # although the result would contain the same entities as before
    # will perform a query and logs:
    # INFO:trackteroid.query:Performing query: "select id, asset.name, version from AssetVersion where (version like "%")"
    all_assetversions_once_more = Query(AssetVersion).by_version("%").get_all()
    print(
        f"result contains same entities: {all_assetversions == all_assetversions_once_more}\n",
        f"result is same collection: {all_assetversions is all_assetversions_once_more}"

    )
    # output:
    # result contains same entities: True
    # result is same collection: False

```
example reuse query results end