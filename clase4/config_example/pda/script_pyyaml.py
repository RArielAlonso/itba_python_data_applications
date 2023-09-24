import yaml

with open("config_example/config.yaml","r") as f:
    config=yaml.safe_load(f)


def do_square(val):
    return val**2

def main():
    
    debug=config.get("debug","False")
    val=config.get("val",1)

    if debug:
        print(config)
    
    res=do_square(val)
    print(f"The result es {res}")

if __name__=="__main__":
    main()