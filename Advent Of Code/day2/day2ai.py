myfile = open("Advent Of Code/day2/day2.txt", "r")
data = myfile.read().strip()
arr = data.split(",")
myfile.close()

def is_invalid(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def sum_invalid_ids(arr):
    total = 0

    for item in arr:
        left, right = item.split("-")
        left = int(left)
        right = int(right)

        min_len = len(str(left))
        max_len = len(str(right))

        for length in range(min_len, max_len + 1):
            if length % 2 != 0:
                continue

            half = length // 2
            start = 10 ** (half - 1)
            end = 10 ** half

            for i in range(start, end):
                num = int(str(i) * 2)
                if left <= num <= right and is_invalid(num):
                    total += num

    return total

print(sum_invalid_ids(arr))
