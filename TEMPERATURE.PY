
print("")
print(r"████████╗███████╗███╗   ███╗██████╗ ███████╗██████╗  █████╗ ████████╗██╗   ██╗██████╗ ███████╗")
print(r"╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██╔════╝")
print(r"   ██║   █████╗  ██╔████╔██║██████╔╝█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝█████╗  ")
print(r"   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗██╔══╝  ")
print(r"   ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗")
print(r"   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝")
print("")
print(r"Made by Etann & Rémy")
print("")
print("====================================")
print("")
#Intialistation de la variable
temperature_brute = ""
#Détection et traitement de l'entrer utillisteur
while len(temperature_brute) <= 10 :
    user_input = input("Saisir 0 ou 1 : ")
    try:
        if 0<= int(user_input) <=1 :
            temperature_brute += user_input
        else:
            print("Veuiller entre une valeur valable : 0 ou 1")
    except ValueError:
        print("Veuiller entre une valeur valable : 0 ou 1")
# Séparation du premier bit
temperature_bin = temperature_brute[1:]

# Partie négative
if int(temperature_brute[0]) == 1 :
    # Prendre le complément à deux
    temperature_bin = ''.join('1' if b == '0' else '0' for b in temperature_bin)
    temperature_dec = int(temperature_bin, 2) + 1
    temperature_dec = -temperature_dec
else:
    temperature_dec = int(temperature_bin, 2)
#Variable complet 
print(temperature_brute)
#Résolution
temperature = float(temperature_dec * 0.125)
print("")
print("====================================")
print("")
print("Température: ",temperature)