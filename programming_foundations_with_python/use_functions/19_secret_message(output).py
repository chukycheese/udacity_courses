import os

def rename_files():
    # 1. get file names from a given folder
    file_list = os.listdir(r'C:\Dev\udacity\programming_foundations_with_python\use_functions\prank\prank')

    saved_path = os.getcwd()
    print("Current working directory: " + saved_path)

    os.chdir(r'C:\Dev\udacity\programming_foundations_with_python\use_functions\prank\prank')

    # 2. for each file, rename filename
    for file_name in file_list[1:]:
        print("Old Name: " + file_name)
        os.rename(file_name, file_name.translate(str.maketrans("0123456789", "__________")).replace("_", ""))
        print("New Name: " + file_name)
        # print(file_name.translate(str.maketrans("0123456789", "__________")).replace("_", ""))

    os.chdir(saved_path)

rename_files()
