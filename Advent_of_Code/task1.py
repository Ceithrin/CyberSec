try:
    f = open("task1input.txt", 'r')
    array = []
    for line in f: # read rest of lines
        array.append([int(x) for x in line.split()])
    print(array)
    print(array[1][0])
    counter = 0
    for x in range(len(array)-3):
        if array[x][0] + array[x+1][0] + array[x+2][0] < array[x+1][0] + array[x+2][0] + array[x+3][0]:
            counter += 1
    print(counter)
finally:
   f.close()