Migrate Drupal to SQLAlchemy
============================

This is a simple module which maps a drupal site's database to a set of SQLAlchemy models.

Works:

- Database table to Model Mapping (unsubstantiated claim)

TODO:

- More useful things!

HOWTODOIT:

- export a Connection String::

    export SQLALCHEMY_DRUPAL_CONNECT_STRING='mysql://user:pass@myawesomeserver.example.com/drupal_database'