"""Sphinx configuration for building project documentation."""

from pathlib import Path

import toml


def _get_project_meta():
    project_root = Path(__file__).resolve().parent.parent
    return toml.load(project_root / "pyproject.toml")["project"]


pkg_meta = _get_project_meta()
project = pkg_meta["name"]
copyright = "2025, Sunil Ghimire"
author = pkg_meta["authors"][0]["name"]

version = pkg_meta["version"]
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
