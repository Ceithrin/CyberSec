try:
    f = open("task2input.txt", 'r')
    array = []
    for line in f: # read rest of lines
        array.append([x for x in line.split()])
    print(array[1][0], array[1][1])
    horizontal = 0
    depth = 0
    aim = 0
    for element in array:
        if element[0] == 'forward':
            horizontal += int(element[1])
            depth += int(element[1])*int(aim)
        elif element[0] == 'down':
            aim += int(element[1])
        elif element[0] == 'up':
            aim -= int(element[1])
    print(horizontal, depth, horizontal*depth)
finally:
   f.close()