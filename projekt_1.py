'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Novotný
email: hornstr@seznam.cz / petrnovotny@gmail.com
discord: vasilek91_82724
'''
import sys

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

print('$ python projekt1.py')
oddelovac = '----------------------------------------'

#definovaný dict s přístupy
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}



#část pro zadání přístupových údajů
username = input('username:')
#username = 'bob'
#heslo = '123'
heslo = input('password:')

print(oddelovac)

#zjišťuju kolik textů je na výběr
pocet_textu = len(TEXTS)

# Ověření uživatele a hesla
if username in users and users[username] == heslo:
    print(f'Welcome to the app, {username}\nWe have {pocet_textu} text to analyze')
else:
    print('unregistered user, terminating the program..')
    sys.exit()  # Tento příkaz ukončí program



print(oddelovac)

#uživatel vybírá text a ujišťuji se že budu pracovat s int
while True:
    vybrany_text = input(f'Enter a number between 1 and {pocet_textu} to select: ')

    # Kontrola, zda je vstup validní
    if not vybrany_text.isdigit():
        print(f'{vybrany_text} is not valid, please enter a valid number.')
        continue
    elif int(vybrany_text) not in range(1, pocet_textu + 1):
        print(f'{vybrany_text} is not valid, please select a number between 1 and {pocet_textu}.')
        continue
    vybrany_text = int(vybrany_text)
    break
  

print(oddelovac)

#tady určuju zvolený text a rozsekám a očistím o tečky a čárky
text_pro_statisiku = TEXTS[vybrany_text - 1]
jednotliva_slova = text_pro_statisiku.split()
ocistena_slova_v_textu = [slovo.strip('''?,:._-"'!/()[{/*-+ˇ^°;}]''') for slovo in jednotliva_slova]
#print(ocistena_slova_v_textu)

#samotný výpočet statistiky
pocet_slov_v_textu = len(text_pro_statisiku.split())

pocet_slov_s_velkym_pismenem = 0
pocet_slov_jenom_s_velkymi_pismeny = 0
pocet_slov_jenom_s_malymi_pismeny = 0
pocet_numerickych_stringu = 0
suma_cisel = 0

for slovo in ocistena_slova_v_textu:
  if slovo[0].isupper():
    pocet_slov_s_velkym_pismenem += 1
  if slovo.isupper() and slovo.isalpha():
    pocet_slov_jenom_s_velkymi_pismeny += 1
  if slovo.islower():
    pocet_slov_jenom_s_malymi_pismeny += 1
  if slovo.isnumeric():
    pocet_numerickych_stringu += 1
  if slovo.isnumeric():
    suma_cisel += int(slovo)

#tady tisknu výstupy ze statistiky
print('There are',pocet_slov_v_textu, 'words in the selected text.')
print('There are',pocet_slov_s_velkym_pismenem,'titlecase words.')
print('There are' ,pocet_slov_jenom_s_velkymi_pismeny,'uppercase words.')
print('There are' ,pocet_slov_jenom_s_malymi_pismeny,'lowercase words.')
print('There are' ,pocet_numerickych_stringu,'numeric strings.')
print('The sum of all the numbers', suma_cisel)

print(oddelovac)

#určuju jak jsou jednotlivá očištěná slova v textu dlouhá
delky_slov = [len(slovo) for slovo in ocistena_slova_v_textu]

#slovnik pro delky slov a jeho naplnění
cetnost_delek = {}
for delka in delky_slov:
  if delka not in cetnost_delek:
    cetnost_delek[delka] = 1
  else:
    cetnost_delek[delka] += 1

#hodnoty z dictu cetnost delek
hodnoty_cetnost_delek = (sorted(cetnost_delek.values()))

#stanovím maximální délku grafu plus 3 místa navíc
delka_grafu = max(hodnoty_cetnost_delek)

#tohel udělá počet znaků v délce četností slov
delka_cetnosti = len(str(max(cetnost_delek)))

#tisk hlavičky grafu
length = 'LEN'
occ = 'OCCURENCES'
nr = 'NR.'

hlavicka_grafu = (f'{length:>{len(str(length))}} | {occ:<{str(delka_grafu)}} | {nr:<2}')
print(hlavicka_grafu)
print(oddelovac)
#tisk grafu
for delka, cetnost in sorted(cetnost_delek.items()):
  graf = cetnost * '*'
  print(f'{delka:>{len(str(length))}} | {graf:<{delka_grafu}} | {cetnost:<2}')