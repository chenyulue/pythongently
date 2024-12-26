from ppeg.exercise25 import print_multiplication_table

def test_print_multiplication_table(capsys):
    print_multiplication_table()
    captured = capsys.readouterr()
    rows = captured.out.strip().split("\n")
    assert rows[0].split()[-1] == "10"
    assert rows[-1].split()[0] == "10|"
    assert rows[-1].split()[-1] == "100"