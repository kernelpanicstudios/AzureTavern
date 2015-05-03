Azure Tavern
============

The best place to roleplay on the Internet! At least, that's the goal :-)

The mission of Azure Tavern is to offer an enhanced roleplaying experience
by providing tools for players and GMs to socialize, play games, and manage
game metadata such as characters, settings and locations, and character sheet
information.

Dependencies
------------

See **src/azuretavern/requirements.txt**.

Developer Setup
---------------

Here are the instructions for setting up Azure Tavern for local development:

  1. Clone the repository and make sure you have the latest code.
  2. Navigate into `{YourLocalProjectDirectory}/src/AzureTavern` and run
     `pip install -r requirements.txt`.
  3. Navigate into `{YourLocalProjectDirectory}/src/AzureTavern/AzureTavern`
     and copy **local_settings.py.template** to **local_settings.py** in the
     same directory.
  4. Make changes to local_settings.py to match your desired database settings.
  5. Run `python src/AzureTavern/manage.py migrate` to create tables etc. for
     the installed Django apps (whether or not they use migrations).
  6. Sanity check: Run `python src/AzureTavern/manage.py runserver` from the
     project root and make sure the server starts up. If it does, you're good
     to go; if not, reach out to the other developers for help.

Maintainer
----------

The maintainer and lead developer for this project is Kevin Partington, aka
Platinum Azure. He can be reached via e-mail: kevin AT kernelpanicstudios DOT
com.
