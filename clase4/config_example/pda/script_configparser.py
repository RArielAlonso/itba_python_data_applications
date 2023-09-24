import os
import configparser

config=configparser.ConfigParser()
config.read("config_example/config.ini")

def do_square(val):
    return val**2

def main():
    
    _val=config['DEFAULT']['VAL']
    _debug=config['DEFAULT']['DEBUG']

    if _val:
        val=float(_val)

    debug=True if _debug.lower()=="true" else False

    if _debug:
        print(f"El valor de val es {config['DEFAULT']['VAL']}")
        print(f"El valor de debug es {config['DEFAULT']['DEBUG']}")

    res=do_square(val)
    print(f"The result es {res}")

if __name__=="__main__":
    main()