AUTHOR = 'Jose V. Benavides'
SITENAME = 'k6wlr'
SITESUBTITLE = 'Fun with technology. This is a personal blog, sketch pad, and fun corner of the internet to document my side adventures.'

SITEURL = '' # this is now set in publishconf

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

SITEIMAGE = '/images/astrobee.svg width=200 height=200'
#SITEIMAGE = '/images/robot.svg width=200 height=200'
#SITEIMAGE = '/images/astrobee2.svg width=300 height=300'
DESCRIPTION = 'A personal blog'

PATH = 'content'

# Regional settings
TIMEZONE = 'America/Phoenix'

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
THEME = "../pelican-alchemy/alchemy"
#THEME = "notmyidea"

TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_LANG = 'en'
STATIC_PATHS = ['images', 'static']

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    }

USE_FOLDER_AS_CATEGORY = True

ARTICLE_PATHS  = ['articles']
ARTICLE_URL     = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS   = ['pages']
PAGE_URL     = "pages/{slug}.html" #'{slug}.html' (both same)
PAGE_SAVE_AS = "pages/{slug}.html" #'pages/{slug}.html' (both same)

TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"
ARCHIVES_URL = "archives.html"

#INDEX_SAVE_AS = 'blog.html' # this requires another page to have: "save_as: index.html" and "URL: "

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
# notmyidea working value is ['index', 'tags', 'categories', 'archives']
# Alchemy value is ['index', 'tags', 'categories', 'archives', 'sitemap'] # add 'sitemap'
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'sitemap'] 
SITEMAP_SAVE_AS = 'sitemap.xml' # used in Alchemy

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
         ('ASR', 'https://www.nasa.gov/intelligent-systems-division/autonomous-systems-and-robotics'),
         )

HIDE_AUTHORS = True

# theme mod
FAVICON_IMG = '/images/favicon.ico'

# STATIC_CHECK_IF_MODIFIED = True
