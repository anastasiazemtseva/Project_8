import time

print('Choose a binary search method:')
print('1. Iteration;')
print('2. Recursion.')
choice = int(input())

if choice == 1:
    start = time.time()


    def BiSearch_iterator(list, number):
        '''

        :param list: list of non-decreasing integers
        :param number: required element
        :return: index of the first occurrence of the specified item
        '''

        first = 0
        final = len(list) - 1
        while first <= final:
            middle = (first + final) // 2

            # The value of the middle element is compared with the desired value.
            # If the value is larger, the comparison will occur on the right side.
            if number > list[middle]:
                first = middle + 1
            # If the value is less - in the left.
            elif number < list[middle]:
                final = middle - 1
            # If equal returns the middle element of the list.
            else:
                return middle
        else:
            return None


    list = [1, 2, 3, 23, 45, 56, 67, 99, 121, 133, 155, 177,
            234, 567, 789, 799, 800, 899, 956, 1232, 2346]
    number = 155
    print(BiSearch_iterator(list, number))
    print(f"{(time.time() - start)} sec.")


elif choice == 2:
    start = time.time()


    def BiSearch_recursion(list, number):
        '''

        :param list: list of non-decreasing integers
        :param number: required element
        :return: index of the first occurrence of the specified item
        '''

        middle = len(list) // 2
        if len(list) == 0:
            return None
        else:
            # The value of the middle element is compared with the desired value.
            # If the value is less, the comparison will occur on the left side.
            if number < list[middle]:
                return BiSearch_recursion(list[:middle], number)
            # If the value is larger, in the right.
            elif number > list[middle]:
                return len(list[:middle]) + BiSearch_recursion(list[middle:], number)
            # If equal returns the middle element of the list.
            else:
                return middle


    list = [1, 2, 3, 23, 45, 56, 67, 99, 121, 133, 155, 177,
            234, 567, 789, 799, 800, 899, 956, 1232, 2346]
    number = 133
    print(BiSearch_recursion(list, number))
    print(f"{(time.time() - start)} sec.")

else:
    print('Try again.')
