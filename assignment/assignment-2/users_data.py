import csv

def user_file_writer(file_name, content):
    writer = open(file_name, "a", encoding="utf-8")
    writer.write(f"{content}\n")
    writer.close()
    return None

def write_csv_file(file_name, row):
    file_writer = open(file_name,'a', encoding="utf-8", newline="\n")
    csv_file_writer = csv.writer(file_writer)
    csv_file_writer.writerow(row)
    file_writer.close()

def read_csv_file(file_name):
    content = []
    file_reader = open(file_name, 'r', encoding="utf-8")
    csv_file_reader = csv.reader(file_reader)
    for row in csv_file_reader:
        content.append(row)
    return content

def user_file_reader(file_name):
    content = []
    reader = open(file_name, "r", encoding="utf-8")
    while True:
        line = reader.readline()
        if line:
            content.append(line)
        else:
            break
    reader.close()
    return content

