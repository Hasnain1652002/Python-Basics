list = ['abc', 'xyz', 'aba', '1221']
count = 0
for element in list:
    if len(element) >= 2 and element[0] == element[-1]:
            count += 1
print(count)