<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset=".graphics/svg/logo_white.svg" width=100>
        <img src=".graphics/svg/logo_black.svg" width=100>
    </picture>
</div>

# Trackteroid

[![Documentation Status][documentation-button]][documentation]
[![Python Versions][pyversion-button]][pypi]
[![Downloads][downloads-button]][downloads]
[![BSD License][bsdlicense-button]][bsdlicense]

[documentation]: https://trackteroid.readthedocs.io
[documentation-button]: https://readthedocs.org/projects/trackteroid/badge/?version=latest
[pyversion-button]: https://img.shields.io/pypi/pyversions/Trackteroid.svg
[pypi]: https://pypi.org/project/trackteroid/
[bsdlicense]: https://opensource.org/licenses/BSD-3-Clause
[bsdlicense-button]: https://img.shields.io/badge/license-BSD-yellow.svg
[downloads]: https://pepy.tech/project/trackteroid
[downloads-button]: https://static.pepy.tech/badge/trackteroid

----
**Declarative, object-oriented wrapper for Ftrack queries. Powerful functional-style interactions with resulting collections.**

Trackteroid depends on [Ftrack](https://www.ftrack.com/en/) and its [Python API](https://ftrack-python-api.readthedocs.io/) a project management and production tracking software specifically designed for the media and entertainment industry. It is commonly used in the fields of film, television, animation, visual effects, and gaming.

## Installation

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):

```shell
pip install trackteroid
```

## Motivation

We have decided to build a wrapping API around the Ftrack Python API to address several limitations and challenges that arise when directly interacting with the Python API. While the Ftrack Python API offers a lot of flexibility, there are certain aspects that can make development and maintenance more cumbersome and less intuitive. By creating a wrapping API, we aim to overcome these challenges and provide a more streamlined and developer-friendly experience. Here are the key reasons for this decision:

- **Simplifying Querying**
  - One of the primary challenges with the Ftrack Python API is the requirement to write queries as SQL-like strings using a custom query language. This approach often leads to complex string formatting and can be hard to read, understand, and debug. This project aims for simplifying the query logic and provides a more expressive and intuitive querying interface. This allows developers to construct queries using a more natural and readable syntax, resulting in improved productivity and reduced errors.


- **Optimizing Query Performance**
  - When working with the Ftrack Python API, developers need to ensure they write efficient queries to minimize unnecessary database calls and optimize performance. This requires careful consideration of the data retrieval logic and understanding the performance implications of different query constructions. In contrast, our API goes the extra mile by attempting to optimize the queries for performance automatically. By leveraging various optimization techniques, we aim to reduce the number of database queries, optimize data retrieval, and improve overall system performance. This alleviates the burden on developers to manually optimize their queries, allowing them to focus more on building features and functionality.


- **Abstracting Database Schema Complexity**
  - Constructing queries with the Ftrack Python API requires a good understanding of the underlying database schema and relationships. This can be a barrier for developers who are not familiar with the intricacies of the Ftrack data model. We aim to abstract away the complexities of the database schema and provide a higher-level interface that shields developers from the details. This simplifies the development process and allows developers to focus on the functionality they want to build, rather than getting lost in the intricacies of the database structure.
  

- **Enhancing Resulting Collections** 
  - The collections returned by the Ftrack Python API after executing queries may not always be convenient enough to interact with directly. They may lack certain methods or properties that would make data manipulation and processing more efficient. We can enrich the resulting collections with additional functionalities and utility methods tailored to the specific needs of our application. This improves the developer experience by providing more convenient and intuitive ways to work with the retrieved data, ultimately enhancing productivity and code maintainability.

  
- **Improved Field Accessibility**
  - The Ftrack Python API does not always present the available fields on entities directly, requiring developers to refer to the documentation or inspect the schema to determine the available properties. We do take steps to enhance field accessibility to some extent. We aim to provide a more intuitive and discoverable way for developers to access entity fields by exposing them directly through the API. This saves developers time and effort by eliminating the need for constant referencing of documentation or inspection of the underlying schema. It enhances productivity and code maintainability by making entity fields more accessible and discoverable within the development workflow.

In summary Trackeroid tries to empower developers by providing a more intuitive and efficient way to interact with the Ftrack platform, ultimately accelerating development, improving code quality, and enhancing the overall user experience.


### Comparison
With **Trackteroid**...
```python
# Calculate and display the total time duration logged for 
# AssetBuild types within specified Shots and Folders.
#
# output:
# Found 9 assetbuilds.
# Found 1 assetbuilds with timelogs.
# {16.0: ['Drone Craft'],
#  'No time tracked yet.': ['Drawer Cabinet 01',
#                           'Gothic Commode 01',
#                           'Shelf 01',
#                           'Side Table 01',
#                           'Small Wooden Table 01',
#                           'Vintage Wooden Drawer 01',
#                           'Wooden Table 01',
#                           'Wooden Table 02']}
  
from pprint import pprint

from trackteroid import (
    Query,
    AssetBuild,
    Folder,
    Task,
    Project
)

assetbuild_collection = Query(AssetBuild).\
    by_name(Project, "sync", "showroom").\
    by_name(Folder, "Asset%", "Delivery 3").\
    get_all(
        projections=[
            Task.Timelog,
            Task.Timelog.duration
        ]
    )

print(
    f"Found {len(assetbuild_collection)} assets.\n"
    f"Found {assetbuild_collection.count(lambda ac: ac.Task.Timelog)} assetbuilds with timelogs."
)

pprint(
    assetbuild_collection.group_and_map(
        lambda abc: abc.Task.Timelog.fold(
            0,
            lambda current, tc: current + tc.duration[0] / 3600
        ) or "No time tracked yet.",
        lambda abc: abc.sort(
            lambda abc: abc.name
        ).name
    )
)
```

...in contrast to the **Ftrack Python API**.
```python
# Calculate and display the total time duration logged for 
# AssetBuild types within specified Shots and Folders.
#
# output:
# Found 9 assetbuilds.
# Found 1 assetbuilds with timelogs.
# {16.0: ['Drone Craft'],
#  'No time tracked yet.': ['Drawer Cabinet 01',
#                           'Gothic Commode 01',
#                           'Shelf 01',
#                           'Side Table 01',
#                           'Small Wooden Table 01',
#                           'Vintage Wooden Drawer 01',
#                           'Wooden Table 01',
#                           'Wooden Table 02']}

from pprint import pprint

import ftrack_api

session = ftrack_api.Session(auto_connect_event_hub=False, auto_populate=False)
project_names = ("sync", "showroom")
folder_specific = "Delivery 3"
folder_unspecific = "Asset%"

query = (
    f"select id, name, assets.name, parent.name, project.name, "
    f"assets.versions.task.timelogs, assets.versions.task.timelogs.duration "
    f"from AssetBuild where project has (name in {project_names}) "
    f"and parent[Folder] has (name is '{folder_specific}' or name like '{folder_unspecific}')"
)

assetbuilds_no_duration = ["No time tracked yet.", []]
assetbuilds_timelog_duration = [0, []]

assetbuilds = session.query(query).all()

for assetbuild in assetbuilds:
    has_duration = False
    for asset in assetbuild["assets"]:
        for version in asset["versions"]:
            durations = [_["duration"] for _ in version["task"]["timelogs"]]
            if any(durations):
                for duration in durations:
                    assetbuilds_timelog_duration[0] += duration / 3600
                if not has_duration:
                    has_duration = True

    if has_duration:
        assetbuilds_timelog_duration[1].append(assetbuild["name"])
    else:
        assetbuilds_no_duration[1].append(assetbuild["name"])

print(
    f"Found {len(assetbuilds)} assetbuilds.\n"
    f"Found {len(assetbuilds_timelog_duration[1])} assetbuilds with timelogs."
)

assetbuilds_no_duration[1].sort()
assetbuilds_timelog_duration[1].sort()

pprint(
    dict(
        [assetbuilds_no_duration, assetbuilds_timelog_duration]
    )
)
```

## Usage

See the [latest documentation][documentation] for usage details.