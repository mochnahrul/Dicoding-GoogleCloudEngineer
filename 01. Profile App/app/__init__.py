# third-party imports
from flask import Flask

# local imports
from .config import ProductionConfig


def create_app(config_class=ProductionConfig):
  app = Flask(__name__)
  app.config.from_object(config_class)

  from .views import public_app
  app.register_blueprint(public_app)

  return app