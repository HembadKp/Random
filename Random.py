
import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", 
help="use 'echo' para iniciar o programa. exemplo: python po.py echo")
args = parser.parse_args()
print(args.echo)

def criador():
    print("----" * 10)
    print("Criador: HembadPy")
    print("----" * 10)
def banner():
    print("####" * 10) 
    print("RANDOM AUTOMATIZADOR\033[32m")
def ola():
   print("====" * 10)
   numero = input('digite numero: ')
   lista = []
   i = 1
   while i <= int(numero):
       coisa = input("adicione qualquer coisa e programa ira selecionar aleatoriamente: ")
       lista.append(coisa)
       i += 1
   print("====" * 10)
   print("PALAVRA ESCOLHIDA: ", random.choice(lista))
   print("====" * 10)
   for x in lista:
       print("LISTA: ", x)
banner()
ola()
criador()
