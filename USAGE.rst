Usage Guide
===========

*This project it's oriented to all Black Desert Online gamers and guild masters players*.
*Purpose is handle and build discord bot tools to handle more easily guild data or player data*

Developers
~~~~~~~~~~

Prerequisites
-------------

+ Create virtualenv : ``mkvirtualenv bdoc-gm``
+ Enter your existing virtualenv : ``workon bdoc-gm``
+ Install package : ``python setup.py clean build install test``
+ Regenerate database scripts : ``python www/manage.py makemigrations guilds``
+ Apply database scripts : ``python www/manage.py migrate``
+ Create new superuser : ``python www/manage.py createsuperuser`` ( *by default is* ``admin`` / ``adminadmin``)

Startup
-------

+ Can start development webserver with : ``python www/manage.py runserver 0.0.0.0:8000``
+ You can handle data from code with : ``python www/manage.py shell``

.. code:: python


    # Introduce some models to start
    from guilds.models import Guild

    g = Guild(name="MyGuildName")
    g.save()
    # end
    exit()


ToDo list
~~~~~~~~~

+ **mysql server** trought **docker image** configuration
+ **django** admin database

  + Will need to use bootstraped template ( *https://djangopackages.org/packages/p/django-admin-bootstrapped/* )
  + CRUD for ``Guilds`` ( *group of players* )
  + CRUD for ``Members`` ( *basic properties of each player* )
  + CRUD for ``Stats`` ( *specific properties about members* )
  + CRUD for ``Assistance`` ( *to handle reports* )
  + CRUD for ``PvP`` ( *specific items* )
  + CRUD for ``PvE`` ( *specific items* )
  + CRUD for ``Elixirs`` ( *specific items* )
  + CRUD for ``Imperial Crafting`` ( *specific items* )
  + CRUD for ``Crafting`` ( *specific items* )

+ scripts wich depends **discord** API for python ( *https://github.com/Rapptz/discord.py* )

.. code:: python


    # some python code 