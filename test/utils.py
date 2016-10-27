import filecmp
import os

def compare_files(file_1, file_2):
    # compares the contents of two files, returns true if they're the same
    return filecmp.cmp(file_1, file_2)

def clean_output():
    output_dir = 'test/integration/outputs'
    # files that shouldn't be deleted
    keepers = [
        '__init__.py',
    ]

    output_contents = os.listdir(output_dir)
    for file_name in output_contents:
        if file_name not in keepers:
            os.remove(
                os.path.join(
                    output_dir, file_name
                )
            )

def file_exists(path):
    # returns true if path exists
    return os.path.isfile(path)
