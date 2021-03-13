# for cislo in range (1,21):
#     if cislo == 4 or cislo == 13:
#         print(f"{cislo} Neparne")
#     elif cislo % 2 == 0:
#         print(f"{cislo} Parne")
#     else :
#         print(f"{cislo} Neparne")

for cislo in range (1,21):
    if cislo == 4 or cislo == 13:
        state = "Nestastne"
    elif cislo % 2 == 0:
        state = "Parne"
    else:
        state = "Neparne"
    print(f"{cislo} je {state}")