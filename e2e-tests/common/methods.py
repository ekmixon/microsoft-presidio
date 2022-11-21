import os

import requests

from common.constants import (
    ANONYMIZER_BASE_URL,
    ANALYZER_BASE_URL,
    IMAGE_REDACTOR_BASE_URL,
)

DEFAULT_HEADERS = {"Content-Type": "application/json"}
MULTIPART_HEADERS = {"Content-Type": "multipart/form-data"}
ANALYZER_BASE_URL = os.environ.get("ANALYZER_BASE_URL", ANALYZER_BASE_URL)
ANONYMIZER_BASE_URL = os.environ.get("ANONYMIZER_BASE_URL", ANONYMIZER_BASE_URL)
IMAGE_REDACTOR_BASE_URL = os.environ.get(
    "IMAGE_REDACTOR_BASE_URL", IMAGE_REDACTOR_BASE_URL
)


def anonymize(data):
    response = requests.post(
        f"{ANONYMIZER_BASE_URL}/anonymize", data=data, headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def anonymizers():
    response = requests.get(
        f"{ANONYMIZER_BASE_URL}/anonymizers", headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def analyze(data):
    response = requests.post(
        f"{ANALYZER_BASE_URL}/analyze", data=data, headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def analyzer_supported_entities(data):
    response = requests.get(
        f"{ANALYZER_BASE_URL}/supportedentities?{data}", headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def redact(file, color_fill=None):
    multipart_form_data = __get_multipart_form_data(file)
    payload = __get_redact_payload(color_fill)
    return requests.post(
        f"{IMAGE_REDACTOR_BASE_URL}/redact",
        files=multipart_form_data,
        data=payload,
    )


def deanonymize(data):
    response = requests.post(
        f"{ANONYMIZER_BASE_URL}/deanonymize", data=data, headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def __get_redact_payload(color_fill):
    return (
        {"data": "{'color_fill':'" + str(color_fill) + "'}"}
        if color_fill
        else {}
    )


def __get_multipart_form_data(file):
    return (
        {
            "image": (file.name, file, "multipart/form-data"),
        }
        if file
        else {}
    )
