# read animals.txt
# and write animals_new.txt
read_file = open('animals.txt', 'r')
write_file = open('animals_new.txt', 'w')
names = []

for line in read_file:
    line = line.rstrip('\n')
    names.append(line)

for uwu in names:
    write_file.write(uwu + ' ')

read_file.close()
write_file.close()
