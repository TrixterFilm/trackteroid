# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import time

project = 'Trackteroid'
copyright = f'2023-{time.strftime("%Y")} Trixter Film GmbH'
author = 'Dennis Weil, Rico Koschmitzky'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# Add the following lines at the top of the file
import myst_parser
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

extensions = [
    'myst_parser',
    'sphinx_togglebutton',
]
myst_enable_extensions = [
    'colon_fence',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_favicon = "_static/favicon.ico"
html_logo = '_static/logo_white.svg'

suppress_warnings = [
    'myst.xref_missing',
    'myst.header'
]