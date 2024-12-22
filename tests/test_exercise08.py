import pytest

from ppeg.exercise08 import write_to_file, append_to_file, read_from_file

@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    yield file_path
    file_path.unlink()

def test_write_append_and_read_file(test_file):
    write_to_file(test_file, "Hello!\n")
    append_to_file(test_file, "Goodbye!\n")
    assert read_from_file(test_file) == "Hello!\nGoodbye!\n"