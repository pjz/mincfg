'''
Sources based on python's built-in libraries.
'''

import os
import logging

from .abstract import ConfigSource, CfgDict

logger = logging.getLogger(__name__)


class DictSource(ConfigSource):
    '''
    Uses the supplied dict as a config source.  Useful for defaults.
    '''
    def __init__(self, cfg_dict: CfgDict):
        self.cfg = cfg_dict

    def as_dict(self) -> CfgDict:
        return self.cfg


class OSEnvironSource(ConfigSource):
    '''
    Uses os.environ as a config source, by parsing PREFIXd keys into hierarchical dictionaries, splitting on _
    '''
    def __init__(self, prefix: str):
        self.prefix: str = prefix.strip('_').upper() + '_'

    def as_dict(self) -> CfgDict:
        result: CfgDict = dict()
        for env_key in os.environ:
            if not env_key.startswith(self.prefix):
                continue
            key_path = env_key.split('_')[1:]
            if not key_path:
                continue
            *ns_list, key = key_path
            logger.debug("OSEnvironSource: %s -> %r,%s ", env_key, ns_list, key)
            namespace = result
            for subns in ns_list:
                namespace = namespace.setdefault(subns, dict())
            namespace[key] = os.environ[env_key]
        return result



