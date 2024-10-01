"""
Auteur : Arnaud POCHIC

"""

def isprime(p):
    """
    Retourne True ou False en fonction de si p est premier ou pas.

    Args:
        num: valeur entiere positive

    Returns:
        True or False
    """
    premier = True
    if p in (0,1):
        return False
    for i in range(2,int(p**0.5+1)):
        if p%i == 0:
            premier = False
            break
    return premier

#### Fonction principale


def main():
    """
    fonction principale qui appelle isprime()
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
