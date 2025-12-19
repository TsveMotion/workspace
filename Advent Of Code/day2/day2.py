myfile = open("Advent Of Code/day2/day2.txt", "r")
data = myfile.read().strip()
arr = data.split(",")
myfile.close()

arr_left = []
arr_right = []

def digits_in_between():
    for items in arr:
        left, right = items.split("-")
        arr_left.append(int(left))
        arr_right.append(int(right))
    return arr_left, arr_right

def itteration_between_limits(left, right):
    for i in range(len(left)):
        number1 = left[i]
        number2 = right[i]
        print(number1)
        print(number2)

left, right = digits_in_between()
itteration_between_limits(left, right)
