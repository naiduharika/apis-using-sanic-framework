from functools import wraps

from cerberus import Validator
from sanic.response import json


def validate(schema, coerce=False, allow_unknown=True):
    validator = Validator(schema)
    validator.allow_unknown = allow_unknown

    def validate_json(f):
        @wraps(f)
        def wrapper(request, *args, **kwargs):
            if request.method == "GET":
                request_params = request.args
            if request.method == "POST":
                request_params = request.json
            if request_params is None:
                return json(
                    {"error": {"message": "Expected JSON body"}},
                    status=415,
                )

            validation_passed = validator.validate(request_params or {})
            if validation_passed:
                if coerce:
                    kwargs["valid_json"] = validator.document
                return f(request, *args, **kwargs)
            else:
                return json(
                    {
                        "error": {
                            "message": "Validation failed.",
                            "invalid": validator.errors,
                        }
                    },
                    status=400,
                )

        return wrapper

    return validate_json
