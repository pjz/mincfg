
from mincfg import MergedConfiguration, OSEnvConfigSource, YamlConfigFile

'''
For the purposes of illustration, imagine that:

/etc/myapp.yaml:

foo: 1
subbar:
    baz: 1
    bar: 1


~/.myapp.yaml:

foo: 2
subbar:
    baz: 2
    blah: 3
blah: 2

and in the environment:

MYAPP_BOO=4
MYAPP_SUBBAR_BRR=4
'''


class MyComplexConfig:

    def __init__(self):
        self.cfg = MergedConfiguration([
            YamlConfigFile("/etc/myapp.yaml"),
            YamlConfigFile("~/.myapp.yaml"),
            YamlConfigFile(os.environ.get("MYAPPCONF")),
            OSEnvConfig("MYAPP"),
        ])

    def subbar_cfg(self):
        '''
        returns the configuration values in the 'subbar' namespace
        as an object.  So using the example config, the result would be:
            SimpleNamespace(bar="1", baz="2", blah="3", brr="4")
        '''
        return self.cfg.as_ns(['subbar'])

