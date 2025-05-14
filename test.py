# C'est pour les testes
def somme(a,b):
    return a+b

print(somme(1,1))

def aire_rectangle(h, b):
    return h*b

def dire_bonjour(message, nom):
    return message + nom

def question():
    input("Ton ordi est casse?")

print("Test de push")

#Exercices Fonctions:
def creer_liste(n):
    liste = []
    for i in range(n):
        value = int(input("Rentrer un chiffre: "))
        liste.append(value)
    return liste


def somme(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


def moyenne(total, numbers):
    mean = total / len(numbers)
    return mean


def ecart_type(numbers, mean):
    dev = 0
    for i in numbers:
        dev += (i - mean) ** 2
    dev = (dev / len(numbers)) ** 0.5
    return dev


def variance(dev):
    return dev ** 2


# n = int(input("Rentrer la taille de la liste: "))
# numbers = creer_liste(n)

numbers = [2, 4, 6, 8, 10]
print("La liste est:", numbers)

total = somme(numbers)
print("La somme de la liste est:", total)

mean = moyenne(total, numbers)
print("La moyenne est:", mean)

Ecart_Type = ecart_type(numbers, mean)
print("L'écart type est:", round(Ecart_Type, 2))

Variance = variance(Ecart_Type)
print("La variance est:", round(Variance, 2))


