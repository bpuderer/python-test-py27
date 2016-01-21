import unittest
import json
from jsonschema import validate, ValidationError


class TestJsonSchema(unittest.TestCase):

    def test_json_schema(self):
        #http://json-schema.org/
        #http://spacetelescope.github.io/understanding-json-schema/
        #https://github.com/Julian/jsonschema
        #
        #not included
        #numeric- multipleOf, exclusiveMinimum, exclusiveMaximum
        #object- minProperties, maxProperties, dependencies, patternProperties
        #array- items
        #$ref, allOf, anyOf, oneOf, not

        schema_str = """
{
    "$schema": "http://json-schema.org/schema#",
    "id": "http://yourdomain.com/schemas/myschema.json",
    "properties": {
        "a_bool": {
            "type": "boolean"
        },
        "a_null": {
            "type": "null"
        },
        "a_num": {
            "type": "number"
        },
        "a_str": {
            "type": "string"
        },
        "an_array": {
            "type": "array"
        },
        "an_enum": {
            "enum": [
                "red",
                "white",
                "blue"
            ]
        },
        "an_int": {
            "type": "integer"
        },
        "array_size": {
            "maxItems": 2,
            "minItems": 0,
            "type": "array"
        },
        "array_type": {
            "items": {
                "type": "number"
            },
            "type": "array"
        },
        "array_unique": {
            "type": "array",
            "uniqueItems": true
        },
        "num_range": {
            "maximum": 42,
            "minimum": 21,
            "type": "number"
        },
        "obj_no_extras": {
            "additionalProperties": false,
            "properties": {
                "only": {
                    "type": "string"
                }
            },
            "type": "object"
        },
        "obj_req_field": {
            "properties": {
                "opt": {
                    "type": "string"
                },
                "req": {
                    "type": "string"
                }
            },
            "required": [
                "req"
            ],
            "type": "object"
        },
        "str_format_dt": {
            "format": "date-time",
            "type": "string"
        },
        "str_format_email": {
            "format": "email",
            "type": "string"
        },
        "str_format_hostname": {
            "format": "hostname",
            "type": "string"
        },
        "str_format_ipv4": {
            "format": "ipv4",
            "type": "string"
        },
        "str_format_ipv6": {
            "format": "ipv6",
            "type": "string"
        },
        "str_format_uri": {
            "format": "uri",
            "type": "string"
        },
        "str_len": {
            "maxLength": 4,
            "minLength": 3,
            "type": "string"
        },
        "str_regex": {
            "pattern": "^[A-Z]{3}$",
            "type": "string"
        }
    },
    "type": "object"
}
                     """

        test_str = """
{
    "a_bool": true,
    "a_null": null,
    "a_num": 1.21,
    "a_str": "str",
    "an_array": [
        1,
        2
    ],
    "an_enum": "red",
    "an_int": 42,
    "array_size": [
        0,
        0
    ],
    "array_type": [
        1.21,
        42,
        3.00e8
    ],
    "array_unique": [
        0,
        1
    ],
    "num_range": 33.3,
    "obj_no_extras": {
        "only": "str"
    },
    "obj_req_field": {
        "req": "str"
    },
    "str_format_dt": "2015-01-20T20:35:00.000Z",
    "str_format_email": "no@thanks.com",
    "str_format_hostname": "foo.bar.com",
    "str_format_ipv4": "192.168.1.1",
    "str_format_ipv6": "2001:0db8:0000:0042:0000:8a2e:0370:7334",
    "str_format_uri": "file://host/path",
    "str_len": "WMSV",
    "str_regex": "MSY"
}
                   """
        try:
            validate(json.loads(test_str), json.loads(schema_str))
        except ValidationError as e:
            self.fail("ValidationError raised by jsonschema: {}".format(e))
