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

import inspect
import logging
import os
import re
import sys

import ftrack_api


DEFAULT_STUBS_PATH = os.path.dirname(__file__)
STUBS_HEADER = "\nimport typing\n"

LOG = logging.getLogger("trackteroid.stubs")

SESSION = ftrack_api.Session(auto_populate=True, auto_connect_event_hub=False)


def make_file(path, mode=0o777, default_content="", overwrite=False):
    """
    Create a file (if it does not yet exist).
    Args:
        path (str):
        mode (octal, optional): file mode
        default_content (str): optional - the default content to put into the file if it get created here
        overwrite (bool): whether the file should be overwritten, if it already exists

    Returns:
        bool - True if file exists or could be created. False if not.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(os.path.dirname(path)):
        try:
            if not os.path.exists(path) or overwrite:
                with open(path, 'w') as file_write:
                    file_write.write(default_content)
                os.chmod(path, mode)
            return True
        except (OSError, AttributeError, TypeError):
            LOG.error("Failed to create file '%s'" % path, exc_info=True)
            return False


class StubClassBuilder(object):
    """ A simply and limited helper to build class stubs """

    CLASS_TEMPLATE = "class {class_name}{class_bases}:\n"
    CLASS_MEMBER_TEMPLATE = "    {member_name}: {type} \n"
    INSTANCE_ATTRIBUTE_TEMPLATE = "        self.{attribute_name}: {type} \n"
    CLASS_ATTRIBUTE_TEMPLATE = "    {attribute_name}: {type} \n"
    METHOD_TEMPLATE = "    def {method_name}({arguments}{keyword_arguments}) -> {return_type}:{ellipsis} \n"

    TYPE_MAP = {
        "array": "{ref} = {ref}",
        "string": "str = str()",
        "number": "float = float()",
        "boolean": "bool = bool()",
        "integer": "int = int()",
        "mapped_array": "typing.List = [{ref}]",
        "variable": "typing.Any = None",
        "any": "{ref} = {ref}"
    }

    def __init__(self, name, bases=()):
        self._content = {
            "header": "",
            "class_members": [],
            "constructor": "",
            "attributes": [],
            "methods": []
        }
        self._name = name
        self._bases = bases

        self._set_class(name, bases)

    def __str__(self):
        return (
            f"{self._content['header']}"
            f"{''.join(self._content['class_members'])}\n"
            f"{self._content['constructor']}"
            f"{''.join(sorted(self._content['attributes']))}"
            f"{''.join(sorted(self._content['methods']))}\n\n"
        )

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def add_member(self, name, type, ref):
        _type = (self.TYPE_MAP.get(type) or type).format(ref=ref)
        self._content["class_members"].append(
            self.CLASS_MEMBER_TEMPLATE.format(
                member_name=name, type=_type)
        )

    def add_attribute(self, name, type, ref):
        """ add an attribute stub

        Args:
            name (str): attribute name
            type (str): attribute type
            ref (str): attribute type references

        Returns:

        """

        if not self._content["constructor"]:
            raise ValueError(
                "No constructor stub was added. Add an ` __init__` stub via add_method() first."
            )

        _type = (self.TYPE_MAP.get(type) or type).format(ref=ref)

        self._content["attributes"].append(
            self.ATTRIBUTE_TEMPLATE.format(
                attribute_name=name, type=_type
            )
        )

    def add_method(self, name, arguments, keyword_arguments="", return_type="None"):
        """ add a method stub

        Args:
            name (str): method name
            arguments (str): collapsed argument type hints
            keyword_arguments (str): collapses keyword argument type hints
            return_type (str): the expected return type

        Returns:

        """
        if keyword_arguments:
            arguments += ", "

        _method_str = self.METHOD_TEMPLATE.format(
            method_name=name,
            arguments=arguments,
            keyword_arguments=keyword_arguments,
            return_type=return_type,
            ellipsis="{ellipsis}"
        )

        # some special treatment
        if name == "__init__":
            self._content["constructor"] = _method_str.format(ellipsis="")
        else:
            self._content["methods"].append(_method_str.format(ellipsis="..."))

    def _set_class(self, name, bases):
        if bases:
            bases = "(" + ", ".join(list(bases)) + ")"
        else:
            bases = ""
        self._content["header"] = self.CLASS_TEMPLATE.format(class_name=name, class_bases=bases)

    def set_class_bases(self, bases):
        self._set_class(self.name, bases)

    @property
    def name(self):
        return self._name


def get_stubs_from_schemas(include_custom_attributes=False):
    """ generate stubs from available entity schemas

    Returns:
        list: list with StubClassBuiler instances
    """
    stubs = []

    for element in SESSION.schemas:
        stub = StubClassBuilder(name=element["id"])

        # ensure we add the __init__ first, because the stub builder is limited
        # and expects we have that added, to use the proper indentation for the
        # attributes
        for name, _ in element["properties"].items():
            if name == "custom_attributes":
                # skip custom attributes as we will add them individually later
                continue
            items = _.get("items")
            ref = _.get("$ref", "")
            if items:
                ref = _["items"].get("$ref", "")
            if ref:
                ref = "{}".format(ref)
            _type = _.get("type")
            if _type:
                stub.add_member(name=name, type=_type, ref=ref)
            else:
                stub.add_member(name=name, type="any", ref=ref)

        if include_custom_attributes and "custom_attributes" in element["properties"].keys():
            item = SESSION.query("select custom_attributes from {}".format(stub.name)).first()
            if item:
                for key in item["custom_attributes"].keys():
                    stub.add_member(name="custom_" + key, type=_type, ref=ref, cls_attribute=True)

        stubs.append(stub)

    return stubs


def get_extended_entity_stubs(classes, stubs):
    """ extend given stubs for our entity implementations

    Args:
        classes (list): list of classes that need to match the stub names
        stubs (list): list of StubClassBuilder instances

    Returns:
        list: list of StubClassBuilder instances

    """
    stubs_map = {_.name: _ for _ in stubs}
    class_map = dict(classes)

    stubs = []

    for stub_name, stub in stubs_map.items():
        _cls = class_map.get(stub_name)
        if _cls:

            stub.add_method(
                name="__init__",
                arguments="self, *args",
                keyword_arguments="**kwargs",
            )

            for method in inspect.getmembers(
                    _cls,
                    predicate=lambda x: (inspect.isfunction(x) or inspect.ismethod(x)) and not x.__name__.startswith(
                        "__")):

                specs = inspect.getfullargspec(method[1])
                varargs = specs.varargs or ""
                if varargs:
                    varargs = ", *" + varargs

                kwargs = []
                args = specs.args or []
                if specs.defaults:
                    for i, element in enumerate(specs.args[-len(specs.defaults):]):
                        if isinstance(specs.defaults[i], str):
                            kwargs.append("{}=\"{}\"".format(element, specs.defaults[i]))
                        else:
                            kwargs.append("{}={}".format(element, specs.defaults[i]))
                    args = specs.args[:-len(specs.defaults)]

                args = ", ".join(args)
                kwargs = ", ".join(kwargs)

                # always expect the forwarded Query return type
                # in case we are a "by_*" Criteria method
                if re.search(r"^by_", method[0]):
                    return_type = "Query({})".format(stub_name)
                elif re.search(r"^inject$", method[0]):
                    return_type = "Query({})".format(stub_name)
                    args = "self, filter"
                    kwargs = ""
                    varargs = ""
                elif method[0] == "get" or method[0].startswith("get_"):
                    return_type = stub_name
                elif method[0] == "create":
                    return_type = stub_name
                elif method[0] == "create_batch":
                    return_type = stub_name
                elif re.match(r"^(un)?link_.*", method[0]):
                    return_type = stub_name
                elif method[0] == "pre_create":
                    continue
                elif method[0] == "delete":
                    return_type = "None"
                else:
                    return_type = "typing.Any"

                # be stupid and ignore any kind of namespace for base classes
                stub.set_class_bases([_.__name__ for _ in _cls.__bases__])
                stub.add_method(
                    name=method[0],
                    arguments=args + varargs,
                    keyword_arguments=kwargs,
                    return_type=return_type
                )
                # if method is a criterion let's add the negated counterpart
                if re.search(r"^by_", method[0]):
                    stub.add_method(
                        name="not_{}".format(method[0]),
                        arguments=args + varargs,
                        keyword_arguments=kwargs,
                        return_type=return_type
                    )

                # TODO: add overload for get, to add relative terminator

            # TODO improve for base types like TypedContext, Component
            #  that support filtering via Entity
            stub.add_method(
                name="__getitem__",
                arguments="self, item: typing.Union[int, slice, str]",
                keyword_arguments="",
                return_type=stub_name
            )
            stub.add_method(
                name="fetch_attributes",
                arguments="self, projections: typing.List[typing.Union[str, Entity]]",
                keyword_arguments="",
                return_type=stub_name
            )
        stubs.append(stub)

    return stubs


def generate_entitites_stubs():
    """ (re)generate our entities.pyi stub file

    Notes:
        This overrides the stub .pyi file at the expected location. Here we will
        override trixter.entities.entities.pyi with the freshly inspected data.
        Use this whenever the implementation of any Entity subclass changes or
        the ftrack entities schema was modified.

    Returns:

    """
    # TODO: The entities lookup should go away once our project is a proper package.
    #  For now look up the expected package name dynamically based on the location of our script
    #  and make 'entities' importable.
    entities_path = os.path.dirname(os.path.dirname(__file__))
    package_name, package_root = os.path.basename(entities_path), os.path.dirname(entities_path)
    sys.path.insert(0, package_root)
    entities = getattr(__import__(package_name), "entities")
    declarations = getattr(__import__(package_name), "declarations")

    classes = inspect.getmembers(
        entities,
        predicate=lambda entity:
            inspect.isclass(entity)
            and issubclass(entity, (entities.Entity, declarations.ForwardDeclaration))
            and " " not in entity.__name__  # TODO: why do we get members with whitespace in name?
    )

    stubs = STUBS_HEADER
    stubs += "from .base import Entity\n"
    stubs += "from ..query import Query\n\n"

    for stub in sorted(get_extended_entity_stubs(classes, get_stubs_from_schemas()), key=lambda x: x.name):
        stubs += stub

    path = os.path.join(os.path.dirname(entities.__file__), "entities.pyi")
    if os.path.isfile(path):
        os.remove(path)

    LOG.info("Updating stubsfile {}...".format(path))
    make_file(path, default_content=stubs)


if __name__ == '__main__':
    generate_entitites_stubs()
