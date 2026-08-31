from colorama import Fore, Style


while True:
    try:
        edad = int(input("Edad: "))
        break
    except ValueError:
        print(Fore.RED + "Ingresa un valor numerico")
        print(Style.RESET_ALL)

print(Fore.GREEN  + "Edad registrada:", edad)