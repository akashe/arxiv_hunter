import os


def get_all_files_with_extension(folder_loc, extension):
    files = []

    for root, dirs, files in os.walk(folder_loc):
        for file in files:
            if file.endswith(extension):
                files.append(os.path.join(root,file))

    return files
