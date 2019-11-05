intro = """
Program using Stack structure for sorting integers
Author: Anh Trung Nguyen Vu
Date: 2 November 2019
Instruction: Algorithm course of Master 1 Bordeaux
"""

print(intro)
# Entry data for sorting , change to next value with COMMA character
base_stack = input("Setting up your UN-ORDERED stack using COMMA for separator: \n").split(",")

# Generate TWO Auxiliary Stacks for sorting Algorithm
aux_premier = []
aux_second = []

# Add new element to the top of the stack
def push2top(value, stack):
    return stack.append(value)

# Remove the top of the stack
def remove_top(value, stack):
    stack.pop()
    return stack

# Get the top of the stack
def top_value(stack):
    return stack.pop()

def compare_top(stack_one, stack_second):
    one = stack_one.pop()
    second = stack_second.pop()
    # case Top of two stack are equal:
    if one == second:
        return 0
    if one > second:
        return 1
    else:
        return 2
