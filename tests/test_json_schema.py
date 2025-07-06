import json

import pytest
from jsonschema import ValidationError, validate

# Define the JSON schema based on json_schema.md
schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "title": {"type": "string"},
        "slides": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "layout": {"type": "string"},
                    "elements": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string"},
                                "text": {"type": ["string", "null"]},
                                "style": {
                                    "type": ["object", "null"],
                                    "properties": {
                                        "bold": {"type": ["boolean", "null"]},
                                        "italic": {"type": ["boolean", "null"]},
                                        "fontSize": {"type": ["number", "null"]},
                                    },
                                    "additionalProperties": False,
                                },
                                "items": {
                                    "type": ["array", "null"],
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "text": {"type": "string"},
                                            "transcription": {
                                                "type": ["string", "null"]
                                            },
                                            "audioSrc": {"type": ["string", "null"]},
                                        },
                                        "required": ["text"],
                                        "additionalProperties": False,
                                    },
                                },
                                "src": {"type": ["string", "null"]},
                                "alt": {"type": ["string", "null"]},
                                "attribution": {"type": ["string", "null"]},
                                "description": {"type": ["string", "null"]},
                            },
                            "required": ["type"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["id", "layout", "elements"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["id", "title", "slides"],
    "additionalProperties": False,
}


def test_json_output_conforms_to_schema():
    # Path to the generated JSON file
    json_file_path = "./output_presentation_test/presentation.json"

    # Load the generated JSON data
    with open(json_file_path, encoding="utf-8") as f:
        data = json.load(f)

    # Validate the data against the schema
    try:
        validate(instance=data, schema=schema)
        print("JSON output conforms to the schema!")
    except ValidationError as e:
        pytest.fail(f"JSON output does not conform to the schema: {e}")
