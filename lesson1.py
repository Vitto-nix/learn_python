import sys


# part 1
def part_1():
    name = "mohammad"
    age = 17
    favorite_game = "GTA sa"
    print(name)
    print(age)
    print(age)
    print(favorite_game)


# part 2
def part_2():
    age = int(input("سن خود را وارد کنید: "))

    if age >= 18:
        print("می تونی بری سینما!")
    else:
        print("هنوز دیر است برگرد خانه.")


# 2.1
def part_2_1():
    age = int(input("کنید وارد را سن خود:"))

    if age < 12:
        print("بازیگوش!")
    elif 12 <= age <= 18:
        print("نوجوان")
    else:
        print("بزرگسال")


# part 3
def part_3():
    for number in range(1, 11):
        if number % 2 == 0:
            print(number)


# 3.1
def part_3_1():
    import random

    random_number = random.randint(1, 20)
    guess = None

    while guess != random_number:
        guess = int(input("حدس بزن: "))
        if guess < random_number:
            print("بزرگ تره!")
        elif guess > random_number:
            print("کوچک تره!")

    print("افرین درست حدس زدی")


parts = {
    "part_1": part_1,
    "part_2": part_2,
    "part_2_1": part_2_1,
    "part_3": part_3,
    "part_3_1": part_3_1,
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command in parts:
            parts[command]()

        else:
            print("Invalid command")
    else:
        print("Please enter a command")
