import pytest

from ppeg.exercise10 import find_and_replace

@pytest.mark.parametrize("text, old_text, new_text, expected", [
    ("The fox", "fox", "dog", "The dog"),
    ("fox", "fox", "dog", "dog"),
    ("Firefox", "fox", "dog", "Firedog"),
    ("foxfox", "fox", "dog", "dogdog"),
    ("The Fox and fox.", "fox", "dog", "The Fox and dog."),
    ("This is a fox and the fox is big.", "fox", "dog", "This is a dog and the dog is big."),
])
def test_find_and_replace(text, old_text, new_text, expected):
    assert find_and_replace(text, old_text, new_text) == expected