import json

with open("config_example/config.json") as f:
    config=json.load(f)

def do_square(val):
    return val**2

def main():
    debug=config.get("debug",False)
    val=config.get("val",1)

    if debug:
        print(config)

    res=do_square(val)
    print(f"The result es {res}")

if __name__=="__main__":
    main()