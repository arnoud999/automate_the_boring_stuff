import os
import zipfile
import re

def backupToZip(folder):
    """Backup the entire contents of folder to folder_X.zip"""

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1

    # Create the zip file
    newZip = zipfile.ZipFile(zipfilename, 'w')
    newZip.write(os.path.listdir(folder), compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

