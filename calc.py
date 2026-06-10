""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers=="":
        return 0
    return sum(int(number) for number in numbers.replace("\n",",").split(","))
