from flask import Flask
from flask_cors import CORS
from app.config.database import db, migrate, configure_database
from flask_marshmallow import Marshmallow
from flask_caching import Cache

ma = Marshmallow()
cache = Cache()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    configure_database(app)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_DEFAULT_TIMEOUT': 300,
                                'CACHE_REDIS_HOST': 'localhost', 'CACHE_REDIS_PORT': 6379,
                                'CACHE_REDIS_DB': '0', 'CACHE_REDIS_PASSWORD': '123456',
                                'CACHE_KEY_PREFIX': 'client_'})
 
    from app.resources import home, client
    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(client, url_prefix='/api/v1')

    with app.app_context():
        db.create_all()

    return app