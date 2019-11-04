#Je veux comparer deux nombre
def reponse(_nb1: int, _nb2: int) -> float:
    """
    Comparer 2 valeurs et return la plus petite ou 0 si elle sont égales
    :param _nb1: float -> 1ere valeur à comparer
    :param _nb2: float -> 2ème valeur à comparer
    :return: float -> la valeur la plus petite ou 0 si elles sont égales
    """
    _nb1 = question
    _nb2 = question2
    if _nb1 < _nb2:
        return _nb1
    elif _nb2 < _nb1:
        return _nb2
    else:
        ("Les valeurs sont fausses")


#Invitation à l'écran
question: int = int(input("Choississez un nombre : "))

question2: int = int(input("Choississez un deuxième nombre : "))

question: float = 0.0
question: float = 0.0

plus_petit = reponse(question, question2)

print(plus_petit, "est le plus petit des 2 nombres")


