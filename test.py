import os


with open('movie_data_paths', 'r') as fp:
    for line in fp.readlines():
        folder = line.strip('\n')
        print("create a folder".format(line))
        os.makedirs(folder)


