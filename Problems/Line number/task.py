# read sample.txt and print the number of lines
test_file = open('sample.txt', 'r')
count = 0

for line in test_file:
    count += 1

print(count)
test_file.close()
