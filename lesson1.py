import sys


# part 1
def part_1():
    name = "mohammad"
    age = 17
    favorite_game = "GTA sa"
    print(name)
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


# part 4
def part_4():
    secret_number = 7
    guess = 0

    while guess != secret_number:
        guess = int(input("یک عدد صحیح بزن: "))
        if guess < secret_number:
            print("بزرگ تره ^")
        elif guess > secret_number:
            print("کوچک تره !")
        else:
            print("افرین درست حدس زدی ")


# part 5
def part_5():
    def greet_user(name):
        print(f"سلام {name}! خوش امدی. ")

    greet_user("Saba")
    greet_user("Mohammd")


# part 6
def part_6():
    my_heroes = ["Batman", "Spider-man", "Iron man"]
    print(my_heroes[0])
    my_heroes.append("Superman")
    my_heroes.remove("Iron man")
    print(my_heroes)


def part_7():
    user_profile = {
        "name": "Mohammad",
        "age": "16",
        "city": "Mashhad",
        "is_active": True,
    }

    print(user_profile["name"])
    print(user_profile["age"])

    user_profile["email"] = "mmd1387s13@gmali.com"
    user_profile["age"] = 17

    print(user_profile)


def part_8():
    with open(
        r"c:\users\ms3pc\Desktop\python\file Io\notes.txt", "w", encoding="utf-8"
    ) as file:
        file.write("سلام دنیا!\n")
        file.write("من دارم پایتون یاد می‌گیرم. \n")

    print("فایل ذخییره شد!")

    # 8.1
    try:
        with open(
            r"c:\users\ms3pc\Desktop\python\file Io\notes.txt", "r", encoding="utf-8"
        ) as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("فایل پیدا نشد!")

    # 8.2
    with open(
        r"c:\users\ms3pc\Desktop\python\file Io\notes.txt", "r", encoding="utf-8"
    ) as f:
        lines = f.readlines()
        print(lines)
    # 8.3
    with open(
        r"c:\users\ms3pc\Desktop\python\file Io\notes.txt", "r", encoding="utf-8"
    ) as f:
        for line in f:
            print(line.strip())


# part 9
def part_9():
    import math
    import random

    print(math.sqrt(16))
    print(random.randint(1, 10))

    # 9.1
    from math import pi, sqrt

    print(f"عدد پی: {pi}")
    print(f"جذر 25: {sqrt(25)}")

    # 9.2
    import requests

    requests = requests.get("https://api.github.com")
    print(requests.status_code)


# part 10
def part_10():
    class Hero:
        def __init__(self, name, hp, atk):
            self.name = name
            self.hp = hp
            self.atk = atk

        def attack(self, target):
            target.hp -= self.atk
            print(f"{self.name} به {target.name} حمله کرد")

    ali = Hero("علی", 100, 20)
    sara = Hero("سارا", 100, 25)

    ali.attack(sara)

    # 10.1
    class Car:
        wheels = 4

        def __init__(self, brand, color, speed=0):
            self.brand = brand
            self.color = color
            self.speed - speed

        def accelerate(self, increment):
            self.speed += increment
            print(f"{self.brand} در سرعت {self.speed} کیلومتر بر ساعته")

        def stop(self):
            self.speed = 0
            print(f"{self.brand} ایستاد.")


parts = {
    "part_1": part_1,
    "part_2": part_2,
    "part_2_1": part_2_1,
    "part_3": part_3,
    "part_3_1": part_3_1,
    "part_4": part_4,
    "part_5": part_5,
    "part_6": part_6,
    "part_7": part_7,
    "part_8": part_8,
    "part_9": part_9,
    "part_10": part_10,
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
