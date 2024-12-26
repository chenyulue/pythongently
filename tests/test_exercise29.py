from ppeg.exercise29 import draw_pyramid

def test_draw_pyramid(capsys):
    draw_pyramid(4)
    captured = capsys.readouterr()
    assert captured.out.rstrip().split('\n') == [
        "   #",
        "  ###",
        " #####",
        "#######"
    ]