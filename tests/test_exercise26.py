from ppeg.exercise26 import print_handshakes

def test_print_handshakes_with_2_names(capsys):
    n = print_handshakes(["Alice", "Bob"])
    captured = capsys.readouterr()
    assert n == 1
    assert captured.out.strip().split("\n") == [
        "Alice shakes hands with Bob",
        ]

def test_print_handshakes_with_3_names(capsys):
    n = print_handshakes(["Alice", "Bob", "Carol"])
    captured = capsys.readouterr()
    assert n == 3
    assert captured.out.strip().split("\n") == [
        "Alice shakes hands with Bob",
        "Alice shakes hands with Carol",
        "Bob shakes hands with Carol",
        ]

def test_print_handshakes_with_4_names(capsys):
    n = print_handshakes(["Alice", "Bob", "Carol", "David"])
    captured = capsys.readouterr()
    assert n == 6
    assert captured.out.strip().split("\n") == [
        "Alice shakes hands with Bob",
        "Alice shakes hands with Carol",
        "Alice shakes hands with David",
        "Bob shakes hands with Carol",
        "Bob shakes hands with David",
        "Carol shakes hands with David",
        ]