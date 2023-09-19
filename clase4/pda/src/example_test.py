def increment(x):
    return x+1

def test_func():
    value=3
    return_value=increment(value)
    expected=5
    assert expected==return_value, "return_valiue doesn'y match expected value"