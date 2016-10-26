import filecmp

def compare_files(file_1, file_2):
    return filecmp.cmp(file_1, file_2)

