import random

class Jogado:
#class 
    def __init__(self,sexo,nome,time, selecao,passe,fina, ritmo, dribra,defesa, fisico):
        #atributos
        self.sexo = sexo
        self.nome = nome
        self.time = time
        self.selecao = selecao
        self.passe = passe
        self.fina = fina
        self.ritmo = ritmo
        self.dribra = dribra
        self.defesa = defesa
        self.fisico = fisico
    #metodos 
    def imp (self):
        print("="*20)
        print("Nome:"+self.nome)
        print("Seleção:"+self.selecao)
        print("Time:"+self.time)
        print("Sexo:"+self.sexo)
        print("="*20)
        print("Passe:",self.passe)#
        print("Finalização:",self.fina)
        print("Ritmo:",self.ritmo)#
        print("Drible:", self.dribra)#
        print("Fisico:",self.fisico)
        print("Defesa:",self.defesa)
        print("="*20)

        


    def compara (self, oponente):
        escolha_atribruto = input("Escolha um atributo para comparar\n[1]Drible\n[2]Passe\n[3]Ritmo\nR: ")
        if escolha_atribruto == "1":
            if self.dribra > oponente.dribra:
                print("O ganhador é "+self.nome)
                return oponente
            else:
                print("O perdedor é "+self.nome)
                return oponente

        if escolha_atribruto == "2":
            if self.passe > oponente.passe:
                print("O ganhador é ",self.nome)
                return oponente
            else:
                print("O perdedor é ",self.nome)
                return oponente
                
        if escolha_atribruto == "3":
            if self.ritmo >  oponente.ritmo:
                print("O ganhador é" ,self.nome)
                return oponente
            else:
                print("O perdedor é ",self.nome)

        if escolha_atribruto == "4":
            if self.fina > oponente.fina:
                print("O ganhador é"+ self.nome)
            else:
                print("O perdedor é"+ self.nome)
        if escolha_atribruto == "5":
            if self.fisico > oponente+self.fisico:
                print("O ganhador é"+ self.nome)
                return oponente
            else:
                print("O perdedor é"+ self.nome)
        if escolha_atribruto == "6":
            if self.defesa > oponente+self.defesa:
                print("O ganhador é"+ self.nome)
                return oponente
            else:
                print("O perdedor é"+ self.nome)
