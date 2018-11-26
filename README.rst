QA Code
=======


.. image:: https://img.shields.io/github/issues/netzulo/qacode.svg
  :alt: Issues on Github
  :target: https://github.com/netzulo/qacode/issues

.. image:: https://img.shields.io/github/issues-pr/netzulo/qacode.svg
  :alt: Pull Request opened on Github
  :target: https://github.com/netzulo/qacode/issues

.. image:: https://img.shields.io/github/release/netzulo/qacode.svg
  :alt: Release version on Github
  :target: https://github.com/netzulo/qacode/releases/latest

.. image:: https://img.shields.io/github/release-date/netzulo/qacode.svg
  :alt: Release date on Github
  :target: https://github.com/netzulo/qacode/releases/latest

+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Continuous Integration System |                           Branch : **master**                                                                                                    |
+===============================+==================================================================================================================================================+
|      TravisCI (linux)         | .. image:: https://travis-ci.org/RealImperialGames/BDOC-guildmanager.svg?branch=master                                                           |
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|      Appveyor (windows)       | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true                                                   |
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|      CircleCI (docker)        | .. image:: https://circleci.com/gh/RealImperialGames/BDOC-guildmanager.svg?&style=shield&circle-token=80384cb2233d112dc0785278d5b7c3d8c6a5686c   |
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|      CodeClimate              | .. image:: https://api.codeclimate.com/v1/badges/46279cf9a6a47ed583d6/maintainability                                                            |
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+


Python tested versions
~~~~~~~~~~~~~~~~~~~~~~

+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|  **3.6**          |  **3.5**          |  **3.4**          |  **3.3**          |  **3.2**          |  **2.7**          |
+===================+===================+===================+===================+===================+===================+
|    *Supported*    |    *Supported*    |    *Supported*    |  *Not Supported*  |  *Not Supported*  |    *Supported*    |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+


How to install ?
----------------

+ Install from PIP : ``pip install bdocguildmanager``

+ Install from setup.py file : ``python setup.py install``


Documentation
-------------

+ How to use library, searching for `Usage Guide`_.


How to exec tests ?
-------------------

+ Tests from setup.py file : ``python setup.py test``

+ Install from PIP file : ``pip install tox``
+ Tests from tox : ``tox -l && tox -e TOX_ENV_NAME`` ( *see tox.ini file to get environment names* )


+---------------------+--------------------------------+
| TOX Env name        | Env description                |
+=====================+================================+
| py27,py34,py35,py36 | Python supported versions      |
+---------------------+--------------------------------+
| flake8              | Exec linter in qalab/ tests/   |
+---------------------+--------------------------------+
| coverage            | Generate XML and HTML reports  |
+---------------------+--------------------------------+
| docs                | Generate doc HTML in /docs     |
+---------------------+--------------------------------+

Configuration File
~~~~~~~~~~~~~~~~~~


::

    {}



.. _Usage Guide: USAGE.rst
