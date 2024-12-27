from ppeg.exercise31 import convert_int_to_str

def test_convert_int_to_str():
    for i in range(-10000, 10000):
        assert convert_int_to_str(i) == str(i)