# Configuration

To tailor Trackteroid to meet your specific requirements, you have the ability to configure it according to your needs.

Configuration in Trackteroid is accomplished through a Python file, providing a high degree of flexibility and adjustability in a language you are already familiar with.

To make your configuration file accessible, you can utilize the `TRACKTEROID_CONFIGURATION` environment variable.

Here's an example for Linux with Bash:
```shell
export TRACKTEROID_CONFIGURATION=/path/to/my/trackteroid_user_config.py
```

The subsequent section outlines the available configuration options within Trackteroid and explains how to customize them according to your preferences.
Configuration entries are defined in ALL_CAPS style and can store constant values or callables.


## ALLOWED_FOR_DELETION_RESOLVER

The _ALLOWED_FOR_DELETION_RESOLVER_ is a callable function that provides the ability to implement overrides for controlling the deletion of specific entity types. When invoked, this function receives the current session object and the name of the entity type that is being requested for deletion.
Default Implementation:
```python
ALLOWED_FOR_DELETION_RESOLVER = lambda session, type_name: True
```

```{warning}
While this function primarily serves as an **additional** security measure to prevent accidental deletions, it should not be relied upon as a substitute for proper API user access management in FTrack.
```


## LOGGING NAMESPACE

The logging namespace utilized by Trackteroid is set to `trackteroid` by default. This namespace serves as the primary identifier for logging purposes within Trackteroid. Modifying this namespace allows for seamless integration of the API into your existing codebase without the need for additional logging configuration setup.


## RELATIONSHIPS_RESOLVER

The _RELATIONSHIPS_RESOLVER_ is a callable function that plays a crucial role in supplying relationship information that cannot be automatically derived by Trackteroid.

Default implementation:
```python
RELATIONSHIPS_RESOLVER = lambda api_version: {}
```

When invoked, the API will pass the version string to the callable, ensuring resilience in the event of changes to the Trackteroid API that necessitate schema modifications. Your resolver function should return a dictionary adhering to a specific schema.

Let's explore the schema using a comprehensive example that involves reading a JSON file to provide the necessary relationship information.

Here's an example implementation of a custom resolver in a _trackteroid_user_config.py_ file.

```python
def relationships_from_json(**kwargs):
    import json

    api_version = kwargs.get("api_version", "0.0.1")

    if api_version.startswith("0.1"):
        with open("/path/to/trackteroid_relationships.json") as f:
            return json.load(f)
    elif api_version.startswith("0.2"):
        with open("/path/to/trackteroid_relationships_new.json") as f:
            return json.load(f)


RELATIONSHIPS_RESOLVER = relationships_from_json
```
In this example, the custom resolver function relationships_from_json reads the appropriate JSON file based on the API version. The returned data from the JSON file provides the relationship information needed by Trackteroid.

Here's an example of the JSON file _trackteroid_relationships.json_ that conforms to the schema:

```json
{
   "entities":{
      "AssetVersion":{
         "AssetBuild":"asset.parent[AssetBuild]",
         "AssetGroup":"asset.parent[AssetBuild].parent[AssetGroup]",
         "Shot":"asset.parent[Shot]",
         "Sequence":["asset.parent[Shot].parent[Sequence]", "asset.parent[Sequence]"]
      },
      "Component":{
         "AssetBuild":"asset.parent[AssetBuild]",
         "AssetGroup":"asset.parent[AssetBuild].parent[AssetGroup]",
         "Shot":"asset.parent[Shot]",
         "Sequence":"asset.parent.parent[Sequence]",
         "Project":"asset.parent.parent.project"
      }
   },
   "overrides":[
      {
         "entities":{
            "AssetVersion":{
               "Shot":"asset.parent[Folder].parent[Shot]"
            }
         },
         "name":"vfx"
      },
      {
         "entities":{
            "AssetVersion":{
               "Episode":"asset.parent[Shot].parent[Episode]"
            }
         },
         "inherit":0,
         "name":"episodic"
      }
   ]
}
```

The resulting dictionary schema can be summarized as follows:

```
{
  "entities":{
    <Source_Entity_Type_Name>:{
      <Target_Entity_Type_Name>:<str>,
      <Target_Entity_Type>:[<str>,<str>]
    }
  },
  "overrides": [
    {
      "entities":{
        <Source_Entity_Type_Name>:{
          <Target_Entity_Type_Name>:<str>,
          <Target_Entity_Type_Name>:[<str>,<str>]
        }
      },
      "name":<str>,
      "inherit"(default:True):<bool>
    }
  ]
}
```

The schema at the root level contains the relationships that will be used as the default schema for the Query. These relationships serve as the base schema, which can be reused or overridden for other custom schemas, as demonstrated in the examples for vfx and episodic.
If a target entity entry contains multiple values it presents an OR relationship.

Here's an example to illustrate how the overrides are applied using the SCHEMA object:
```python
from pprint import pprint

from trackteroid import SCHEMA

pprint(SCHEMA.default)
# output: 
# {'entities': {'AssetVersion': {'AssetBuild': 'asset.parent[AssetBuild]',
#                                'AssetGroup': 'asset.parent[AssetBuild].parent[AssetGroup]',
#                                'Sequence': ['asset.parent[Shot].parent[Sequence]',
#                                             'asset.parent[Sequence]'],
#                                'Shot': 'asset.parent[Shot]'},
#               'Component': {'AssetBuild': 'asset.parent[AssetBuild]',
#                             'AssetGroup': 'asset.parent[AssetBuild].parent[AssetGroup]',
#                             'Project': 'asset.parent.parent.project',
#                             'Sequence': 'asset.parent.parent[Sequence]',
#                             'Shot': 'asset.parent[Shot]'}}}

pprint(SCHEMA.vfx)
# output: 
# {'entities': {'AssetVersion': {'AssetBuild': 'asset.parent[AssetBuild]',
#                                'AssetGroup': 'asset.parent[AssetBuild].parent[AssetGroup]',
#                                'Sequence': ['asset.parent[Shot].parent[Sequence]',
#                                             'asset.parent[Sequence]'],
#                                'Shot': 'asset.parent[Folder].parent[Shot]'},
#               'Component': {'AssetBuild': 'asset.parent[AssetBuild]',
#                             'AssetGroup': 'asset.parent[AssetBuild].parent[AssetGroup]',
#                             'Project': 'asset.parent.parent.project',
#                             'Sequence': 'asset.parent.parent[Sequence]',
#                             'Shot': 'asset.parent[Shot]'}},
#  'name': 'vfx'}

pprint(SCHEMA.episodic)
# output:
# {'entities': {'AssetVersion': {'Episode': 'asset.parent[Shot].parent[Episode]'}},
#  'name': u'episodic'}
```

In the example, `SCHEMA.default` represents the default schema, which serves as the baseline for other schemas. `SCHEMA.vfx` demonstrates an override named "vfx," which inherits all the entries from the default schema but overrides the relationship for `Shot`. On the other hand, `SCHEMA.episodic` demonstrates an override named "episodic" that doesn't inherit from the default schema and only includes the relationships it provides, as it has dis abled inheritance. 
```{warning}
The relationships provided by your resolver take precedence over the relationships automatically derived from the Session/Database schema.
```


## WARN_ON_INJECT 

The _WARN_ON_INJECT_ variable can be set to either `True` or `False`, with the default value being `False`. When set to `True`, it enables the emission of a `logging.warning` message when the _inject_ query criterion is used.

The _inject_ criterion serves as a workaround for situations where certain criteria implementations are missing. Enabling the _WARN_ON_INJECT_ option can be useful in identifying the usage of this criterion in your codebase and exploring potential alternative approaches that may exist.
