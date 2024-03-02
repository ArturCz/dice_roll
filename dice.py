import random
def roll_dice(dice):
    dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    # xDy + z

    rolll = 0
    summ = 0
    try:
        x = dice[:dice.find("D")]
        if x == "":
            x = 1
        elif x == "0":
            check_x = 1 / int(x)
        else:
            x = int(x)
        if "+" in dice:
            check_dice = dice[dice.find("D"):dice.find("+")]
            y = int(dice[(dice.find("D") + 1):dice.find("+")])
            z = int(dice[(dice.find("+")) + 1:])
        elif "-" in dice:
            check_dice = dice[dice.find("D"):dice.find("-")]
            y = int(dice[(dice.find("D") + 1):dice.find("-")])
            z = int(dice[(dice.find("-")) + 1:])
        else:
            check_dice = dice[dice.find("D"):]
            y = int(dice[(dice.find("D") + 1):])
            z = 0
        dices.index(check_dice)

        while rolll < x:
            summ = summ + random.randint(1, y)
            rolll = rolll + 1
        summ = summ + z
        print(summ)
    except ValueError:
        print("Invalid dice")
    except TypeError:
        print("Invalid dice")
    except ZeroDivisionError:
        print("Invalid dice")



roll_dice("0D6")
roll_dice("4-3D6")
roll_dice("100D100*100")
roll_dice("100D100-100")
roll_dice("D22")

