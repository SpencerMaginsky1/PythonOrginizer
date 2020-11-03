import os
import collections
from pprint import pprint

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
EXT_IMGS  = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif']
EXT_DOCS  = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso']





# Step 1 - (Optional) Create directories where we want to store the files
BASE_PATH = os.path.expanduser('~')


# Step 2 - Map files from Downloads folder based on their file extension
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)

pprint(files_mapping)

# Step 3 - Move all files given a file extension to a target directory
for f_ext, f_list in files_mapping.items():

    if f_ext in EXT_INSTL:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'OrginizedDownloads/Applications', file))

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'OrginizedDownloads/Music', file))

    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'OrginizedDownloads/Movies', file))

    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'OrginizedDownloads/Pictures', file))

    elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'OrginizedDownloads/Documents', file))

    else:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'OrginizedDownloads/Other', file))