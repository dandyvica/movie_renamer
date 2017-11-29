# a simple movie renamer:
# Python3 only

import sys
import os
import re

# list of regexes
regs = [
    [r'(19\d\d)', r'(\1)'],
    [r'(20\d\d)', r'(\1)'],
    [r'\[.*?\]', ''],
    [r'bdrip(?i)', ''],
    [r'french(?i)', ''],
    [r'x264.*(?i)', ''],
    [r'dvdrip.*(?i)', ''],
    [r'xvid.*(?i)', ''],
    [r'brrip.*(?i)', ''],
    [r'\.', ' '],
]

# useful debug to watch for regexes substitutions
debug = False
if os.environ.get('MVRDBG') is not None:
    debug = True

# function to rename movie
def rename_movie(fn: str) -> str:

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


# for each argument (which is supposed to be a file name), get new name and rename file
for fn in sys.argv[1:]:
    # rename file
    new_name = rename_movie(fn)

    # rename file if any
    answer = input('Do you want to rename "{0}" by "{1}" ? (Y/N): '.format(fn, new_name))
    if answer.lower().startswith('n'):
        continue
    else:
        if not debug:
            os.rename(fn, new_name)




