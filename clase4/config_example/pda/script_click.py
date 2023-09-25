import click

def do_square(val):
    return val**2

@click.command()
@click.option("--valor",type=float,required=True,help="Por favor ingresa tu valor para elevar al cuadrado")
@click.option("--name",type=str,help="Por favor ingresa tu nombre")
def main(name,valor):
    res=do_square(valor)
    if name:
        nombre=",tu nombre es "+name
        print(f"The result es {res}{nombre}")
    else:
        print(f"The result es {res}")

if __name__=="__main__":
    main()