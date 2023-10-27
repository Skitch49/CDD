EUR = 0.85
JPY = 110
GBP = 0.75

print("Bienvenue dans le Convertisseur de Devises en PYTHON.")

continuer = 'Oui'

while continuer.lower() == 'oui':
    print("Que voulez-vous faire?")
    print("\n1-Conversions USD/EUR", "\n2-Conversions USD/JPY", "\n3-Conversions USD/GBP")
    choix = input()
    print("Vous avez choisi", choix)

    if choix == '1':
        print("Entrez le nombre d'USD que vous voulez convertir en euros:")
        try:
            value = input()
            if value.isnumeric():
                value = float(value)
                euros = value * EUR
                print("Montant équivalent en EUR :", euros)
            else:
                raise ValueError("Input is a null value or not a number")
        except ValueError as e:
            print(e)

    elif choix == '2':
        print("Entrez le nombre d'USD que vous voulez convertir en yen:")
        try:
            value = input()
            if value.isnumeric():
                value = float(value)
                yen = value * JPY
                print("Montant équivalent en JPY :", yen)
            else:
                raise ValueError("Input is a null value or not a number")
        except ValueError as e:
            print(e)


    elif choix == '3':
        print("Entrez le nombre d'USD que vous voulez convertir en livres:")
        try:
            value = input()
            if value.isnumeric():
                value = float(value)
                livres = value * GBP
                print("Montant équivalent en GBP :", livres)
            else:
                raise ValueError("Input is a null value or not a number")
        except ValueError as e:
            print(e)

    continuer = input(
        "Voulez-vous effectuer une autre conversion ? (Oui/Non) ")

print("Merci d'avoir utilisé le Convertisseur de Devises!")
