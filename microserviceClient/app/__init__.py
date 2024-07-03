from flask import Flask
from flask_cors import CORS
from app.config.database import migrate, configure_database
from flask_marshmallow import Marshmallow
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()
cache = Cache()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    configure_database(app)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache',
                                 'CACHE_DEFAULT_TIMEOUT': 300,
                                 'CACHE_REDIS_HOST': 'redis',
                                #'CACHE_REDIS_HOST': 'redis', Configuracion para traefik
                                #'CACHE_REDIS_HOST': 'localhost', Configuracion local
                                  'CACHE_REDIS_PORT': 6379,
                                'CACHE_REDIS_DB': '0',
                                #'CACHE_REDIS_PASSWORD': '123456',
                                'CACHE_KEY_PREFIX': 'client_'})
 
    from app.resources import client
    app.register_blueprint(client, url_prefix='/api/v1')

    return app