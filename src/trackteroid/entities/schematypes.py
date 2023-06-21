#  BSD 3-Clause License
#
#  Copyright (c) 2023, Trixter GmbH
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

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
