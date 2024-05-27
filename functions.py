#
# # def - function def - inition(izveidot pasu savu funkciju)
# # blueprint - projekts funkcijas
# # pec def funkcijas jabut divam rindam brivam!!!
# # return ir pedejais funkcijai(neko pectam nevaram rakstit)
# #() mute, return ir dibens
#
# def hello_world() -> str:
#     return "Hello, World"
#
#
# greetings = hello_world()
#
#
# print(greetings)
# print(hello_world())
#
#
# def get_introduction() -> str:
#     return "My name is Kaspars"
#
#
# print(get_introduction())
#
#
# def get_age() -> int:
#     return 35
#
#
# print(get_age())
#
#
#
# def get_greeting() -> str:
#
#     return f'{get_introduction()}, i am {get_age()}'
#
#
# print(get_greeting())

# parametri vai argumenti lidz 4
def add_numbers(number_1: str, number_2: str) -> float:
    result = float(number_1) + float(number_2)
    return result


def take_numbers(number_1: str, number_2: str) -> float:
    result = float(number_1) - float(number_2)
    return result


def multiply_numbers(number_1: str, number_2: str) -> float:
    result = float(number_1) * float(number_2)
    return result


def divide_numbers(number_1: str, number_2: str) -> float:
    result = float(number_1) / float(number_2)
    return result


# ctrl + alt + L = formate kodu pec stila

def calculate(operation, number_1, number_2) -> float:
    if operation == "+":
        result: float = add_numbers(number_1, number_2)

    elif operation == "-":
        result: float = take_numbers(number_1, number_2)
    elif operation == "*":
        result: float = multiply_numbers(number_1, number_2)
    elif operation == "/":
        result: float = divide_numbers(number_1, number_2)
    else:
        result: str = "symbols only"

    return result
