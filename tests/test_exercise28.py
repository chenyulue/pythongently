from ppeg.exercise28 import draw_border

def test_draw_border(capsys):
    draw_border(5, 3)
    captured = capsys.readouterr()
    assert captured.out == "+--+\n|  |\n+--+\n"

def test_draw_border_with_width_less_than_2(capsys):
    draw_border(1, 3)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_draw_border_with_height_less_than_2(capsys):
    draw_border(5, 1)
    captured = capsys.readouterr()
    assert captured.out == ""