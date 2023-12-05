# file_path = 'sample_input.txt'
file_path = 'input.txt'

from gear_ratios import create_2d_array

def calc_gear_ratios():
    gear_ratios = []
    array = create_2d_array(file_path)
    for row in range(len(array)):
        col = 0
        while col < len(array[row]):
            char = array[row][col]
            if char == '*':
                gear_ratios.append(gear_ratio(array, row, col))
            col += 1
    return gear_ratios

    


def gear_ratio(array, row, col):
    """given the row and col of a `*` determine if it is a gear by checking if it is adjecent to 
    exactly 2 numbers"""
    adjacent_numbers = detect_adjacent_numbers(array, row, col)
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    else:
        return 0



def detect_adjacent_numbers(array, row, col):
    """give the row and col of a `*` look for adjacent numbers"""
    # look in the 3x3 matrix where * is the center, for digits
    adjacent_numbers = []
    for i in range(-1, 2):
        # list used to store the colum indeces of the number
        num_indeces = []
        if (row + i) >= 0 and (row + i) < len(array[row]):
            for j in range(-1, 2):
                if (col + j) >= 0 and (col + j) < len(array[row]):
                    char = array[row + i][col + j]
                    if char.isdigit():
                        # i need to avoid calling this function for digits which form part of the same number
                        if (col + j) not in num_indeces:
                            number, num_indeces = get_number(array, row + i, col + j)
                            adjacent_numbers.append(number)
    return adjacent_numbers

    
def get_number(array, row, col):
    """Given the location of a digit follow it backwards until char is no longer a digit
    at that point go forwards to get the full number"""
    # store the indeces of each digit that's in the number and return this list
    # it will be useful later to avoid callin the same function on the same number
    num_indeces = []
    char = array[row][col]
    left_offset = 0
    # go bakcwards
    while char.isdigit():
        left_offset += 1
        if (col - left_offset) >= 0:
            char = array[row][col - left_offset]
        else:
            break
    # col will now be the first digit of the number
    # we need to add a plus one because left offset will be one place behind the start of digits.l
    col = col - left_offset + 1
    # now go forwards
    right_offset = 0
    number = ''
    char = array[row][col]

    while char.isdigit():
        number += char
        num_indeces.append(col + right_offset)
        right_offset += 1
        # if the last char in a row is a digit then the while loop will never stop unless we break
        if (col + right_offset) < len(array[row]):
            char = array[row][col + right_offset]
        else:
            break
    return int(number), num_indeces



def main():
    gear_ratios = calc_gear_ratios()
    total = sum(gear_ratios)
    print(total)


if __name__ == '__main__':
    main()



        


