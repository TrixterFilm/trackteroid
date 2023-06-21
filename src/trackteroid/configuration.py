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



def _override_configuration():
    """ idenfities and parses a user configuration and applies relevant attributes to this module

    """
    _custom_configuration = os.getenv("TRACKTEROID_CONFIGURATION", False)
    # try our best to source a custom configuration
    if _custom_configuration:
        if not os.path.exists(_custom_configuration):
            raise OSError("Custom configuration `{}` doesn't exist.".format(_custom_configuration))
        if not os.path.splitext(_custom_configuration)[1] in [".py"]:
            raise AssertionError("Custom configuration must `{}` be a .py file.".format(_custom_configuration))

        _LOG.info("Custom configuration specified in `{}`. Trying to load...".format(_custom_configuration))
        try:
            custom_configuration = importlib.load_source("configuration", _custom_configuration)
        except:
            raise RuntimeError(
                "Failed to load custom configuration.\n{}".format("\n".join(traceback.format_exception(*sys.exc_info())))
            )

        relevant_attributes = [_ for _ in globals().keys() if _.isupper() and not _.startswith("_")]
        for attribute in relevant_attributes:
            if hasattr(custom_configuration, attribute):
                _LOG.info("Adding '{}' from user configuration.".format(attribute))
                globals()[attribute] = getattr(custom_configuration, attribute)

# default entries - ALL upper variable names in here can be set in custom user configuration
############################################################################################
# TODO: add example output
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

_LOG = logging.getLogger("{}.configuration".format(LOGGING_NAMESPACE))

_override_configuration()


