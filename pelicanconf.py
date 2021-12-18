AUTHOR = 'Jose V. Benavides'
SITENAME = 'k6wlr.com'
#SITEURL = 'https://k6wlr.com'
SITEURL = ''
SITESUBTITLE = 'Fun with technology'

#THEME = "/home/jvbenavi/r/pelican-octopress-theme"

SUMMARY_MAX_LENGTH = 150

PATH = 'content'
ARTICLE_PATHS = ['posts']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('NASA', 'https://nasa.gov/'),
         ('Astrobee', 'https://nasa.gov/astrobee'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/jvbenavi'),
          ('github', 'https://github.com/jvbenavi'),)

# octo
SIDEBAR_IMAGE = 'images/redknight.png'
SIDEBAR_IMAGE_ALT = "alt text"
SIDEBAR_IMAGE_WIDTH = 100
SEARCH_BOX = 'true'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCIVE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/index.html'

DEFAULT_PAGINATION = False

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
STATIC_PATHS = ['images', 'pdfs', 'static']

#PLUGIN_PATHS = ['../pelican-plugins']
#PLUGINS = ['liquid_tags.img']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
