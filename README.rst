*********************************************
Postgres.conf optimizator
*********************************************

.. contents::

======================================
Makina Corpus sponsorised software
======================================
|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com


=======================
README
=======================

    This script some optimized parameters in a postgresql configuration file according
    to the current machine possibilities and parameters given on the command
    line.

BASIC USAGE
---------------

    pypgoptimizator -i pg.conf -o new.pg.conf

HELP
--------

    pypgoptimizator --help

Parameters
---------------

    - *-b*: The shared buffer size. It's 8192 by default, and it can be changed at
      compilation time, pgsql side.
    - *-l*: The output logs filename scheme (log_filename paramater)
    - *-o*: The output file to write into
    - *-i*: The input postgresql configuration file to read info from
    - *-m*: max connections parameter for postgres (default 100)
    - *-p*: The availaible Memory in KBytes, defaults to all available memory



