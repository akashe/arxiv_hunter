import os


def get_all_files_with_extension(folder_loc, extension):
    total_files = []

    for root, dirs, files in os.walk(folder_loc):
        for file in files:
            if file.endswith(extension):
                total_files.append(os.path.join(root,file))

    return total_files
