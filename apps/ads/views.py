from flask import jsonify, make_response, Blueprint
from flask import request
from marshmallow import ValidationError

from apps.ads.external_ads import ExternalAd
from apps.shared.schemas import RequestSchema
from redis_client import RedisClient, RedisSection, RedisSectionField

bp = Blueprint('ads', __name__, url_prefix='/ads')


@bp.route('/', methods=['POST'])
def ads():
    # TODO The API accepts a Request in JSON format but returns a Response in XML format
    #  This approach doesn't follow the best practises and could be confusing to use it.
    #  When the requirements are defined properly, this approach could be changed.

    data = request.get_json(force=True)

    try:
        validated_data = RequestSchema().load(data)
    except ValidationError as err:
        return make_response(jsonify(err.messages), 400)

    xml_response = ExternalAd.get()
    if not xml_response:
        return make_response(xml_response, 400)

    # Increment by Username
    RedisClient().increment(
        section=RedisSection.REQUESTS,
        field=RedisSectionField.USERNAME,
        value=validated_data['username']
    )

    # Increment by SDK Version
    RedisClient().increment(
        section=RedisSection.REQUESTS,
        field=RedisSectionField.SDK_VERSION,
        value=validated_data['sdk_version']
    )

    return make_response(xml_response, 200)
