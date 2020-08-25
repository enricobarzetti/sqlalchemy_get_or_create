SQLAlchemy get_or_create()
==========================

SQLAlchemy versions of Django's get_or_create() and update_or_create()

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install sqlalchemy_get_or_create

Usage
-----

get_or_create(session, model, defaults=None, \*\*kwargs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Same as Django's `get_or_create()` but also takes the SQLAlchemy session and model

update_or_create(session, model, defaults=None, \*\*kwargs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Same as Django's `update_or_create()` but also takes the SQLAlchemy session and model

Acknowledgments
===============

#. Django
#. Some code cribbed from https://skien.cc/blog/2014/01/15/sqlalchemy-and-race-conditions-implementing-get_one_or_create/
