AUTHOR = 'Jose V. Benavides'
SITENAME = 'k6wlr.com'
SITESUBTITLE = 'Fun with technology'
SITEURL = ''#'https://k6wlr.com'

PATH = 'content'

# Regional settings 
TIMEZONE = 'America/Los_Angeles'

# Plugins and extentions
MARKDOWN = {
    'extension_configs': {
        "markdown.extensions.admonition": {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        "markdown.extensions.toc": {"permalink": " "},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = None

# Appearance
THEME = "/home/jvbenavi/r/pelican-themes/notmyidea"
#THEME = "/home/jvbenavi/r/pelican-themes/alchemy" # can have cover's with: 
#https://alpynepyano.github.io/healthyNumerics/posts/python-pelican-website-with-jupyter-part-1.html

TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_LANG = 'en'
STATIC_PATHS = ['images', 'static']

USE_FOLDER_AS_CATEGORY = True

ARTICLE_PATHS  = ['articles']
ARTICLE_URL     = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATH = ['pages']
PAGE_URL     = "{slug}"
PAGE_SAVE_AS = "{slug}.html" #'pages/{slug}.html'

# pelican or elegant defaults? 
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
#SEARCH_URL = "search"

#TAG_SAVE_AS = ""
#AUTHOR_SAVE_AS = ""
#CATEGORY_SAVE_AS = ""
DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives'] # remove 'authors'

#about.md overides root index.html 
# then place original article index in top menu 
INDEX_SAVE_AS = 'blog_index.html'
MENUITEMS = [('Blog', SITEURL + '/blog_index')]

DISPLAY_CATEGORIES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
        ('Linkedin', 'https://www.linkedin.com/in/jose-benavides-a3a1942'),
        ('Github', 'https://github.com/jvbenavi'),
        ('RSS', SITEURL + '/feeds/all.atom.xml'),
        ('Twitter', 'https://twitter.com/jvbenavi'),
)

SUMMARY_MAX_LENGTH = 100

# Blogroll
LINKS = (('NASA', 'https://nasa.gov/'),
         ('Astrobee', 'https://nasa.gov/astrobee'),)

# notmyidea mod 
FAVICON_IMG = '/images/favicon.ico'

