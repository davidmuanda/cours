###Je veux comparer entre deux nombre lequel est le plus petit

def reponse(_nb1: int, _nb2: int):
    _nb1 = question
    _nb2 = question2
    if _nb1 < _nb2:
        print("La valeur la plus petite est:", _nb1)
    elif _nb2 < _nb1:
        print("La valeur la plus petite est :", _nb2)
    elif _nb1 == _nb2:
        print("Les deux valeurs sont égales")
    else:
        print("Valeur fausses")

#Partie principal
nombre: float = 0.0
nombre2: float = 0.0

#Invitation à l'écran
question: int = int(input("Choississez un nombre : "))

question2: int = int(input("Choississez un deuxième nombre : "))

reponse(nombre, nombre2)



