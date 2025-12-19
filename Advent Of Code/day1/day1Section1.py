myfile = open("Advent Of Code/day1/day1.txt", "r")  # open day1.txt, which contains input from AoC
arr = []  # create a blank array
for line in myfile:  # go through each line in the file
    arr.append(line.strip())  # add each line to the array

num = 50  # starting dial position
length_of_array = len(arr)

number = 0
direction = ""
number_start = 50  # dial starts at 50
value_total = 0  # password counter


for item in arr:

    direction = item[:1]       # get L or R
    number = int(item[1:])     # number of clicks

    if direction == "R":
        number_start = (number_start + number) % 100
    elif direction == "L":
        number_start = (number_start - number) % 100

    #only check AFTER rotation finishes
    if number_start == 0:
        value_total = value_total + 1


print(value_total)
