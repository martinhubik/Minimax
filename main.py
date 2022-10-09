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
    return numbers


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
    Output methods
'''

def get_lowest_num(numbers):
    print("lowestNum + index")

def get_highest_num(numbers):
    print("highestNum + index")

def sort_numbers(numbers):
    print("sorted list + algo choice impl")





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
                    print(sys.argv[number] + " Not a number!")
                    break
                numbers.append(sys.argv[number])
            print(numbers)
    if (len(sys.argv) == 1):
            numbers = generate_pseoudorandom_array(ARRAY_LEGTH, GROUND_VALUE, TOP_VALUE)


    # Output





if __name__ == '__main__':
    main()


