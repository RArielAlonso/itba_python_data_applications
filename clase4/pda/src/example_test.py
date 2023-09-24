

def multiple_2(func):
    def wrapper(value1,value2):
        return_value=func(value1,value2)
        return_value=return_value*2
        return return_value
    return wrapper

@multiple_2
def increment_division(a,m):
    num=a+1
    div=m
    assert div!=0, "El valor de m no puede ser 0"
    return_value=num/div
    return return_value

# def test_func(value):
#     return_value=increment(value)
#     expected=5
#     assert expected==return_value, "return_valiue doesn'y match expected value"

valor=increment_division(2,1)
print(valor)