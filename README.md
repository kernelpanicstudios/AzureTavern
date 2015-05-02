Azure Tavern
============

The best place to roleplay on the Internet! At least, that's the goal :-)

The mission of Azure Tavern is to offer an enhanced roleplaying experience
by providing tools for players and GMs to socialize, play games, and manage
game metadata such as characters, settings and locations, and character sheet
information.

Dependencies
------------

  * Python 2.7 (reference: 2.7.3)
  * Django 1.8 (reference: 1.8.2)
  * South 0.8 (reference: 0.8.4)
  * django-braces 1.3 (reference: 1.3.1)

Developer Setup
---------------

Here are the instructions for setting up Azure Tavern for local development:

  1. Clone the repository and make sure you have the latest code.
  2. Navigate into `{YourLocalProjectDirectory}/src/AzureTavern/AzureTavern`
     and copy **local_settings.py.template** to **local_settings.py** in the
     same directory.
  3. Make changes to local_settings.py to match your desired database settings.
  4. Run `python src/AzureTavern/manage.py syncdb` to create tables etc. for
     the Django apps which do not use South migrations.
  5. Run `python src/AzureTavern/manage.py migrate` to create tables etc. for
     the Django apps which do use South migrations (including the ones we are
     developing here).
  6. Sanity check: Run `python src/AzureTavern/manage.py runserver` from the
     project root and make sure the server starts up. If it does, you're good
     to go; if not, reach out to the other developers for help.

Maintainer
----------

The maintainer and lead developer for this project is Kevin Partington, aka
Platinum Azure. He can be reached via e-mail: kevin AT kernelpanicstudios DOT
com.
