# a simple movie renamer:
# Python3 only

import sys
import os
import re
import glob
import argparse

# function to rename movie
def rename_movie(fn: str, debug: bool) -> str:

    # save path name of the original file
    file_path = os.path.dirname(fn)

    # split file name to get the base name
    file_name = os.path.basename(fn)
    (file_basename, file_ext) = os.path.splitext(file_name)

    # replace all regexes
    for reg in regs:
        # save original pattern and replacement regex
        (pattern, repl) = reg

        # replace pattern in the base name
        file_basename = re.sub(pattern, repl, file_basename)
        if debug: 
            print(file_basename)

    # build new name
    new_name = "{0}{1}".format(file_basename.strip(), file_ext)

    return('{0}/{1}'.format(file_path, new_name))



# list of regexes to be substituted
regs = [
    [r'(19\d\d)', r'(\1)'],
    [r'(20\d\d)', r'(\1)'],
    [r'\[.*?\]', ''],
    [r'(?i)bdrip', ''],
    [r'(?i)french', ''],
    [r'(?i)vostfr', ''],
    [r'(?i)h264', ''],
    [r'(?i)ita', ''],
    [r'(?i)episodio', ''],
    [r'(?i)x264.*', ''],
    [r'(?i)dvdrip.*', ''],
    [r'(?i)xvid.*', ''],
    [r'(?i)brrip.*', ''],
    [r'(?i)720p', ''],
    [r'(?i)hdlight', ''],
    [r'(?i)1080p', ''],
    [r'(?i)true', ''],
    [r'(?i)multi', ''],
    [r'(?i)bluray', ''],
    [r'(?i)web', ''],
    [r'(?i)weeds', ''],
    [r'(?i)hdtv.*', ''],
    [r'\-', ''],
    [r'_', ' '],
    [r'\.', ' '],
]

# manage arguments
parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true',
                    default=False,
                    dest='debug',
                    help='watch regexes substitutions')

parser.add_argument('-f', 
                    dest='files',
                    help='List of files',
                    nargs='*')                                                  

args = parser.parse_args()

# if we're on Linux or any Unix shell, glob expansion is made before the script is called. No need to call glob function.
if os.name == 'posix':
    files_to_rename = args.files
elif os.name == 'nt':
    files_to_rename = glob.glob(args.files)

# for each argument (which is supposed to be a file name), get new name and rename file
for fn in files_to_rename:
    # rename file
    new_name = rename_movie(fn, args.debug)

    # rename file if any
    answer = input('Do you want to rename "{0}" by "{1}" ? (Y/N): '.format(fn, new_name))
    if answer.lower().startswith('n'):
        continue
    else:
        if not args.debug:
            os.rename(fn, new_name)




