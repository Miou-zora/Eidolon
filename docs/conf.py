import os
import sys

sys.path.append(os.path.abspath(".."))

extensions = [
    "myst_parser",
    "sphinxawesome_theme.highlighting",

    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
]

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "linkify",
    "tasklist",
]

autodoc_typehints = "none"
autodoc_member_order = "alphabetical"
autodoc_default_options = {
    "members": True,
    "show-inheritance": True
}

html_theme = "sphinxawesome_theme"

set_type_checking_flag = True
source_suffix = ".md"

md_prolog = """
```{eval-rst}
.. :rocker: replace:: 🚀
```
"""
