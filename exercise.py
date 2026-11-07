import sys


# Exercise 1
def test_1():
    score = int(input("Enter your score? "))

    if score <= 60:
        print("F")
        print("Fail")
    elif 60 <= score <= 69:
        print("D")
        print("Poor")
    elif 70 <= score <= 79:
        print("C")
        print("Average")
    elif 80 <= score <= 89:
        print("B")
        print("Good")
    else:
        print("A")
        print("Excellent")


# Exercise 2
def test_2():
    number = int(input("number? "))

    if number % 2 == 0:
        print("number even")
    else:
        print("number odd")


# Exercise 3
def test_3():
    for number in range(1, 31):
        if number % 2 == 0:
            print(number)
            print("even")
        elif number % 2 != 0:
            print(number)
            print("odd")


# Exercise 4
def test_4():
    total_sum = 0

    while True:
        user_input = input("(یا 'پایان' برای خروج)یک عدد وارد کنید: ")

        if user_input == "پایان":
            break

        total_sum += int(user_input)
        print(f"جمع فعلی: {total_sum}")

    print(f"جمع نهایی: {total_sum}")


# Exercise 5
def test_5():
    def add_numbers(a, b):
        result = a + b
        return result

    num1 = int(input("عدد اول: "))
    num2 = int(input("عدد دوم: "))

    total = add_numbers(num1, num2)
    print(f"جمع: {total}")

# 5.1
    def calculate_area(length, width):
        area = length * width
        return area

    length = float(input("طول مستطیل: "))
    width = float(input("عرض مستطیل: "))

    result = calculate_area(length, width)
    print(f"مساحت مسطتیل: {result}")


tests = {
    "test_1": test_1,
    "test_2": test_2,
    "test_3": test_3,
    "test_4": test_4,
    "test_5": test_5,
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command in tests:
            tests[command]()

        else:
            print("Invalid command")
    else:
        print("Please enter a command")
