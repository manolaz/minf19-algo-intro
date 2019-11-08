from collections import deque
import  operator

intro = """
Program using Stack structure for sorting integers
Author: Anh Trung Nguyen Vu
Date: 2 November 2019
Instruction: Algorithm course of Master 1 Bordeaux
"""

sorting_order_guide = """
Sorting selection use:
[ 1 ] => INCREASE ordering
[ 2 ] => DECREASE ordering
"""

# Use DEQUE as base struture for STACK construction
def new_stack():
    return deque()

# checking if a stack is empty or having elements
def is_empty(stack):
    return len(list(stack)) == 0

# Add new element to the top of the stack
def push(value, stack):
    return stack.append(value)

# Remove the top of the stack
def pop(stack):
    if len(stack) > 0:
        stack.pop()

# Get the top of the stack
def top_value(stack):
    return stack[-1]

# Chosing the sorting order
def sort_config(choice, one, two):
    if choice == 1:
        return operator.gt(one, two)
    if choice == 2:
        return operator.lt(one, two)

# Sorting the entry_stack to an order on choice
def sort_stack(origin, sort_order):
    # Generate TWO Auxiliary Stacks for sorting Algorithm
    auxiliary = new_stack()
    # Run the Algorithm until the Entry Stack become empty
    while (is_empty(origin) == False):
        tempo = top_value(origin)
        pop(origin)

        # the condition for sorting
        while ((is_empty(auxiliary) == False) and
                sort_config(sort_order, top_value(auxiliary), tempo)):
            # Moving AUX => ORIGIN
            push(top_value(auxiliary), origin)
            pop(auxiliary)

        # Moving ORIGIN  => AUX
        push(tempo, auxiliary)
        # Tracing the changes of Auxiliary stack
        print("AUX : {}".format(auxiliary))
    # Result of Algorithm stored on the AUX stack
    return auxiliary

# The MAIN function
def main():
    # Present the Program
    print(intro)
    print("Give your stack of INTERGERS  , stop by ZERO value: \n")
    elem = 1
    # Entry data for sorting , stop data enter by ZERO
    base_stack = new_stack()
    while elem > 0:
        elem = int(input("element = "))
        if elem != 0:
            push(elem, base_stack)
    print("Entry Stack : \n {}.".format(base_stack))

    # Chosing your sort Order
    choice_sort_order = int(input(sorting_order_guide))
    # Init the result
    sorted_stack = new_stack()
    # Run the sorting Algorithm
    try:
        sorted_stack = sort_stack(base_stack, choice_sort_order)
    except Exception as e:
        print(e)
    # View result
    if sorted_stack:
        print("Sorted Stack : \n {}".format(sorted_stack))

# Bootstrapping the program execution
if __name__ == "__main__":
    main()
