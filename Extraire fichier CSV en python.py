
import csv


pers = int(input("Combien d'eleve(s) font le test ? : "))


def colonne(file, n, sep=","): #fichier, definition fonction lisant le fichier
    with open(file, "r") as f: #"r" pour read / w pour write pour modifier le fichier
        jp = csv.reader(f, delimiter = sep)
        lignes = list(jp) #lecture ligne par ligne du fichier
        res = [] 
        if (n < len(lignes[0])) and (n>= -len(lignes[0])):
            for l in lignes:
                res.append(l[n]) # prise des informations de la colonne n
            return res

for i in range(pers):
    nom = str(input("Quel est ton nom ? : "))        
    def nbq(file, n, sep=","):
        with open(file, "r") as f2:
            jp2 = csv.reader(f2, delimiter = sep)
            lignes2 = list(jp2)
            res2 = len(lignes2[1])
            return res2
    
    if __name__ == "__main__":
        score = 0
        ques = nbq("Exo pays.csv", 1, sep=",")
   
        for i in range(1,ques):
            c = colonne("Exo pays.csv", i, sep=",")
            q = c[1]
            p1 = c[2]
            p2 = c[3]
            rep = c[4]
        
            print("Quelle est la capitale de",q)
            print("a :",p1)
            print("b :",p2)
            rep1 = input("Votre reponse : ")
            if rep1 == rep :
                    print("Bien joue")
                    score = score + 1
        print("Le score de", nom, "est de", score,"/", ques-1)

        with open('Exo pays2.csv', 'w',newline ='') as f:
            writer=csv.writer(f)
            test1 = "Resultat des eleves"
            writer.writerows([test1])
            test2 = ([nom, score,"/", ques-1])
            writer.writerows([test2])


        """r = csv.reader(open('Exo pays2.csv')) 
        lines = list(r)

        lines [1]= [(nom, score,"/", ques-1)]
        writer = csv.writer(open('Exo pays2.csv', 'w'))
        writer.writerows(lines)"""
        


#problemes à regler : le premier revient / ecriture case par case