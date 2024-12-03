
with open("input.txt", "r") as f:
    lines = [x.split() for x in f.readlines()]


left_list = sorted(int(x[0]) for x in lines)
right_list = sorted(int(x[1]) for x in lines)


sum = 0
for left, right in zip(left_list, right_list):
    sum += abs(left - right)

print("part 1:", sum)


right_lookup = {n: right_list.count(n) for n in right_list}

score = 0
for left in left_list:
    if left in right_lookup:
        score += left * right_lookup[left]

print("part 2:", score)