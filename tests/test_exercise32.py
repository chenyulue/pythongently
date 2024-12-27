from ppeg.exercise32 import convert_str_to_int

def test_convert_str_to_int():
    for i in range(-10000, 10000):
        assert convert_str_to_int(str(i)) == i