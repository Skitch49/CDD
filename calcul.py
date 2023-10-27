EUR = 0.85
JPY = 110
GBP = 0.75

print("Bienvenue dans le Convertisseur de Devises en PYTHON.")
print("Que voulez-vous faire?")
print("\n1-Conversions USD/EUR", "\n2-Conversions USD/JPY", "\n3-Conversions USD/GBP")
choix = input()
print("Vous avez choisi", choix)

if choix == '1':
    print("Entrez le nombre d'USD que vous voulez convertir en euros:")
    try:
        if input().isnumeric():
            value = float(input())
            euros = value * EUR
            print("Montant équivalent en EUR :", euros)
        else:
            raise ValueError("Input is a null value or not a number")
    except ValueError as e:
        print(e)

elif choix == '2':
    print("Entrez le nombre d'USD que vous voulez convertir en yen:")
    try:
        if input().isnumeric():
            value = float(input())
            yen = value * JPY
            print("Montant équivalent en JPY :", yen)
        else:
            raise ValueError("Input is a null value or not a number")
    except ValueError as e:
        print(e)
    

elif choix == '3':
    print("Entrez le nombre d'USD que vous voulez convertir en livres:")
    try:
        if input().isnumeric():
            value = float(input())
            livres = value * GBP
            print("Montant équivalent en GBP :", livres)
        else:
            raise ValueError("Input is a null value or not a number")
    except ValueError as e:
        print(e)
