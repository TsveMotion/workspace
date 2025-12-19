myfile = open("Advent Of Code/day1/day1.txt", "r")  # open day1.txt, which contains input from AoC
arr = []  # create a blank array
for line in myfile:  # go through each line in the file
    arr.append(line.strip())  # add each line to the array

num = 50  # starting dial position
length_of_array = len(arr)

number = 0
direction = ""
number_start = 50  # dial starts at 50
value_total = 0  # value counter


for item in arr:

    direction = item[:1]    # get L or R
    number = int(item[1:])  # number of clicks

    if direction == "R":
        direction_value = 1
    elif direction == "L":
        direction_value = -1

    # PART 2: move dial one click at a time
    for i in range(number):
        number_start = (number_start + direction_value) % 100

        # count EVERY time dial hits 0
        if number_start == 0:
            value_total = value_total + 1


print(value_total)
