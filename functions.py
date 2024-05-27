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
