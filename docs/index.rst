:hide-toc:

.. mincfg documentation master file, created by
   sphinx-quickstart on Tue Jan 12 20:59:34 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MinCfg: The Minimal Config System
=================================

Release v\ |version|.

.. image: https://github.com/pjz/mincfg/workflows/Python%20tests/badge.svg
    :target: https://github.com/pjz/mincfg/workflows/Python%20tests/badge.svg

--------------



*Handling simple things simply...*

.. code-block:: python

    from mincfg import MergedConfiguration, YamlFileSource

    mycfg = MergedConfiguration([YamlFileSource('/etc/myapp.yaml'), 
                                 YamlFileSource('~/.myapp.yaml')])

*and more complicated things reasonably...*

.. code-block:: python

    from mincfg import MergedConfiguration, YamlFileSource,\
                       OSEnvironSource, DictSource
   
    defaults = DictSource({'url': 'https://example.com', 
                           'user': 'testuser', 
                           'pass': 'testpassword' })

    mycfg = MergedConfiguration([defaults, 
                                 YamlFileSource('/etc/myapp.yaml'), 
                                 YamlFileSource('~/.myapp.yaml'),
                                 YamlFileSource(os.environ.get('MYAPPCFG')),
                                 OSEnvironSource('MYAPP_')
                                ])

        
The main caveat is that all config keys are case-insensitive (lower case).


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   configs.rst
   sources.rst


.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
