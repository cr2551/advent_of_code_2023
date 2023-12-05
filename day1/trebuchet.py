import os

# make sure the script works even when you don't run it from this directory
script_directory = os.path.dirname(os.path.abspath(__file__))
print(os.path.abspath(__file__))
print(script_directory)
file_path = os.path.join(script_directory, "input.txt")


def calibrate(file_path):
    """For each line of input text, grab the first and last digits, if there is only one digit then it will be repeate
    for it is both the first and last digit simoultaneosuly.
    ex: 
    h3jkk4hfj -> 34
    fdjs7jjjf  -> 77
    """

    numbers = []
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        while line:
            # print(line)
            nums = ''
            for char in line:
                # if a char is a digit add it to a new string of digits.
                if char.isdigit():
                    nums += char
            # when we have our sring of digits, redefine it to be only the first and last digit and convert it to an int
            nums = int(nums[0] + nums[-1])
            # append to numbers list
            numbers.append(nums)
            line = file.readline().strip()
        # print(numbers)
            
        print('Total is: ', sum(numbers))

        

calibrate(file_path)
    