# Importing the libraries
import os
import glob

# Function to save the paths of empty files in a txt
def saving_paths_empty_files(directory):
    
    # Creating the txt file
    with open('.\\final_folder\\files_empty.txt', 'w') as txt_file:

        # Defining the root directory we are searching for, and
        # /**/*.* pertains to capturing all paths
        name_paths_to_delete = f'{directory}/**/*.*'

        # Using glob to capture file paths
        paths_to_delete = glob.glob(name_paths_to_delete, recursive = True)

        # Printing the paths of empty files
        #[print(path) for path in paths_to_delete if os.path.getsize(path) == 0]

        # Storing the paths of empty files in a txt
        txt_file.write('\n'.join(path for path in paths_to_delete if os.path.getsize(path) == 0))


# Function to delete empty files
def deleting_empty_files(directory):

    # Defining the root directory we are searching for, and
    # /**/*.* pertains to capturing all files
    name_files_to_delete = f'{directory}/**/*.*'

    # Using glob to capture file paths
    files_to_delete = glob.glob(name_files_to_delete, recursive = True)

    # Deleting the empty files
    [os.remove(path) for path in files_to_delete if os.path.getsize(path) == 0]

    # Defining the root directory we are searching for, and
    # /**/*.* pertains to capturing all paths
    name_paths_to_delete = f'{directory}/**/'

    # Using glob to capture paths
    paths_to_delete = glob.glob(name_paths_to_delete, recursive = True)

    # Deleting the empty dirs
    # os.path.isdir(path): checks if the path 'path' refers to a directory
    # not os.listdir(path): checks if the directory at path is empty, i.e., it does not contain any files or subdirectories
    [os.rmdir(path) for path in paths_to_delete if os.path.isdir(path) and not os.listdir(path)]


# The passed parameter is the root of the directory we want to work with on this occasion
saving_paths_empty_files('final_folder\\first_result')

# The passed parameter is the root of the directory we want to work with on this occasion
deleting_empty_files('final_folder\\first_result')