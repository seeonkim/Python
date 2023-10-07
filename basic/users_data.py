
def user_file_writer(file_name, content):
    writer = open(file_name, "a", encoding="utf-8")
    writer.write(f"{content}\n")
    writer.close()
    return None



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