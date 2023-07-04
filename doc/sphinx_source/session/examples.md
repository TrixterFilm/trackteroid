example deferred operations1 start
```python
from trackteroid import (
    Query,
    SESSION,
    Asset,
    AssetVersion,
    Component,
    ComponentLocation
)

operations_file = "/tmp/recorded_operations.dbm"

with SESSION.deferred_operations(operations_file):
    asset_collection = Query(Asset).by_name("bc0040_comp").get_one(
        projections=[
            AssetVersion,
            AssetVersion.Task,
            Component,
            ComponentLocation.resource_identifier,
        ]
    )
    assetversion_collection = asset_collection.AssetVersion.create(
        task=asset_collection.AssetVersion.Task
    )
    component_collection = assetversion_collection.Component.create(
        name="main"
    )
    componentlocation_collection = component_collection.ComponentLocation.create(
        resource_identifier="/path/to/final/file"
    )
    assetversion_collection.is_published = True
```
example deferred operations1 end

example deferred operations2 start
```python
from trackteroid import SESSION

operations_file = "/tmp/recorded_operations.dbm"
SESSION.reconnect_and_commit(operations_file)
```
example deferred operations2 end

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