import random

print("Monty Hall Problem")


# expected results
def test():
    print("\nRandom door picking")
    correct_choices = 0
    for i in range(10000):
        # create door with car
        doors = [0, 0, 0]

        car = random.randrange(0, 3)
        doors[car] = 1

        # pick a door
        choice = random.randrange(0, 3)

        if doors[choice] == 1:
            correct_choices += 1

    print(str(correct_choices / 100) + "%", "choices correct")
    print("")


# monty hall situation with a random door being revealed


def hall1():
    print("Random door revealed")
    correctswaps = 0
    correctholds = 0
    freebies = 0
    for i in range(10000):
        # create door with car

        d1, d2, d3 = 0, 1, 2
        doors = [d1, d2, d3]

        car = random.randrange(0, 3)
        doors.remove(car)

        # pick a door
        choice = random.randrange(0, 3)
        randDoor = random.randrange(0, 3)

        if randDoor == car:
            freebies += 1
            continue

        if choice == car:
            correctholds += 1

        else:
            correctswaps += 1

    print(str(correctswaps / 100) + "%", "swapped")
    print(str(correctholds / 100) + "%", "holds")
    print(str(correctholds / 100) + "%", "freebies")
    print("")


# monty hall situation where a goat is always revealed and you keep your pick
def hall2():
    print("Proper test with a goat being revealed")
    correctswaps = 0
    correctholds = 0
    for i in range(10000):
        # create door with car

        d1, d2, d3 = 0, 1, 2
        doors = [d1, d2, d3]

        car = random.randrange(0, 3)
        doors.remove(car)

        # pick a door
        choice = random.randrange(0, 3)

        # goat is revealed
        goatDoor = random.choice(doors)
        doors.remove(goatDoor)

        if choice == car:
            correctholds += 1

        else:
            correctswaps += 1

    print(str(correctswaps / 100) + "%", "swapped")
    print(str(correctholds / 100) + "%", "holds")


test()
hall1()
hall2()
