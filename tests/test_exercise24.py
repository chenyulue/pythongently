from ppeg.exercise24 import print_every_15_minutes

def test_print_every_15_minutes(capsys):
    print_every_15_minutes()
    captured = capsys.readouterr()
    results = captured.out.strip().split("\n")
    assert len(results) == 96
    assert results[0] == "12:00 am"
    assert results[-1] == "11:45 pm"