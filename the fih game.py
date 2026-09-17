import random as rand

# def loot(cod,salmon,catfish,tuna):
#     pass

"""
    other = input("other").lower()

    if other == "other":
        print("worm shop")
        for worm in worms:
            print(f"- {worm}")
"""

#test commitu
coins = 0
worms = 0
"""
for _ in range(100):
    pass
"""
rand_coins = rand.randrange(3, 20)


#grupy do sklepu
rods = [("wooden rod", 20), ("iron rod", 60), ("steel rod", 80), ("master rod", 200)]
worms = [("worm", 2), ("blue worm", 5), ("ancient worm", 16), ("golden worm", 10)]
#rybki
fish1 = ["cod", "salmon", "catfish", "tuna"]

loot_chests_loot = [
    (rand.randrange(2, 6), "worms"),
    (rand_coins, "coins"),       #liczba od 3 do 20
    (1, "ancient artefact"),
    (1, "pearl"),
    (1, "golden worm")
]
"""
1. Przyjmujesz inputa (x)
2. Wpisujesz jakies wyrazenie (fish, salmon)
3. W metodzie loot1 gdzie masz tablice fish1 i zmienna randomFish1, usuwasz ja
4. Powtarzasz az nie bedzie konca
"""
# "coins", "gold", "artefact", "pearl", "golden worm"
#
# rand.randrange(2,6) 'worms' , rand.randrange(3,20) "coins"

def enoughToBuy(rod):
    return print(coins >= rod[1]) #puki co tyloko test "print(coins >= rod[1])" to tylok wazne->coins >= rod[1]


def loot2():
    fish1.extend(["puffer fish", "shark", "swordfish"])
    randomFish1 = rand.choice(fish1)

    fish1.remove(randomFish1)
    return rand.randrange(1, 5), randomFish1


# zrobic wielka petle i zapisywanie przedmitow
#

def loot3():
    fish1.extend(["loot_chest"])
    randomFish1 = rand.choice(fish1)
    fish1.remove(randomFish1)


    if randomFish1 == "loot_chest":     #jezeli loot chest ->losuj z tablicy loot_chests_loot
        print("loot chest found")
        rand_choice = rand.randrange(0, len(loot_chests_loot))
        if loot_chests_loot[rand_choice] == "coins":
            coins = coins + rand_coins
        return loot_chests_loot[rand_choice]

    else:
        return rand.randrange(1, 3), randomFish1


print("fish,shop,worm")

choice = input("fih?").lower()

if choice == "fish":
    try:
        print(loot1() + loot2()) or print(loot1() + loot2() and loot3())
    except:
        print("no fish found")


elif choice == "shop":
    print(f"coins: {coins}")
    print("Available rods:")
    for rod in rods:
        print(f"- {rod}")
        input("enter: buy rod_name")



elif choice == "worm":
    print("worm shop")
    for worm in worms:
        print(f"- {worm}")
        input("enter: buy worm_name")
        coins = coins - worm[1]     #coins = coins - worm[1]
        print(f"coins: {coins}")


else:
    print("invalid choice")
