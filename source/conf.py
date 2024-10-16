
# todo Please change it to your needs
project = 'Portfollio'
html_title = 'Portfollio'
html_logo = '_static/img/preh_logo.svg'
author = 'preh.gmbh'

# todo select a theme if you want
html_theme = 'sphinx_book_theme'
# html_theme = 'sphinxawesome_theme'
# html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']
extensions = [
    'myst_parser', 
    'sphinx_rtd_theme',
    "sphinx_design",
    "sphinxcontrib.drawio",
    "sphinx_togglebutton"
]
templates_path = ['_templates']
exclude_patterns = []
html_theme_options = {} # we do not have any options at the moment

myst_enable_extensions = [
    "colon_fence",
    "attrs_inline",
    "attrs_block",
    "html_image"
]

suppress_warnings = [
    # "myst.xref_missing", 
    # "myst.iref_ambiguous"
]