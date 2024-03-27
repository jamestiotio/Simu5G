# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('_themes'))


# -- Project information -----------------------------------------------------

project = 'Simu5G'
author = 'Antonio Virdis, Giovanni Nardini'
copyright = author

# The short X.Y version this doc refers to (last tagged release)
release = re.sub('^v', '', os.popen('git describe --tags --abbrev=0 --match=v[0-9].*').read().strip())
# Git version this documentation built from (including last release tag, number of commits since then and git hash)
version = re.sub('^v', '', os.popen('git describe --tags --abbrev=4 --match=v[0-9].*').read().strip())

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '7.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#    'IPython.sphinxext.ipython_console_highlighting',
#    'IPython.sphinxext.ipython_directive',
    'sphinx.ext.mathjax',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.imgconverter',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    #'sphinxcontrib.images',
    'tools.doxylink',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [ '.rst',
  '.md',
]

# Source parsers
source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

# The root toctree document.
root_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
  '_build', '_deploy', 'Thumbs.db', '.DS_Store', '**/_docs', 'global.rst',
  '_static', '_themes', '_templates', '.venv', 'images'
#  'simulations/**'
#  'showcases/**',
#  'tutorials/**',
]

# graphviz options
graphviz_output_format = 'svg'

# -- python auto doc generator configuration ----------------------------------
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
autosummary_imported_members = False
autosummary_ignore_module_all = True
html_show_sourcelink = False  # Remove 'view source code' from top of page (for html, not python)
autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
set_type_checking_flag = True  # Enable 'expensive' imports for sphinx_autodoc_typehints
#autodoc_typehints = "description" # Sphinx-native method. Not as good as sphinx_autodoc_typehints
add_module_names = False # Remove namespaces from class/method signatures

# Exclusions
# To exclude a module, use autodoc_mock_imports. Note this may increase build time, a lot.
# (Also, when installing on readthedocs.org, we omit installing Tensorflow and
# Tensorflow Probability so mock them here instead.)
autodoc_mock_imports = []

# To exclude a class, function, method or attribute, use autodoc-skip-member. (Note this can also
# be used in reverse, ie. to re-include a particular member that has been excluded.)
# 'Private' and 'special' members (_ and __) are excluded using the Jinja2 templates; from the main
# doc by the absence of specific autoclass directives (ie. :private-members:), and from summary
# tables by explicit 'if-not' statements. Re-inclusion is effective for the main doc though not for
# the summary tables.
def autodoc_skip_member_callback(app, what, name, obj, skip, options):
    exclusions = ('')
    inclusions = ('')
    if name in exclusions:
        return True
    elif name in inclusions:
        return False
    elif obj.__doc__ == None: # skip everything that does not have an explicit docstring
        return True
    else:
        return skip

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme_path = ['_themes']

html_baseurl = 'https://simu5g.org'

extensions.append("sphinx_immaterial")
html_theme = "sphinx_immaterial"
html_css_files = ['custom.css',]

# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
        "logo": "material/book-open-page-variant-outline",
    },
    "site_url": "https://simu5g.org/",
    "repo_url": "https://github.com/Unipisa/Simu5G",
    "repo_name": "Simu5G",
    # "edit_uri": "blob/site/doc/src",
    "globaltoc_collapse": True,
    "features": [
        #"navigation.expand",
        "navigation.tabs",
        #"toc.integrate",
        #"navigation.sections",
        "navigation.instant",
        # "header.autohide",
        "navigation.top",
        "navigation.tracking",
        "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "dark-blue",
            "accent": "dark-green",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    # BEGIN: version_dropdown
    "version_dropdown": False,
    "version_info": [
        {
            "version": "https://github.com/Unipisa/Simu5G",
            "title": "latest",
            "aliases": [],
        },
    ],
    # END: version_dropdown
    "toc_title_is_page_title": True,
    # BEGIN: social icons
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/Unipisa/Simu5G",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/twitter",
            "link": "https://twitter.com/Simu5G",
            "name": "X",
        },
    ],
    # END: social icons
}

# end html_theme_options
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#html_extra_path = ['.']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'simu5g'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('users-guide/index', 'simu5g-users-guide.tex', "Simu5G User's Guide", '', 'manual', False),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (root_doc, 'simu5g', 'Simu5G Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (root_doc, 'Simu5G', 'Simu5G Documentation',
     author, 'Simu5G', '5G Simulation Model.',
     'Miscellaneous'),
]

# external link configuration
extlinks = {
  'wiki': ('https://en.wikipedia.org/wiki/%s', '')
}

# image extension config
images_config = {
    'override_image_directive': True,
#    'backend': 'LightBox2',
#    'default_image_width': '100%',
#    'default_image_height': 'auto',
#    'default_group': 'None',
#    'download': True,
    'default_show_title': False
}

# -- Doxylink config ---------------------------------------------------------

doxylink = {
#        'cpp' : ('doxytags.xml', 'https://doc.omnetpp.org/simu5g/api-current/doxy/'),
#        'ned' : ('nedtags.xml', 'https://doc.omnetpp.org/simu5g/api-current/neddoc/'),
#        'msg' : ('msgtags.xml', 'https://doc.omnetpp.org/simu5g/api-current/neddoc/'),
}

# -- Extension configuration -------------------------------------------------
rst_prolog = open('global.rst', 'r').read()

# whether to show TODO items
todo_include_todos = False
todo_emit_warnings = False

def opp_preprocess(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]

    # implicitly import global macros in into the opp namespace at the beginning of each source file
    src = "{% import 'global-macros.inc' as opp %}\n" + src

    # run the templating engine on the source file
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

#################################x
# inline highlight extension

# Use defaults provided by highlight directive for code role.
# inline_highlight_respect_highlight = False

# Highlight also normal literals like :code:`literal`
inline_highlight_literals = True

# ###########################################################################
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"

from pygments.lexers.c_cpp import CLexer, CppLexer
from pygments.lexer import RegexLexer, include, bygroups, using, this, inherit, default, words
from pygments.token import Name, Keyword, Comment, Text, Operator, String, Number, Punctuation, Error
from sphinx.highlighting import lexers
from pygments.formatters import HtmlFormatter

#####
class NedLexer(RegexLexer):
    name = 'ned'
    filenames = ['*.ned']

    #: optional Comment or Whitespace
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'

    # The trailing ?, rather than *, avoids a geometric performance drop here.
    #: only one /* */ style comment
    _ws1 = r'\s*(?:/[*].*?[*]/\s*)?'

    tokens = {
        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text),  # line continuation
            (r'//(\n|[\w\W]*?[^\\]\n)', Comment.Single),
            (r'/(\\\n)?[*][\w\W]*?[*](\\\n)?/', Comment.Multiline),
            # Open until EOF, so no ending delimeter
            (r'/(\\\n)?[*][\w\W]*', Comment.Multiline),
        ],
        'statements': [
            (r'(L?)(")', bygroups(String.Affix, String), 'string'),
            (r"(L?)(')(\\.|\\[0-7]{1,3}|\\x[a-fA-F0-9]{1,2}|[^\\\'\n])(')",
             bygroups(String.Affix, String.Char, String.Char, String.Char)),
            (r'(true|false)\b', Name.Builtin),
            (r'(<-->|-->|<--|\.\.)', Keyword),
            (r'(bool|double|int|xml)\b', Keyword.Type),
            (r'(inout|input|output)\b', Keyword.Type),
            (r'(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+[LlUu]*', Number.Float),
            (r'(\d+\.\d*|\.\d+|\d+[fF])[fF]?', Number.Float),
            (r'0x[0-9a-fA-F]+[LlUu]*', Number.Hex),
            (r'#[0-9a-fA-F]+[LlUu]*', Number.Hex),
            (r'0[0-7]+[LlUu]*', Number.Oct),
            (r'\d+[LlUu]*', Number.Integer),
            (r'\*/', Error),
            (r'[~!%^&*+=|?:<>/-]', Operator),
            (r'[()\[\],.]', Punctuation),
            (words(("channel", "channelinterface", "simple", "module", "network", "moduleinterface"), suffix=r'\b'), Keyword),
            (words(("parameters", "gates", "types", "submodules", "connections"), suffix=r'\b'), Keyword),
            (words(("volatile", "allowunconnected", "extends", "for", "if", "import", "like", "package", "property"), suffix=r'\b'), Keyword),
            (words(("sizeof", "const", "default", "ask", "this", "index", "typename", "xmldoc"), suffix=r'\b'), Keyword),
            (words(("acos", "asin", "atan", "atan2", "bernoulli","beta", "binomial", "cauchy", "ceil", "chi_square", "cos", "erlang_k", "exp","exponential", "fabs", "floor", "fmod", "gamma_d", "genk_exponential","genk_intuniform", "genk_normal", "genk_truncnormal", "genk_uniform", "geometric","hypergeometric", "hypot", "intuniform", "log", "log10", "lognormal", "max", "min","negbinomial", "normal", "pareto_shifted", "poisson", "pow", "simTime", "sin", "sqrt","student_t", "tan", "triang", "truncnormal", "uniform", "weibull", "xml", "xmldoc"), suffix=r'\b'), Name.Builtin),
            ('@[a-zA-Z_]\w*', Name.Builtin),
            ('[a-zA-Z_]\w*', Name),
        ],
        'root': [
            include('whitespace'),
            # functions
            (r'((?:[\w*\s])+?(?:\s|[*]))'  # return arguments
             r'([a-zA-Z_]\w*)'             # method name
             r'(\s*\([^;]*?\))'            # signature
             r'([^;{]*)(\{)',
             bygroups(using(this), Name.Function, using(this), using(this),
                      Punctuation),
             'function'),
            # function declarations
            (r'((?:[\w*\s])+?(?:\s|[*]))'  # return arguments
             r'([a-zA-Z_]\w*)'             # method name
             r'(\s*\([^;]*?\))'            # signature
             r'([^;]*)(;)',
             bygroups(using(this), Name.Function, using(this), using(this),
                      Punctuation)),
            default('statement'),
        ],
        'statement': [
            include('whitespace'),
            include('statements'),
            ('[{}]', Punctuation),
            (';', Punctuation, '#pop'),
        ],
        'function': [
            include('whitespace'),
            include('statements'),
            (';', Punctuation),
            (r'\{', Punctuation, '#push'),
            (r'\}', Punctuation, '#pop'),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|'
             r'u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            (r'[^\\"\n]+', String),  # all other characters
            (r'\\\n', String),  # line continuation
            (r'\\', String),  # stray backslash
        ]
    }

lexers['ned'] = NedLexer(startinline=True)

#####
class MsgLexer(CppLexer):
    name = 'msg'
    filenames = ['*.msg']
    mimetypes = ['text/x-msg']

    tokens = {
        'statements': [
            (words(("import","cplusplus", "namespace", "struct", "message",
                "packet", "class", "noncobject", "enum", "extends"), suffix=r'\b'), Keyword),
            (words(("properties", "fields"), suffix=r'\b'), Keyword),
            (r'(abstract|readonly|bool|char|short|int|long|double|unsigned|string)\b', Keyword.Type),
            (r'[~!%^&*+=|?:<>/@-]', Operator),
            inherit,
        ],
    }

lexers['msg'] = MsgLexer(startinline=True)

#####
class IniLexer(RegexLexer):
    name = 'ini'
    filenames = ['*.ini']
    mimetypes = ['text/x-ini']

    tokens = {
        'root': [
            (r'[;#].*$', Comment.Single),
            (r'\s+', Text),
            (r'\[.*?\]', Keyword),
            (r'(.*?)([ \t]*)(=)([ \t]*)([^#\n]*(?:\n[ \t].+)*)',
             bygroups(Name.Attribute, Text, Operator, Text, String)),
        ],
    }

    def analyse_text(text):
        npos = text.find('\n')
        if npos < 3:
            return False
        return text[0] == '[' and text[npos-1] == ']'

lexers['ini'] = IniLexer(startinline=True)

#######################################################################

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace

class FpStyle(Style):
        default_style = "default"
        style = {
                Text: '#ffffff'
}

class FingerprintLexer(RegexLexer):
    name = 'fp'
    filenames = ['*.fp']
    mimetypes = ['text/x-fp']
    pygments_style = "FpStyle"

    tokens = {
        'root': [
            #(r'.*: ', Text),
            #(r'PASS', Keyword),
            #(r'FAILED', String),
            (r'(.* : )(PASS)?(FAILED)?(ERROR)?',
             bygroups(Name.Entity, Name.Builtin, String, String)),
            (r'.*?\n', Name.Entity),
        ],
    }

    def analyse_text(text):
        npos = text.find('\n')
        if npos < 3:
            return False
        return text[0] == '[' and text[npos-1] == ']'

lexers['fp'] = FingerprintLexer(startinline=True)

#######################################################################
# -- setup the customizations
import tools.video
import tools.audio

def setup(app):
    app.connect("source-read", opp_preprocess)
    app.add_directive('youtube', tools.video.Youtube)
    app.add_directive('vimeo', tools.video.Vimeo)
    app.add_directive('video', tools.video.Video)
    app.add_directive('video_noloop', tools.video.Video_noloop)
    app.add_directive('audio', tools.audio.Audio)
    app.connect("autodoc-skip-member", autodoc_skip_member_callback) # Entry point to autodoc-skip-member
