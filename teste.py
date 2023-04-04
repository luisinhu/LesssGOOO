from testeclass import Jogado
import random

benzema = Jogado("M", "Benzema", "Real", "França",90,97,92,94,45,90)
neymar = Jogado("M", "Neymar", "PSG", "Brasil",87,87,90,95,39,64)
pelé = Jogado("M", "Pelé", "Santos", "Brasil",96,96,99,76, 39, 64)
bappe = Jogado("M", "Mbappe", "PSG", "França",88,96,99,98,44,87)
formiga = Jogado("F","Formiga","PSG","Brasil",80,78,76,77,90,92)
Marta = Jogado("F","Marta","Orlando Pride","Brasil",90,89,85,96,34,70)
Debinha = Jogado("F","Debinha","Kansas City Current","Brasil",93,88,85,87,34,70)



lista = [benzema,neymar,pelé,bappe,formiga,Marta,Debinha]
sorteado  = random.choice(lista)

print(sorteado.imp())

lista2 = [benzema,neymar,pelé,bappe,formiga,Marta,Debinha]
sorteado2  = random.choice(lista2)

print(sorteado2.imp())

if sorteado == benzema:
    benzema.compara(sorteado2)

if sorteado == neymar:
    neymar.compara(sorteado2)

if sorteado == pelé:
    pelé.compara(sorteado2)


if sorteado == bappe:
    bappe.compara(sorteado2)

if sorteado == formiga:
    formiga.compara(sorteado2)

if sorteado == Debinha:
    Debinha.compara(sorteado2)
if sorteado == Marta:
    Marta.compara(sorteado2)

