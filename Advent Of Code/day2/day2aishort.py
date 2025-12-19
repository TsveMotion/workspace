data = open("Advent Of Code/day2/day2.txt").read().strip().split(",")

total = 0
for r in data:
    L, R = map(int, r.split("-"))
    for l in range(len(str(L)), len(str(R)) + 1):
        if l % 2 == 0:
            for i in range(10**(l//2 - 1), 10**(l//2)):
                n = int(str(i) * 2)
                if L <= n <= R:
                    total += n

print(total)
