# Configuration file for the Sphinx documentation builder.

# -- Project information
source_suffix = ['.rst', '.md']

extensions = [
    "recommonmark",
    'alabaster'
]

html_static_path = ['_static']

language = 'zh'

exclude_patterns = []

project = "Dbird's dices"
copyright = '2022, Dogbird'
author = 'DarkseaDogbird'

release = '1.0.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'alabaster'

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
