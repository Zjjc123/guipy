=========
Changelog
=========

Release 0.3.0
==============================

Dependencies
------------

Features added
--------------

- `#23 <https://github.com/Zjjc123/guipy/pull/23>`_ Adding more components
    - **Switch**: A switch with two states
    - **Button**: A button that can display text and execute a callback when pressed
    - **Dropdown**: A dropdown menu that supports any object (in menu.py, other types of menus can be put here)
    - **LivePlot**: An extension of Plot. Displays a timestamped data stream and changes the y range dynamically.

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