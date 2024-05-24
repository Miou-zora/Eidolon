import os
import sys

sys.path.append(os.path.abspath(".."))

extensions = [
    "myst_parser",
]

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "linkify",
    "tasklist",
]

set_type_checking_flag = True
source_suffix = ".md"
