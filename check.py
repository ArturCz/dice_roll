import random
def check(dice):
    rolll = 0
    summ = 0
    try:
        x = dice[:dice.find("D")]
        if x == "":
            x = 1
        else:
            x = int(x)
        if "+" in dice:
            print("mns")
            y = int(dice[(dice.find("D")+ 1):dice.find("+")])
            z = int(dice[(dice.find("+"))+1:])
        elif "-" in dice:
            y = int(dice[(dice.find("D") + 1):dice.find("-")])
            z = int(dice[(dice.find("-")) + 1:])
        else:
            y = int(dice[(dice.find("D") + 1):])
            z = 0

        while rolll < x:
            summ = summ + random.randint(1, y)
            rolll = rolll + 1
        summ = summ + z
        print(summ)
    except ValueError:
        print("Invalid")



check("D6")

#xDy + z