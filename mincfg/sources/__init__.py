import os
import logging
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Dict, Union, Any, Set

from .errsrc import ErrorMessagingSource as ErrSrc
from .abstract import CfgDict, ConfigSource
from .builtin import DictSource, OSEnvironSource
from .meta import SubsetSource

__all__ = [ 
    'CfgDict',
    'ConfigSource',
    'DictSource',
    'OSEnvironSource',
    'YamlFileSource',
    'SubsetSource',
    'INIFileSource',
]

try:
    from .yamlfilesrc import YamlFileSource
except ImportError:
    YamlFileSource = ErrSrc("Using YamlFileSource requires mincfg[yaml] or mincfg[all] be installed") # type: ignore

try:
    from .inifilesrc import INIFileSource
except ImportError:
    INIFileSource = ErrSrc("Using INIFileSource requries mincfg[ini] or mincfg[all] be installed")  # type: ignore

