import os


def add(a,b):
    return a+b


def count_lines(path):
    file = open(path, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count


def poppunk_assign(path):
    os.system('''
    cd %s
    poppunk_assign --db GPS_v4 --query input_data/qfile.txt --output poppunk_clusters_flask --threads 4
    '''
    %path)
    return path+"/poppunk_clusters_flask"
