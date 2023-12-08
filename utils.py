def read_file(file_path):
    with open(file_path) as f:
        list_of_lines = f.readlines()
    return list_of_lines
