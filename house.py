name = input("what's your name? ")

match name:
    case "Deng" | "Achol" | "Bol":
       print("Juba")
    case "Gor" | "Jose":
       print("Rumbek")
    case "Laat":
       print("Azande")
    case _:
       print("Unknown")