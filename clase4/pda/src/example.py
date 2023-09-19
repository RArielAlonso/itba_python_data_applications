import math

def my_func(x):
    x_proc=x+1
    assert x_proc>=0, "El valor de x es negativo"
    res=math.sqrt(x_proc)
    return res

def main():
    breakpoint()
    var=2
    return_value=my_func(var)
    print(return_value)

if __name__=='__main__':
    main()