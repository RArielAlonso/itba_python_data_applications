from memory_profiler import profile
import random

@profile
def main():
    list_int=[random.randint(1,10) for i in range(10000)]
    list_float_0_1=[random.random() for i in range(10000)]
    list_str=["ariel" for i in range(10000)]
    b = [2] * (2 * 10 ** 7)
    del list_int
    del b


if __name__=="__main__":
    main()
