import pytest
from transform import extract_filename, extract_filename2, rank, rank2

# FIRST VERSION
## NOTE: let's test the boundary values.


def test_rank_unique():

    message = {"prevalence": 1}
    rank(message)
    assert message == {"rank": "UNIQUE"}


def test_rank_rare():

    message = {"prevalence": 1000}
    rank(message)
    assert message == {"rank": "RARE"}


def test_rank_common():
    message = {"prevalence": 1001}
    rank(message)
    assert message == {"rank": "COMMON"}


## NOTE: we should be careful to test all platforms -- parametrizing to the resque!
def test_extract_filename():

    message = {"file_path": r"C:\\Users\scary_ransomware.exe"}
    assert extract_filename(message) == {"file_name": "scary_ransomware.exe"}


# Second version
## We don't want to repeat all that code. Let's write a better test for the path

PATH_PARAMS = [
    (r"/home/max/scary_ransomware.exe", "scary_ransomware.exe"),
    ("/tmp/test/clean.pdf", "clean.pdf"),
    ("document.docx", "document.docx"),
    ("", ""),
    (1, ""),
]


@pytest.mark.parametrize("file_path, file_name", PATH_PARAMS)
def test_extract_filename(file_path, file_name):

    assert extract_filename2(file_path) == file_name


RANK_PARAMS = [(1, "UNIQUE"), (1000, "RARE"), (1001, "COMMON")]


@pytest.mark.parametrize("prevalence, rank_string", RANK_PARAMS)
def test_rank(prevalence, rank_string):

    assert rank2(prevalence) == rank_string
