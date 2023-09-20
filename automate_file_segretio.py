import os, glob

# This assumes that this code is run inside
# the directory with the image files

# Path to the directory you will store
# the directories with files (current here)
path_to_files = os.getcwd()
objectcodes = ['QQS Eur F699-1', 'BL RL4_QRS Eur F699-1-2-7-5_379' ]

# For each objectcode
for obc in objectcodes:
    # Make a directory if it doesn't already exist
    file_dir = os.path.join(path_to_files, obc)
    if not os.path.isdir(file_dir):
        os.mkdir(file_dir)
        # If you need to set the permissions
        # (this enables it all - may not be what you want)
        os.chmod(file_dir, 0o777)

    # Then move all the files that have that objectcode
    # in them and end with *.jpeg to the correct dir
    for fname in glob.glob('*' + obc + '*.jpg'):
        # Move the file
        os.rename(fname, os.path.join(file_dir, fname))