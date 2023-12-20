# Importing the libraries
import os
import glob
import re
from unidecode import unidecode

# Function to fix the name of files and folders
def fixing_files_and_folders_names(directory):
    
    # Defining the root directory we are searching for, and
    # /**/*.* pertains to capturing all files
    name_paths_to_fix = f'{directory}/**/*.*'

    # Using glob to capture file paths
    paths_to_fix = glob.glob(name_paths_to_fix, recursive = True)

    # Using rename, re and unidecode to fix the filenames and paths
    [os.rename(path, re.sub(r'\s+', '_', unidecode(path))) for path in paths_to_fix]


# The passed parameter is the root of the directory we want to work with on this occasion
fixing_files_and_folders_names('final_folder\\first_result')