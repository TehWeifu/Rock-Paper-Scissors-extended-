numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_test = open('file_with_list.txt', 'w')

print(numbers, end='', file=file_test)

file_test.close()
