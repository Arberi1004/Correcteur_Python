#Ceci est la fonction qui va permettre de lire le dictionnaire et de retourner chaque mot
def dictionnaire(dico):
    motsDico = []                   #on créer une list où l'on stockera tous les mots du dictionnaire ligne par ligne, sans caractère à droite et a gauche
    fichierEntree = open(dico, "r") #on ouvre le fichier du dictionnaire
    for ligne in fichierEntree:
        mot = ligne.strip()         #on retire les elements a droite et a gauche
        motsDico.append(mot)        #on ajoute nos mots à la liste motsdico
    fichierEntree.close()
    return motsDico
    

def texteBase(texte):               #comme pour le dictionnaire, on va traiter le fichier texte de base, la ou les erreurs sont présentes
    motsFichier = []                #on créer cette liste pour stocker chaque mot du fichier a traiter
    fichierEntree = open(texte, "r") #on ouvre le fichier pour le traiter
    for ligne in fichierEntree:
        motLigne = ligne.strip().split()    #on divise la chaine en liste et on retire les elements de droite a gauche pour pouvoir bien traiter chaque mot
        for mot in motLigne:
            motsFichier.append(mot.strip(".,!\":;?").lower()) #on retire toute ponctuation car lors du retour de fonction on evitera d'avoir de la ponctuation en retour
    fichierEntree.close()
    return motsFichier

def trouverErr(dico, texte): #fonction qui permet de trouver et de stocker les erreurs
    erreurs = []
    for mot in texte:
        if mot not in dico:
            erreurs.append(mot)
    return erreurs


# pour afficher les erreurs et proposer les corrections, j'ai réalisé cette fonction
#je n'ai pas réussi à reproduire à l'identique comme vous mais j'ai quelque chose qui fonctione 
def afficheErr(erreurs,dico,texte,fichierTexte,newFile):
    #file = open(newFile, "w+")
    file = []
    print("Pour accepter la proposition de correction, tapez 1. \n Pour refuser la proposition de correction, tapez 0. \n Pour proposez votre propre correction, tapez 2. \n")
    print("Les erreurs sont :")
    print(erreurs)
    for mot in erreurs:
        print(mot)
        for mots in dico:          
           #dans ce if on compare les premières lettres et la longueurs de la chaines de caractère 
           if(mot[:1] == mots[:1] and mot[:2] == mots[:2] and mot[:3] == mots[:3] and mot[:4] == mots[:4] and len(mot)==len(mots)):
               print(mots)
               #On propose 3 choix : ajouter un mot parmis les corrections proposée, passer sur le mot, ou ajouter sa propre correction
               choix = input("Votre choix : \n") 
               if (choix == '0'):
                  print(" ")
               elif (choix == '1'):
                   
                   file.append(mots)
                   print(file)
                   
               elif (choix == '2'):
                   correction = input("Saisissez votre correction : ")
                   file.append(correction)
                   print(file)
                   
#ici je veux créer mon nouveau fichier avec mes corrections ou je regroupe les mots deja correctement rédigé et les mots corrigés                    
    for word in texte:
        if word not in erreurs:
            file.append(word)
#on affiche la liste de fin grace au print et on créer le nouveau fichier en meme temps  
#contrairement à vous je n'ai pas réussi à insérer les éléments à leur place initiale          
    print("Vous pouvez vonsulter votre liste corrigée : \n ") 
    print(file)
    nouvFile = open(newFile, "w+")
    for element in file:
        nouvFile.write(element + " ")
        
        


def main():
    print("Bienvenue dans votre correcteur orthographique !")
    
    dico = input("Entrez le chemin absolu de votre dictionnaire : ")
    texte = input("Entrez le chemin absolu du fichier à inspecter : ")
    newFile = input("Entrez le chemin du nouveau fichier (au format ../chemin/nom_fichier.txt) : ")
    listeDico = dictionnaire(dico)   
    listeTexte = texteBase(texte)
    listeErreurs = trouverErr(listeDico, listeTexte)
    afficheErr(listeErreurs,listeDico,listeTexte,texte,newFile)
    
    
main()