import pytest
from presidio_analyzer.recognizer_result import RecognizerResult

from presidio_image_redactor import ImageAnalyzerEngine
from presidio_image_redactor.entities import ImageRecognizerResult


@pytest.fixture(scope="function")
def get_ocr_analyzer_results():
    ocr_result = {
        "text": [
            "",
            "Homey",
            "Interiors",
            "was",
            "created",
            "by",
            "Katie",
            "",
            "Cromley.",
        ],
        "left": [143, 143, 322, 530, 634, 827, 896, 141, 141],
        "top": [64, 67, 67, 76, 64, 64, 64, 134, 134],
        "width": [936, 160, 191, 87, 172, 51, 183, 801, 190],
        "height": [50, 47, 37, 28, 40, 50, 40, 50, 50],
    }

    text = " Homey Interiors was created by Katie  Cromley."

    analyzer_result = [
        RecognizerResult("PERSON", 32, 37, 0.85),
        RecognizerResult("PERSON", 39, 46, 0.85),
    ]

    return ocr_result, text, analyzer_result


@pytest.fixture(scope="function")
def get_image_recognizerresult():
    return [
        ImageRecognizerResult("PERSON", 32, 37, 0.85, 896, 64, 183, 40),
        ImageRecognizerResult("PERSON", 39, 46, 0.85, 141, 134, 190, 50),
    ]


@pytest.fixture(scope="module")
def image_analyzer_engine():
    return ImageAnalyzerEngine()
