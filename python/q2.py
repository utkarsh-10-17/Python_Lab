total = 0
count = 0
max1=0
min1=0


with open('file.txt', 'r') as file:
    for line in file:
        val = int(line.strip())
        total += val
        if val > max1:
            max1 = val
        if val < min1:
            min1 = val
        count += 1
        

if count > 0:
    average = total / count
else:
    average = 0


print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {max1}")
print(f"Minimum: {min1}")
