import os


def stringy(file_list):
    counter = 0
    for file in file_list:
        counter = counter + 1
        name = str(counter) + '.txt' 
        temp_file = []
        with open(file, 'r') as f:
            for line in file:
                temp_file.append(line)
        with open(name, 'a') as f:
            for line in temp_file:
                f.write(line + '\n')

            
stringy(['config.php', 'dumbass.php', 'idiot.php'])