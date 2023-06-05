from .query import Query
from .session import SESSION
from .entities import *
from .entities.schematypes import (
    CUSTOM_ATTRIBUTE_TYPE_COMPATIBILITY,
    OBJECT_TYPES,
    ASSET_TYPES,
    TASK_TYPES,
    PROJECT_SCHEMAS
)
from .constants import __VERSION__

# for usage in stubsgenerator
import entities