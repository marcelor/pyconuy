# -*- coding: utf-8 -*-
import sys, os

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../speaker'))

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Expand Speaker Python Library'
copyright = u'2013, Marcelo Ramos'


version = '0.1'
release = '0.1.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

man_pages = [
    ('index', 'speaker', u'Expand Speaker Python Library',
     [u'Marcelo Ramos'], 1)
]

texinfo_documents = [
  ('index', 'Expand Speaker Python Library', u'Expand Speaker Python Library',
   u'Marcelo Ramos', 'Expand Speaker Python Library', 'One line description of project.',
   'Miscellaneous'),
]


# Activate the theme.
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'basicstrap'
html_theme_options = {
    'inner_theme': True,
    'inner_theme_name': 'bootswatch-cerulean',
}
