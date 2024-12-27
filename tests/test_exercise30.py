from ppeg.exercise30 import draw_box

def test_draw_box(capsys):
    draw_box(2)
    captured = capsys.readouterr()
    lines = captured.out.rstrip().split("\n")
    assert lines[0] == "   +----+"
    assert lines[1] == "  /    /|"
    assert lines[2] == " /    / |"
    assert lines[3] == "+----+  +"
    assert lines[4] == "|    | /"
    assert lines[5] == "|    |/"
    assert lines[6] == "+----+"