import random as rand

# def loot(cod,salmon,catfish,tuna):
#     pass

#test commitu
#
rods = ["wooden rod", "iron rod", "steel rod", "master rod"]
worms = ["worm", "blue worm", "ancient worm", "golden worm"]


loot_chests_loot = [
    (rand.randrange(2, 6), "worms"),
    (rand.randrange(3, 20), "coins"),
    (1, "ancient artefact"),
    (1, "pearl"),
    (1, "golden worm"),
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


def loot1():
    global fish1
    fish1 = ["cod", "salmon", "catfish", "tuna"]
    randomFish1 = rand.choice(fish1)
    fish1.remove(randomFish1)
    return rand.randrange(1, 5), randomFish1


def loot2():
    fish1.extend(["puffer fish", "shark", "swordfish"])
    randomFish1 = rand.choice(fish1)

    fish1.remove(randomFish1)
    return rand.randrange(1, 5), randomFish1


# zrobic wielka petle i zapisywanie przedmitow


def loot3():
    fish1.extend(["loot_chest"])
    randomFish1 = rand.choice(fish1)
    fish1.remove(randomFish1)
    if randomFish1 == "loot_chest":
        print("loot chest found")
        rand_choice = rand.randrange(0, len(loot_chests_loot))
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
    print("Available rods:")
    for rod in rods:
        print(f"- {rod}")

    other = input("other").lower()

    if other == "other":
        print("worm shop")
        for worm in worms:
            print(f"- {worm}")
