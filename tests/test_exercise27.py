from ppeg.exercise27 import draw_rectangle

def test_draw_rectangle(capsys):
    draw_rectangle(10, 4)
    captured = capsys.readouterr()
    assert captured.out.strip() == "\n".join("#" * 10 for _ in range(4))

def test_draw_rectangle_with_width_less_than_1(capsys):
    draw_rectangle(0, 4)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_draw_rectangle_with_height_less_than_1(capsys):
    draw_rectangle(10, 0)
    captured = capsys.readouterr()
    assert captured.out == ""