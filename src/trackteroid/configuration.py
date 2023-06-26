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

import importlib
import logging
import os
import traceback
import sys

import wrapt


def _fallback_decorator(fallback_func, attribute):
    """ fallback mechanism for the wrapped function on the associated config entry

    Args:
        fallback_func callable: function to wrap
        attribute: name of the attribute the fallback will be applied to

    Returns:
        callable: function wrapper

    """
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        try:
            return wrapped(*args, **kwargs)
        except:
            _LOG.error(
                f"Calling '{attribute}' raised an exception. Falling back to default implementation!",
                exc_info=True
            )
            return fallback_func(*args, **kwargs)

    return wrapper


def _override_configuration():
    """ identifies and parses a user configuration and applies relevant attributes to this module

    """
    _custom_configuration = os.getenv("TRACKTEROID_CONFIGURATION", False)
    # try our best to source a custom configuration
    if _custom_configuration:
        if not os.path.exists(_custom_configuration):
            raise OSError(f"Custom configuration `{_custom_configuration}` doesn't exist.")
        if not os.path.splitext(_custom_configuration)[1] in [".py"]:
            raise AssertionError(f"Custom configuration must `{_custom_configuration}` be a .py file.")

        _LOG.info(f"Custom configuration specified in `{_custom_configuration}`. Trying to load...")
        try:
            spec = importlib.util.spec_from_file_location("custom_configuration", _custom_configuration)
            custom_configuration = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(custom_configuration)
        except:
            raise RuntimeError(
                "Failed to load custom configuration.\n{}".format(
                    "\n".join(traceback.format_exception(*sys.exc_info()))
                )
            )

        relevant_attributes = [_ for _ in globals().keys() if _.isupper() and not _.startswith("_")]
        for attribute in relevant_attributes:
            if hasattr(custom_configuration, attribute):
                _LOG.info(f"Adding '{attribute}' from user configuration.")
                if attribute in _CALLABLES_REQUIRE_FALLBACK:
                    globals()[attribute] = _fallback_decorator(
                        globals()[attribute],
                        attribute
                    )(getattr(custom_configuration, attribute))
                else:
                    globals()[attribute] = getattr(custom_configuration, attribute)


# default entries - ALL upper variable names in here can be set in custom user configuration
############################################################################################

# A functions that gets the current api version string and would return a custom entities
# schema used for relationship resolutions.
RELATIONSHIPS_RESOLVER = lambda api_version: {}

# The primary logger
LOGGING_NAMESPACE = "trackteroid"

# A function that gets the current session and the type name that it requests a
# deletion for and resolves to True or False.
ALLOWED_FOR_DELETION_RESOLVER = lambda session, type_name: True

WARN_ON_INJECT = False
############################################################################################

_LOG = logging.getLogger(f"{LOGGING_NAMESPACE}.configuration")
_CALLABLES_REQUIRE_FALLBACK = [
    "RELATIONSHIPS_RESOLVER",
]

_override_configuration()


