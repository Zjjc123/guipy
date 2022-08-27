# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Guipy"
copyright = "2022, Casey Culbertson, Jason Zhang"
author = "Casey Culbertson, Jason Zhang"
release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["autoapi.extension"]

autoapi_type = "python"
autoapi_dirs = ["../guipy"]


def skip_util_classes(app, what, name, obj, skip, options):
    # if name starts with a _
    if name.split(".")[-1][0] == "_":
        skip = True
    return skip


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_util_classes)


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
