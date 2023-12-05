# do something similar as in part1 trebuchet but also counting `one` or `two` etc instead of just digits.
import os
script_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_path, 'input.txt')

def calibrate(file_path):
    total = 0
    digits_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    file = open(file_path, 'r')
    line = file.readline().strip()
    while line:
        line_length = len(line)
        first_digit = get_digit(line, 0, line_length, 1)
        last_digit = get_digit(line, line_length - 1, -1, -1)
        total += int(first_digit + last_digit)

        line = file.readline().strip()
    file.close()
    print(total)
    return total

def get_digit(line, start, end, step):
    
    digits_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in range(start, end, step):
        break_outer_loop = False
        # if char is digit then append it
        if line[i].isdigit():
            return line[i]
        else:
        # otherwise check if it the start of a string representation of a digit. i.e compare it and the following chars
        # to the keys in digits_dict
            for key in digits_dict:
                # grab the substring from i up to (but not including) i+ length of the key. ex 'five' length is 4. 
                end = i + len(key)
                # prevent IndexError
                if end <= len(line):
                    if line[i : end] == key:
                        return str(digits_dict[key])
                        # flag to break out of the outer for loop as well
        if break_outer_loop:
                break


calibrate(file_path=file_path)
