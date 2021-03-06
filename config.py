import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or '234DFGDFdfgdf234234dfgdFGJRETGFHFG456gfhFGH'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Discogs Credentials
    #DISCOGS_USERNAME = 'dave@classicalvinyl.com'
    #DISCOGS_PASSWORD = 'D3troit5'
    DISCOGS_USERNAME = 'muce@protonmail.com'
    DISCOGS_PASSWORD = 'N0rthW1ckP4rk)'
    DISCOGS_USER_AGENT = 'VinylAlert/0.1'
    DISCOGS_CONSUMER_KEY = 'cPWXjqpPoqOzmsrXJZMh'
    DISCOGS_CONSUMER_SECRET = 'pGnECEjBciPnpERBCwqKfUkhUxhNMJOj'
    DISCOGS_PERSONAL_ACCESS_TOKEN = 'oWHZLfHsMdzPVUSvlAlvpZDexuEoRAJTunEIBIQQ'
    # Discogs URLs
    DISCOGS_CALLBACK_URL = 'http://localhost:5000/authorised'
    DISCOGS_ARTIST_URL = 'http://www.discogs.com/artist'
    DISCOGS_BASE_URL = 'https://api.discogs.com/'
    DISCOGS_MAIN_MENU_URL = 'http://localhost:5000/main_menu.html'
    DISCOGS_USER_URL = ''
    DISCOGS_TITLE_URL = ''
    DISCOGS_FORMAT_URL = ''
    # Releases
    DISCOGS_RELEASE = '/releases/(release_id)'
    DISCOGS_MASTER_RELEASE = '/masters/(master_id)'
    DISCOGS_ARTIST = '/artists/(artist_id)'
    DISCOGS_ARTIST_RELEASES = '/artists/(artist_id)/releases'
    DISCOGS_LABEL = '/labels/(label_id)'
    DISCOGS_LABEL_RELEASES = '/labels/(label_id)/releases'
    # Marketplace
    DISCOGS_INVENTORY = '/users/{username}/inventory{?status,sort,sort_order}'
    DISCOGS_LISTING = '/marketplace/listings/{listing_id}'
    DISCOGS_ORDER = '/marketplace/orders/{order_id}'
    DISCOGS_LIST_ORDERS = '/marketplace/orders{?status,sort,sort_order}'
    DISCOGS_LIST_ORDER_MESSAGES = '/marketplace/orders/{order_id}/messages'
    DISCOGS_FEE = '/marketplace/fee/{price}'
    DISCOGS_FEE_WITH_CURRENCY = '/marketplace/fee/{price}/{currency}'
    DISCOGS_PRICE_SUGGESTIONS = '/marketplace/price_suggestions/{release_id}'
    # Identity
    DISCOGS_IDENTITY = 'oauth/identity'
    DISCOGS_PROFILE = '/users/{username}'
    DISCOGS_USER_SUBMISSIONS = 'users/{username}/submissions'
    DISCOGS_USER_CONTRIBUTIONS = '/users/{username}/contributions'
    DISCOGS_COLLECTION = '/users/{username}/collection/folders'
    DISCOGS_COLLECTION_FOLDER = '/users/{username}/collection/folders/{folder_id}'
    DISCOGS_GET_COLLECTION_RELEASES = '/users/{username}/collection/folders/{folder_id}/releases'
    DISCOGS_LIST_CUSTOM_FIELDS = '/users/{username}/collection/fields'
    DISCOGS_WANTLIST = '/users/{username}/wants'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'muce@protonmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'N0rthW1ckP4rk)'
    MAIL_SUBJECT_PREFIX = '['+DISCOGS_USER_AGENT+']'
    MAIL_SENDER = 'VinylAlert Admin <admin@classicalvinyl.com>'
    MAIL_ADMIN = os.environ.get('VINYLALERT_ADMIN') or 'muce@protonmail.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):


    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
