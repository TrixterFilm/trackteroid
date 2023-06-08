# Configuration

To tailor Trackteroid to meet your specific requirements, you have the ability to configure it according to your needs.

Configuration in Trackteroid is accomplished through a Python file, providing a high degree of flexibility and adjustability in a language you are already familiar with.

To make your configuration file accessible, you can utilize the `TRACKTEROID_CONFIGURATION` environment variable.

Here's an example for Linux with Bash:
```shell
export TRACKTEROID_EXAMPLE=/path/to/my/trackteroid_user_config.py
```

The subsequent section outlines the available configuration options within Trackteroid and explains how to customize them according to your preferences.
Configuration entries are defined in ALL_CAPS style and can store constant values or callables.

## RELATIONSHIPS_RESOLVER

The _RELATIONSHIPS_RESOLVER_ is a callable function that plays a crucial role in supplying relationship information that cannot be automatically derived by Trackteroid.

Default implementation:
```python
RELATIONSHIPS_RESOLVER = lambda api_version: {}
```

When invoked, the API will pass the version string to the callable, ensuring resilience in the event of changes to the Trackteroid API that necessitate schema modifications. Your resolver function should return a dictionary adhering to a specific schema.

Let's delve into the schema and demonstrate the usage of a custom resolver through a comprehensive example. In this example, we'll utilize a JSON file that the resolver will read and use to provide the necessary information.

We implement a custom function that loads content from different json files:

_trackteroid_user_config.py_

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

We create a json file that adds relationship for AssetVersion and Component exlusively for demonstration purpose.

_trackteroid_relationships.json_
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

Based on the json example we can abstract the actual schema and explain the content.

_schema_
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