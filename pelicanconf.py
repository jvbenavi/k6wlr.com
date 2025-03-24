AUTHOR = 'Jose V. Benavides'
SITENAME = 'k6wlr.com'
SITESUBTITLE = 'Fun with technology'

SITEURL = 'https://k6wlr.com'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

SITEIMAGE = '/images/astrobee.svg width=200 height=200'
#SITEIMAGE = '/images/robot.svg width=200 height=200'
#SITEIMAGE = '/images/astrobee2.svg width=300 height=300'
DESCRIPTION = 'A personal blog page'

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
THEME = "/home/jvbenavi/r/pelican-alchemy/alchemy"
#THEME = "simple"

TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_LANG = 'en'
STATIC_PATHS = ['images', 'static']

USE_FOLDER_AS_CATEGORY = False

ARTICLE_PATHS  = ['articles']
ARTICLE_URL     = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS   = ['pages']
PAGE_URL     = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html" #'pages/{slug}.html'

TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"
ARCHIVES_URL = "archives.html"

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives'] # remove 'authors'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
ICONS = (
        ('linkedin', 'https://www.linkedin.com/in/jose-benavides-a3a1942'),
        ('github', 'https://github.com/jvbenavi'),
)

SUMMARY_MAX_LENGTH = 100

# Blogroll
LINKS = (('NASA', 'https://nasa.gov/'),
         ('Astrobee', 'https://nasa.gov/astrobee'),)

HIDE_AUTHORS = True

# theme mod
FAVICON_IMG = '/images/favicon.ico'

