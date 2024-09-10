"""
Module conf.py

Notes
------

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Project information:
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

"""

# Libraries
import os
import sys
import datetime

# noinspection PyUnresolvedReferences
import revitron_sphinx_theme


'''
Path
'''
sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../revitron'))


'''
Master
'''
master_doc = 'index'


'''
Basic
'''
project = 'Emissions'
project_copyright = '{}, greyhypotheses'.format(datetime.datetime.now().year)
author = 'greyhypotheses'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

Sphinx extension modules. Extensions are either Sphinx extensions, named 'sphinx.ext.*', 
or custom ones.  Note, myst_enable_extensions excludes 'linkify'
'''
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'revitron_sphinx_theme',
    'autodocsumm',
    'sphinxcontrib.httpdomain',
    'sphinx.ext.napoleon',
    'sphinxext.opengraph',
    'sphinxcontrib.jquery',
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx_design',
    'sphinxcontrib.mermaid'
]

myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
    'attrs_block',
    'attrs_inline'
]

add_module_names = False

napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False


'''
Mathematics
'''
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
myst_dmath_double_inline = True


'''
Templates
'''
templates_path = ['_templates']


'''
Patterns
'''
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

'''

html_theme = 'revitron_sphinx_theme'

html_theme_options = {
    'canonical_url': 'https://prml-0003.github.io/',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'github_url': 'https://github.com/prml-0003/prml-0003.github.io',
    'logo_mobile': '_static/32x32.svg'
}

html_static_path: list[str] = ['_static']

html_css_files: list[str] = [
    'css/custom.css', 'css/generic.css',
    'https://fonts.googleapis.com/css?family=Vollkorn',
    'https://fonts.googleapis.com/css?family=Tangerine'
]

html_js_files: list[str] = ['https://code.jquery.com/jquery-3.7.0.min.js',
                            'https://code.highcharts.com/stock/highstock.js',
                            'https://code.highcharts.com/stock/modules/data.js',
                            'https://code.highcharts.com/stock/modules/exporting.js',
                            'https://code.highcharts.com/stock/modules/export-data.js',
                            'https://code.highcharts.com/stock/modules/accessibility.js',
                            'https://code.highcharts.com/highcharts.js',
                            'https://code.highcharts.com/modules/networkgraph.js'
                            ]

html_title = 'CLIMATE & SUSTAINABILITY'

html_favicon = '_static/favicon.ico'

html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Parent',
             'url': 'https://github.com/theartificialintelligenceunit'},
            {'title': 'Summary',
             'url': 'https://prml-0003.github.io/docs/build/html/summary/summary.html'}
        ]
    },
    'display_github': True,
    'github_repo': 'prml-0003.github.io',
    'conf_py_path': 'develop/docs/source/'
}

html_sidebars = {}


'''
Options for intersphinx extension
https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration
'''
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
