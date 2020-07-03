# read sums.txt
test_file = open('sums.txt', 'r')

for line in test_file:
    number = line.split()
    print(int(number[0]) + int(number[1]))

test_file.close()
