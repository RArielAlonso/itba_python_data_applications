import os
from dotenv import load_dotenv

load_dotenv()

def do_square(val):
    return val**2

def main():
    
    _val=os.getenv("VAL")
    _debug=os.getenv("DEBUG","FALSE")

    debug=True if _debug.lower()=="true" else False

    if _val:
        val=float(_val)
    else:
        return

    if debug:
        print(f"Val is {_val}")
        print(f"Debug is set to {_debug}")

    res=do_square(val)
    print(f"The result es {res}")

if __name__=="__main__":
    main()