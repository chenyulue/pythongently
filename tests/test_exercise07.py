from ppeg.exercise07 import print_ascii_table
def test_print_ascii_table(capsys):
    print_ascii_table()
    captured = capsys.readouterr()
    strings = captured.out.strip().split('\n')

    assert len(strings) == 127-32
    assert strings[0] == "32  "
    assert strings[1] == "33 !"
    assert strings[-2] == "125 }"
    assert strings[-1] == "126 ~"