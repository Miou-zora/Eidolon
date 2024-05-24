import os
import sys

sys.path.append(os.path.abspath(".."))

extensions = [
    "myst_parser",
    "sphinxawesome_theme.highlighting",
]

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "linkify",
    "tasklist",
]

html_theme = "sphinxawesome_theme"

set_type_checking_flag = True
source_suffix = ".md"
