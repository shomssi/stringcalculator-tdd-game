""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers=="":
        return 0
    delimiter =","
    parts=["", numbers]
    if numbers.startswith("//"):
        parts=numbers.split("\n", 1)
        delimiter=parts[0][2:]
    return sum(int(number) for number in parts[1].replace("\n",delimiter).split(delimiter))
