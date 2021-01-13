
.. docs on the contents of mincfg.sources

Sources
#######

Sources are how config information is gathered.  The point at which you need a configuration *system* is when you
want to support more than one source.

Builtin Sources
***************

Sources available if all you have are Python's basic batteries.

.. autoclass:: mincfg.DictSource

.. autoclass:: mincfg.OSEnvironSource

AddOn Sources
*************

These require support modules be installed.

.env files
==========

Using `PyYaml`_

.. code-block:: shell

    pip install mincfg[env]

.. autoclass:: mincfg.DotEnvFileSource

.ini files
==========

Using `configobj`_

.. code-block:: shell

    pip install mincfg[ini]

.. autoclass:: mincfg.INIFileSource

.yaml files
===========

Using `python-dotenv`_

.. code-block:: shell

    pip install mincfg[yaml]

.. autoclass:: mincfg.YamlFileSource

.. _PyYaml: https://pyyaml.org/wiki/PyYAMLDocumentation
.. _python-dotenv: https://pypi.org/project/python-dotenv/
.. _configobj: https://configobj.readthedocs.io/en/latest/configobj.html

Abstract Sources
****************

...and because there's always a newer format coming down the line, there's an Abstract Base Class that they're
all derived from

.. autoclass:: mincfg.ConfigSource

