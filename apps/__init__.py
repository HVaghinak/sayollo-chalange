import os

from dotenv import load_dotenv
from flask import Flask

from apps.ads import views as ads_views
from apps.impressions import views as impressions_views


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(os.environ['FLASK_CONFIGURATION_SETUP'])

    app.register_blueprint(ads_views.bp)
    app.register_blueprint(impressions_views.bp)

    return app
