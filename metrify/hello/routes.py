"""
The "routes.py" module registers the operation URL endpoints to the package's
`Blueprint` object.
"""

from flask import Response, current_app, jsonify

from metrify.hello import bp
from metrify.hello.strategies import hello as hello_strategy


@bp.route("/hello")
def hello() -> Response:
    """Status Code 200 HELLO, WORLD!"""
    return jsonify(hello_strategy())
