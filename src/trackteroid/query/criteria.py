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
import re

from collections import namedtuple

import wrapt

from ..configuration import LOGGING_NAMESPACE

LOG = logging.getLogger("{}.criteria".format(LOGGING_NAMESPACE))


class Criterion(object):
    """ a helper class to store and resolve a query criterion"""
    def __init__(self, name="", args=(), kwargs={}, target=None, filter=lambda *args, **kwargs: "", negate=False):
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.target = target
        self.filter = filter
        self.negate = negate

    def resolve(self):
        partial_query = self.filter(self.target, *self.args, **self.kwargs)
        if self.negate:
            partial_query = re.sub("\s+(in|like)\s+", r" not_\1 ", partial_query)
            partial_query = re.sub("\s+is\s+", " is_not ", partial_query)

        return partial_query

    # stay compatible - previously we used a namedtuple as Criterion object
    def as_dict(self):
        return {
            "name": self.name,
            "args": self.args,
            "kwargs": self.kwargs,
            "target": self.target,
            "filter": self.filter,
            "negate": self.negate
        }


class Criteria():
    """ stubs for filtering (aka query criteria)

    This is used to allow proper autocompletion within (some) IDE(s).
    """

    class InvalidArgumentsError(ValueError): pass
    class CriterionNotImplementedError(NotImplementedError): pass


    def by_id(self, *ids):
        raise NotImplementedError

    def by_location(self, *locations):
        raise NotImplementedError

    def by_resource_identifier(self, *resource_identifiers):
        raise NotImplementedError

    def by_version(self, *versions):
        raise NotImplementedError

    def by_name(self, *names):
        raise NotImplementedError

    def by_type(self, *types):
        raise NotImplementedError

    def by_metadata(self, **dictionaries):
        raise NotImplementedError

    def by_description(self, regex):
        raise NotImplementedError

    def by_comment(self, regex):
        raise NotImplementedError

    def by_publisher(self, *publishers):
        raise NotImplementedError

    def by_status(self, *statuses):
        raise NotImplementedError

    def by_state(self, *states):
        raise NotImplementedError

    def by_list(self, *lists):
        raise NotImplementedError

    def by_publish_time(self, start=None, end=None):
        raise NotImplementedError

    def by_status_change_time(self, start=None, end=None):
        raise NotImplementedError

    def by_assignee(self, *assignees):
        raise NotImplementedError

    def by_lifespan(self, start=None, end=None):
        raise NotImplementedError

    def by_outgoing_link(self, *ids):
        raise NotImplementedError

    def by_incoming_link(self, *ids):
        raise NotImplementedError

    def by_component_location(self, *component_locations):
        raise NotImplementedError

    def by_file_type(self, *file_types):
        raise NotImplementedError

    def by_system_type(self, *system_types):
        raise NotImplementedError

    def by_size(self, *sizes):
        raise NotImplementedError

    def by_active_state(self, *states):
        raise NotImplementedError

    def by_action(self, *actions):
        raise NotImplementedError

    def by_data(self, *datas):
        raise NotImplementedError

    def by_publish_state(self, publish_state):
        raise NotImplementedError

    def inject(self, filter):
        raise NotImplementedError

    def by_creation_date(self, *dates):
        raise NotImplementedError

    def by_finish_date(self, *dates):
        raise NotImplementedError

    @staticmethod
    def supported_targets(*supported):
        """ Wraps the filter methods and validates the filter targets against
        the given supported targets. Raises an error if a given target is
        not supported.

        Args:
            *supported (Entity): arbitrary number of supported entities

        Returns:
            func (filter method): original filter method
        """

        @wrapt.decorator
        def wrapper(wrapped, instance, args, kwargs):
            _supported_class_names = [_.__name__ for _ in supported]

            if args:
                if (not [_ for _ in _supported_class_names if _ in ["_EntityBase", "Entity"]]) and inspect.isclass(args[0]):
                    if not ((args[0] in supported) or bool([_ for _ in supported if args[0].__bases__[0] == _])):
                        raise Criteria.InvalidArgumentsError(
                            "You provided an unsupported target {} in `.{}()`. {}.".format(
                                args[0].__name__,
                                wrapped.__name__,
                                "No targets supported" if not supported else "Supported targets: " + ", ".join(
                                    [_.__name__ for _ in supported]
                                )
                            )
                        )

            # Propagate target as TargetRelation object
            if args[0]:
                args = [instance.relationship[args[0]]] + list(args[1:])
            return wrapped(*args, **kwargs)

        return wrapper