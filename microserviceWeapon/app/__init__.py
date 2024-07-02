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
                                'CACHE_REDIS_PORT': 6379,
                                'CACHE_REDIS_DB': '0',
                                'CACHE_KEY_PREFIX': 'weapon_'})
    
    from app.resources import weapon
    app.register_blueprint(weapon.weapon, url_prefix='/api/v1')

    return app