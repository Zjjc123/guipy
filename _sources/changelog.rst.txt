=========
Changelog
=========

Release 0.3.1
==============================

Dependencies
------------

Features added
--------------

- `#29 <https://github.com/Zjjc123/guipy/pull/29>`_ Allow user to import all components with ``from guipy.components import *``

Bugs fixed
----------

Release 0.3.0
==============================
Made changes to the manager and the component base class. Component._draw() should contain most of the drawing that a component needs. Components.root surface is no longer standard in components, as Switch and Button have two static surfaces. Component.update() is now responsible for readying surfaces. In a similar fashion, GUIManager.update() now updates and blits components.

Dependencies
------------

Features added
--------------

- `#23 <https://github.com/Zjjc123/guipy/pull/23>`_ Adding more components
    
    - **Switch**: A switch with two states
    - **Button**: A button that can display text and execute a callback when pressed
    - **Dropdown**: A dropdown menu that supports any object (in menu.py, other types of menus can be put here)
    - **Live Plot**: An extension of Plot. Displays a timestamped data stream and changes the y range dynamically
- `#23 <https://github.com/Zjjc123/guipy/pull/23>`_ Added more util functions.

    - **get_default_font()**: gets a Font object and is cross platform
    - **clip()**: applies a range to a value
    - **float_format()**: converts floats to strings.

Bugs fixed
----------


Release 0.2.0
==============================

Dependencies
------------

Dev Dependencies

- Sphinx
- sphinx-rtd-theme
- sphinx-autoapi
  
Features added
--------------

- `#2 <https://github.com/Zjjc123/guipy/pull/2>`_ Using Poetry for Dependencies, Building, and Releasing. Added GitHub workflows to automatically release on each GitHub tags.
- `#5 <https://github.com/Zjjc123/guipy/pull/5>`_ Using Sphinx for Documentation and adding GitHub Action for Publishing Docs.
- `#20 <https://github.com/Zjjc123/guipy/pull/20>`_ Added Plot and Textbox.

Bugs fixed
----------

- `#17 <https://github.com/Zjjc123/guipy/pull/17>`_ Removed private modules from documentation.