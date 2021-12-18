AUTHOR = 'Jose V. Benavides'
SITENAME = 'k6wlr.com'
SITESUBTITLE = 'Fun with technology'
SITEURL = ''

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
#THEME = "/home/jvbenavi/r/blog-themes/elegant"
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = "Misc"
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCIVE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/index.html'
STATIC_PATHS = ['images', 'static']
ARTICLE_PATHS = ['articles']

# pelican or elegant defaults? 
#TAG_SAVE_AS = ""
#AUTHOR_SAVE_AS = ""
#CATEGORY_SAVE_AS = ""
#PAGE_URL = "{slug}"
#PAGE_SAVE_AS = "{slug}.html" 'pages/{slug}.html'
#TAGS_URL = "tags"
#CATEGORIES_URL = "categories"
#ARCHIVES_URL = "archives"
#SEARCH_URL = "search"

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

SUMMARY_MAX_LENGTH = 150

# Blogroll
LINKS = (('NASA', 'https://nasa.gov/'),
         ('Astrobee', 'https://nasa.gov/astrobee'),)

DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# notmyidea mod 
FAVICON_IMG = 'https://k6wlr.com/share/favicon.ico'

