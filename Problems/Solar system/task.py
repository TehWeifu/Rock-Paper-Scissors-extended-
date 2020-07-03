# create the planets.txt
test_file = open("planets.txt", 'w')
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for i in planets:
    test_file.write(i + '\n')

test_file.close()
