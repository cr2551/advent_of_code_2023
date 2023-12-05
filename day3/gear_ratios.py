
file_path = 'input.txt'
test_input = 'test.txt'

def is_symbol(character: str) -> bool:
    """Determine if `character` is any symbol that is not a period"""
    return (not character.isalnum()) and (character != '.')


# we need to get a list of the indexes adjacent to each number and check those for symbols
# we need to handle cases where the number or char is in the first/last row, first/last column or in a corner
def get_part_numbers(array: list) -> list:
    """Go through each col for each row and append the valid part numbers to a list.
    Return the list of valid part numbers"""
    # when we detect a digit follow the trail until we stop getting digits.
    # then get the indexes of those chars adjacent to num
    # go through the array and and detect the number and the box around it to check those indexes for symbols
    row = 0
    col = 0
    nums = []
    while row < len(array):
        col = 0
        while col < len(array[row]):
            current_num = ''
            offset = -1
            for col_index in range(col, len(array[row])):
                char = array[row][col_index]

                if char.isdigit():
                    current_num += char
                    offset += 1
                else:
                    break

            if current_num:
                if is_part_number(array, row, col, offset):
                    nums.append(int(current_num))

            col = col_index
            # go to next col/char
            col += 1

        # go to next row
        row += 1

    return nums


def create_2d_array(file_path):
    """Read file and convert it into a 2d array where each row is a line in the file 
    and each column is a character in that line.
    """
    with open(file_path, 'r') as file:
        array = []
        line = file.readline().strip()
        while line:
            array.append(line) 
            line = file.readline().strip()
    return array


def is_part_number(array, row, col, offset):
    # offset = offset - 1
    """Determine if a a num is a part number by checking the adjacent indeces for symbols"""
    # i will use i var to add to the row and j var to add to the col
    for i in range(-1, 2):
        new_row = row + i
        if (new_row >= 0) and (new_row < len(array)):
            # print(new_row)
            for j in range(-1, 2):
                if (col + j) >= 0 and (col + j) < len(array[row]):
                    # print(col+j)
                    if is_symbol(array[new_row][col + j]):
                        return True

                if (col + offset + j) >= 0 and (col + offset + j) < len(array[row]):
                    if is_symbol(array[row+i][col + offset + j]):
                        return True


def main():
    # arr = create_2d_array(file_path=test_input)
    arr = create_2d_array(file_path=file_path)
    parts_list =  get_part_numbers(arr)
    print(parts_list)
    total = sum(parts_list)
    print(total)
    return total


if __name__ == '__main__':
    main()

