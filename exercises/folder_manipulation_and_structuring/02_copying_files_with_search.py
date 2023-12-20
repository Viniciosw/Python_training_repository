# Importing the libraries
import shutil
import os
import glob

# Copying to another folder only the files that contain 'blue' in the name
def copying_files_with_search(directory, search):

    # Defining the root directory and the word we are looking for in the files or path
    partial_path = f'{directory}/**/*{search}*'
    
    # Defining the destination root for our files
    root_destiny = '.\\final_folder\\second_result\\'

    # Using glob to capture file paths
    path_files_found = glob.glob(partial_path, recursive = True)

    # Breaking down the paths to make it possible to capture specific folders or files
    path_pieces = [piece.split('\\') for piece in path_files_found]

    # Capturing only the 'example' folders
    roots_destiny = [piece[1] + '\\' for piece in path_pieces]

    # Defining the destination path for each of the files
    roots_destiny = [root_destiny + path for path in roots_destiny]

    # Merging the respective indices of path_files_found e roots_destiny
    final_paths = list(zip(path_files_found, roots_destiny))

    # Creating the directories in which the files will be stored
    [os.makedirs(os.path.dirname(path), exist_ok = True) for path in roots_destiny]

    # Copying the files to their destination
    # root, dirs, files
    [shutil.copy(path[0], path[1]) for path in final_paths]

# The passed parameters are the root of the directory we want to work with and the part of the word we are looking for
copying_files_with_search('initial_folder', 'blue')