from argparse import ArgumentParser



def do_square(val):
    return val**2

def main():
    parser=ArgumentParser()
    parser.add_argument("--nombre",type=str,help="Por favor ingresa tu nombre")
    parser.add_argument("valor",type=float,help="Por favor ingresa tu valor para elevar al cuadrado")
    args=parser.parse_args()

    res=do_square(args.valor)
    if args.nombre:
        nombre=",tu nombre es "+args.nombre
        print(f"The result es {res}{nombre}")
    else:
        print(f"The result es {res}")

if __name__=="__main__":
    main()