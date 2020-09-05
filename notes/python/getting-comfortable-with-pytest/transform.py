from pathlib import Path

MESSAGE = {
    "sha256": "",
    "file_path": r"C:\\Users\...",
    "file_size": 0,
    "file_type": "EXE",
    "prevalence": 0,
}


"""
Notes

First, write a docstring for you function that will describe what it does. Tip:
if there is an 'and' in there, think if it could be two functions.

E.g.
    Transform a message. Extract a file_name (the last part of the path) and add a rank
    according to the prevalence

Let's split that into two functions.




"""


def rank(message):
    """Rank a message according to the prevalence:

        1 = UNIQUE
        <=1000 = RARE
        >1000 = COMMON
    """

    prevalence = message["prevalence"]

    if prevalence == 1:
        message["rank"] = "UNIQUE"
    elif prevalence <= 1000:
        message["rank"] = "RARE"
    elif prevalence > 1000:
        message["rank"] = "COMMON"

    del message["prevalence"]


def rank2(prevalence):
    """Return a rank according to the prevalence:

        1 = UNIQUE
        <=1000 = RARE
        >1000 = COMMON
    """

    if prevalence == 1:
        return "UNIQUE"
    elif prevalence <= 1000:
        return "RARE"
    elif prevalence > 1000:
        return "COMMON"


def extract_filename(message):
    """Extract a file_name (the last part of the path)."""

    file_path = message["file_path"]

    message["file_name"] = file_path.split("\\")[-1]

    del message["file_path"]


def extract_filename2(file_path):

    try:
        return Path(file_path).name
    except TypeError:
        return ""


## Manual testing
print(rank({"prevalence": 1}))  # I'm expecting 'UNIQUE'
print(rank({"prevalence": 1}))  # 'RARE'
print(rank({"prevalence": 1}))  # 'COMMON'


"""Then we will have one function that combines them both"""


def transform(message):
    """NOTE: test with a fixture"""
    ...
