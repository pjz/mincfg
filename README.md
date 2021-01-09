# MinCfg - the Minimum Configuration Handling System

There are many configuration management/definition systems.  This one is mine.

A set of simple tools to build a configuration system with

The first set are 'sources':
  - OSEnvConfigSource: which parses config values from os.environ into hierarchical dictionaries
  - YamlConfigFile: which parses a yaml file into hierarchical dictionaires
The second tool is:
  - MergedConfiguration: which merges multiple configuration sources into a coherent whole

Yes, much more could be done:
    - required keys
    - value validation
    - default parsers
    - default default values (that .get() without a default would default to)
    - more file types (json, ini, env, ... xml?)


Much inspiration - and the .get() signature - is taken from everett, but the
implementation is all mine.

