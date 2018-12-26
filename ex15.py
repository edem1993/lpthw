# Reading Files

# betölti a 'sys' modulból az 'argv' funkciót
from sys import argv
# megadjuk a 2 argumentumot (script neve + még egy)
script, filename = argv
# txt váltózóhoz rendeljük az argumentumot, ami a fájlnak a neve jelen esetben
txt = open(filename)
# kiíratjuk f-stringgel a fájl nevét
print(f"Here's your file {filename}")
# beolvassuk read() funkcióval a txt változót, ami tartalmazza a fájl tartalmát
print(txt.read())
txt.close()

# megadjuk a fájl nevét újból
print("Type the filename again:")
# hozzárendeljük a promptban megadott fájlnevet egy új változóhoz
file_again = input("> ")
# megnyitjuk a fájlt és hozzárendeljük még1 változóhoz
txt_again = open(file_again)
# beolvassuk a fájlt és kiíratjuk az új fájl tartalmát
print(txt_again.read())
txt_again.close()