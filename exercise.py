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


# Exercise 6
def test_6():
    favorite_foods = ["pizza", "Burger", "Kebab", "Pasta", "Salad"]
    print("اولین غذای من: ", favorite_foods[0])
    new_food = input("اسم یک غذای جدید: ")
    favorite_foods.append(new_food)
    print("لیست کامل: ")
    for food in favorite_foods:
        print(f"- {food}")

    # 6.1
    grades = []

    for i in range(5):
        grade = float(input(f"نمره دانش اموز {i + 1}: "))
        grades.append(grade)

    average = sum(grades) / len(grades)
    print(f"میانگین نمرات: {average:.2f}")
    print(f"بالاترین نمره: {max(grades)}")
    print(f"پایین ترین نمره: {min(grades)}")


# Exercise 7
def test_7():
    product = {"name": "Laptop", "price": 50000, "stock": 10}

    print(f"قیمت: {product['price']}")

    product["stock"] -= 1
    print(f"موجودی جدی: {product['stock']}")

    product["discount"] = 0.1

    print(product)


# 7.1
# phonebook


tests = {
    "test_1": test_1,
    "test_2": test_2,
    "test_3": test_3,
    "test_4": test_4,
    "test_5": test_5,
    "test_6": test_6,
    "test_7": test_7,
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
