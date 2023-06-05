import imp
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
            custom_configuration = imp.load_source("configuration", _custom_configuration)
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


