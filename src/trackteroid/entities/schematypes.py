import re

from arrow.arrow import Arrow
from datetime import datetime
from collections import defaultdict

from ..session import SESSION


class AttributeInfo(object):
    def __init__(self, types=tuple(), array=False, mutable=True):
        self.types = types
        self.array = array
        self.mutable = mutable


class _CustomAttributeTypeCompatibility(object):
    _compatibility_map = {
        "number": (int, float),
        "date": (Arrow, datetime),
        "text": (str),
        "boolean": (bool,),
        "enumerator": (str),
        "dynamic_enumerator": (str),
        "expression": (str)
        }

    def __init__(self):
        self.attributes = {}

    def __getattr__(self, item):
        if not self.attributes:
            configs = SESSION.query("select key, type.name from CustomAttributeConfiguration").all()
            for config in configs:
                self.attributes[config["key"]] = AttributeInfo(
                        types=self._compatibility_map[config["type"]["name"]],
                        )

        if item in self.attributes:
            return self.attributes[item]

        raise KeyError("Custom Attribute '{}' not found.".format(item))


class TypesBase(object):
    projections = ["id", "name"]
    entity_type = None

    def __init__(self):
        self._types = defaultdict(dict)

    def get(self, item, session=SESSION):
        if " " in item:
            item = self._to_camel_case(item)
        session_id = str(session)
        types = self._types[session_id]
        if not types:
            object_types = session.query(
                "select {} from {}".format(", ".join(self.projections), self.entity_type)
            ).all()
            for _type in object_types:
                types[self._to_camel_case(_type["name"])] = _type

        if item in types:
            return types[item]
        elif item == "types":
            return types

        raise KeyError("{} '{}' not found.".format(self.entity_type, item))

    def __getattr__(self, item):
        return self.get(item)

    def __getitem__(self, item):
        return self.get(item)

    @staticmethod
    def _to_camel_case(string):
        return "".join([_.capitalize() for _ in re.findall(r"[a-zA-Z]*\s*?", string)])


class _ObjectTypes(TypesBase):
    entity_type = "ObjectType"


class _AssetTypes(TypesBase):
    entity_type = "AssetType"


class _ProjectSchemas(TypesBase):
    entity_type = "ProjectSchema"


class _TaskTypes(TypesBase):
    entity_type = "Type"


CUSTOM_ATTRIBUTE_TYPE_COMPATIBILITY = _CustomAttributeTypeCompatibility()
OBJECT_TYPES = _ObjectTypes()
ASSET_TYPES = _AssetTypes()
TASK_TYPES = _TaskTypes()
PROJECT_SCHEMAS = _ProjectSchemas()
