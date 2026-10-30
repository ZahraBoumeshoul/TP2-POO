# -*- coding: utf-8 -*-
# TP2 POO - Mes premieres classes en Python : les constructeurs
# Etudiante : Zahra BOUMESHOUL - Filiere R2C - ESTK
# Ce fichier regroupe les 7 exercices. Chaque exercice redefinit la classe Livre.


def titre(texte):
    print("\n" + "=" * 60)
    print(texte)
    print("=" * 60)


# ------------------------------------------------------------
# EXERCICE 1 - Une classe sans constructeur
# ------------------------------------------------------------
titre("EXERCICE 1 - Classe sans constructeur")


class Livre:
    pass


l1 = Livre()
l1.titre = "La Boite a merveilles"
l1.auteur = "Sefrioui"
l1.annee = 1954

l2 = Livre()
l2.titre = "Le Passe simple"
l2.auteur = "Chraibi"
# l'annee de l2 a ete oubliee !

print(f"{l1.titre} - {l1.auteur} ({l1.annee})")
try:
    print(f"{l2.titre} - {l2.auteur} ({l2.annee})")      # ligne qui plante
except AttributeError as e:
    print("ERREUR (etape 1) : AttributeError:", e)

# Etape 2 : on ajoute l'annee manquante
l2.annee = 1954
print(f"{l2.titre} - {l2.auteur} ({l2.annee})")

# Etape 3 : troisieme livre
l3 = Livre()
l3.titre = "Clean Code"
l3.auteur = "Martin"
l3.annee = 2008
print(f"{l3.titre} - {l3.auteur} ({l3.annee})")

# Q1.2 : faute de frappe -> pas d'erreur, un nouvel attribut "anee" est cree
l4 = Livre()
l4.titre = "Test"
l4.auteur = "Test"
l4.anee = 1954
try:
    print(l4.annee)
except AttributeError as e:
    print("Faute de frappe l4.anee = 1954 -> AttributeError a la lecture de l4.annee:", e)


# ------------------------------------------------------------
# EXERCICE 2 - Mon premier constructeur
# ------------------------------------------------------------
titre("EXERCICE 2 - Mon premier constructeur")


class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def afficher(self):
        if self.disponible:
            etat = "disponible"
        else:
            etat = "emprunte"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")


l1 = Livre("La Boite a merveilles", "Sefrioui", 1954)
l2 = Livre("Le Passe simple", "Chraibi", 1954)
l3 = Livre("Clean Code", "Martin", 2008)

l2.emprunter()
l1.afficher()
l2.afficher()
l3.afficher()


# ------------------------------------------------------------
# EXERCICE 3 - Creer un livre sans argument
# ------------------------------------------------------------
titre("EXERCICE 3 - Livre sans argument")

# Etape 1 : constructeur de l'exercice 2 + l4 = Livre()
try:
    l4 = Livre()
except TypeError as e:
    print("ERREUR (etape 1) : TypeError:", e)


# Etape 2 : valeurs par defaut
class Livre:
    def __init__(self, titre="Sans titre", auteur="Inconnu", annee=2026):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def afficher(self):
        if self.disponible:
            etat = "disponible"
        else:
            etat = "emprunte"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")


# Etape 3
l1 = Livre("La Boite a merveilles", "Sefrioui", 1954)
l4 = Livre()
l1.afficher()
l4.afficher()


# ------------------------------------------------------------
# EXERCICE 4 - Plusieurs facons de creer un livre
# ------------------------------------------------------------
titre("EXERCICE 4 - Plusieurs facons de creer un livre")

l1 = Livre("La Boite a merveilles", "Sefrioui", 1954)   # 3 arguments
l2 = Livre("Initiation a la POO", "Berka")              # 2 arguments
l3 = Livre()                                            # 0 argument
l4 = Livre("Clean Code", annee=2008)                    # argument nomme
for l in (l1, l2, l3, l4):
    l.afficher()

# Q4.2 : deux __init__ dans la meme classe ?
class Test:
    def __init__(self):
        print("premier __init__")

    def __init__(self, x):
        print("deuxieme __init__ avec x =", x)


try:
    Test()
except TypeError as e:
    print("Test() -> TypeError:", e)
Test(5)


# ------------------------------------------------------------
# EXERCICE 5 - Un constructeur qui refuse les erreurs
# ------------------------------------------------------------
titre("EXERCICE 5 - Constructeur qui refuse les erreurs")


class Livre:
    def __init__(self, titre, auteur, annee):
        if titre == "":
            raise ValueError("le titre est vide")
        if annee < 1450 or annee > 2026:
            raise ValueError(f"annee impossible : {annee}")
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def afficher(self):
        if self.disponible:
            etat = "disponible"
        else:
            etat = "emprunte"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")


l1 = Livre("La Boite a merveilles", "Sefrioui", 1954)
l1.afficher()

try:
    l2 = Livre("Le Passe simple", "Chraibi", 3054)
    l2.afficher()
except ValueError as e:
    print("Livre refuse :", e)

try:
    l2 = Livre("", "Chraibi", 1954)
    l2.afficher()
except ValueError as e:
    print("Livre refuse :", e)


# ------------------------------------------------------------
# EXERCICE 6 - Compter les livres
# ------------------------------------------------------------
titre("EXERCICE 6 - Compter les livres")


class Livre:
    nombre_livres = 0                     # compteur PARTAGE par tous les livres

    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        Livre.nombre_livres = Livre.nombre_livres + 1
        self.numero = Livre.nombre_livres

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def afficher(self):
        print(f"#{self.numero} {self.titre} - {self.auteur} ({self.annee})")


print("Livres crees :", Livre.nombre_livres)
l1 = Livre("La Boite a merveilles", "Sefrioui", 1954)
l2 = Livre("Le Passe simple", "Chraibi", 1954)
l3 = Livre("Clean Code", "Martin", 2008)
l1.afficher()
l2.afficher()
l3.afficher()
print("Livres crees :", Livre.nombre_livres)

# Q6.2 : version fautive (self.nombre_livres au lieu de Livre.nombre_livres)
print("\n--- Q6.2 : version fautive avec self.nombre_livres ---")


class LivreFaux:
    nombre_livres = 0

    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.nombre_livres = self.nombre_livres + 1     # cree un attribut d'INSTANCE
        self.numero = self.nombre_livres

    def afficher(self):
        print(f"#{self.numero} {self.titre} - {self.auteur} ({self.annee})")


print("Livres crees :", LivreFaux.nombre_livres)
f1 = LivreFaux("La Boite a merveilles", "Sefrioui", 1954)
f2 = LivreFaux("Le Passe simple", "Chraibi", 1954)
f3 = LivreFaux("Clean Code", "Martin", 2008)
f1.afficher()
f2.afficher()
f3.afficher()
print("Livres crees :", LivreFaux.nombre_livres)


# ------------------------------------------------------------
# EXERCICE 7 - Copie ou meme livre ?
# ------------------------------------------------------------
titre("EXERCICE 7 - Copie ou meme livre ?")


class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def afficher(self):
        if self.disponible:
            etat = "disponible"
        else:
            etat = "emprunte"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")


original = Livre("Clean Code", "Martin", 2008)
meme = original                                                   # un autre NOM pour le meme livre
copie = Livre(original.titre, original.auteur, original.annee)    # un DEUXIEME livre

copie.emprunter()
print("Apres copie.emprunter() :")
print("  original : ", end=""); original.afficher()
print("  copie    : ", end=""); copie.afficher()

meme.emprunter()
print("Apres meme.emprunter() :")
print("  original : ", end=""); original.afficher()

print(meme is original, copie is original)
