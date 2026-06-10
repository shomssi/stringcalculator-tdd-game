""" Edit the function below to implement the String Calculator TDD Kata """
import re
def add(numbers):
    numbers = re.findall(r'-?\d+',text)
    sum = 0
    if numbers:
        count = 0
        for i in numbers:
            count++
            if i<=1000 and i>=0:
                sum+=i
            if count>2:
                break
    return sum
