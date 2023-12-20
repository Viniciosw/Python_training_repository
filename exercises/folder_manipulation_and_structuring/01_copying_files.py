# Importing the libraries
import shutil
import glob
import os

# Function to copy desired files and folders to another destination
def copying_files(directory):

    # Defining the root directory we are searching for, and...
    # /**/*.* refers to capturing all files
    files_path = f'{directory}/**/*.*'

    # Defining the destination root for our files
    root_destiny = '.\\final_folder\\first_result\\'

    # Using glob to capture file paths
    path_files_found = glob.glob(files_path, recursive = True)

    # Breaking down the paths to make it possible to capture specific folders or files
    path_pieces = [piece.split('\\') for piece in path_files_found]

    # Capturing only the folders named 'example'
    roots_destiny = [piece[1] + '\\' for piece in path_pieces]

    # Variation of the roots_destiny
    # Example: path[:2] is ['initial_folder', 'example_01'] and [path[-1][:-4], path[-1]] is 'apple_01', 'apple_01.txt'
    #roots_destiny = [path[:2] + [path[-1][:-4], path[-1]] for path in path_pieces]
    
    # Defining the destination path for each of the files
    roots_destiny = [root_destiny + path for path in roots_destiny]

    # Merging the respective indices of path_files_found e roots_destiny
    final_paths = list(zip(path_files_found, roots_destiny))

    # Creating the directories where the files will be stored
    [os.makedirs(os.path.dirname(path), exist_ok = True) for path in roots_destiny]

    # Copying the files to their destination
    # root, dirs, files
    [shutil.copy(path[0], path[1]) for path in final_paths]


# The passed parameter is the root of the directory we want to work with on this occasion
copying_files('initial_folder')