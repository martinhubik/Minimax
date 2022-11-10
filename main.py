import sys
from random import randint

'''
    Input operation methods
'''

def input_file(filename):
    numbers_file = open(filename, "r")
    numbers = numbers_file.readlines()[0]
    numbers_file.close()

    numbers = numbers.rsplit(' ')
    numbers_int = [eval(number) for number in numbers]
    return numbers_int


'''
    Pseudorandom generator settings
'''

ARRAY_LEGTH = 20
GROUND_VALUE = -1000
TOP_VALUE = 1000

def generate_pseoudorandom_array(array_length, ground_value, top_value):
    numbers = []
    for number in range (1, array_length):
        numbers.append(randint(ground_value, top_value))
    return numbers

'''
    Sorting algorithms
'''

def bubble_sort(list):
    list_lenght = len(list)
    for number in range(list_lenght - 1, 0, -1):
        for index in range(number):
            if list[index] > list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp
    return list

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


def insertion_sort(list):
    # Traverse through 1 to len(list)
    for i in range(1, len(list)):

        key = list[i]

        # Move elements of list[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list
'''
    Output methods
'''

def get_lowest_num(numbers):
    return min(numbers)
def get_highest_num(numbers):
    return max(numbers)

def sort_numbers(numbers):
    choice_made = False
    while(not choice_made):
        print("Please choose an algorithm to sort the numbers:\n1)Bubble Sort - 1\n2)Insertion Sort - 2\n3)Merge Sort - 3")
        sorting_algorithm = input()
        match sorting_algorithm:
            case "1":
                choice_made = True
                numbers = bubble_sort(numbers)
            case "2":
                choice_made = True
                numbers = insertion_sort(numbers)
            case "3":
                choice_made = True
                numbers = merge_sort(numbers)
            case _:
                print("Please enter the algorith number")
    return numbers

'''
    Program settings
'''



def main():

    # Input logic

    if (len(sys.argv) > 1):
        if (len(sys.argv) == 2 and sys.argv[1].endswith(".txt")):
            numbers = input_file(sys.argv[1])
        else:
            numbers = []
            for number in range(1, len(sys.argv)):
                try:
                    int(sys.argv[number])
                except:
                    print(sys.argv[number] + " Not an INT!")
                    break
                numbers.append(sys.argv[number])
            print(numbers)
    if (len(sys.argv) == 1):
            numbers = generate_pseoudorandom_array(ARRAY_LEGTH, GROUND_VALUE, TOP_VALUE)



    # Output
    print("Unsorted: ")
    print(numbers)
    sort_numbers(numbers)
    print(f"Lowest number: {get_lowest_num(numbers)}")
    print(f"Highest number: {get_highest_num(numbers)}")
    print("Sorted list: ")
    print(numbers)



if __name__ == '__main__':
    main()


