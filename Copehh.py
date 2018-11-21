import os
import json

# First python script so be nice LOL 
# Source folder downloads unrard files and so on
SRC_FOLDER = 'download/'
# destination folder aka backup or whatever 
DEST_FOLDER = '//'

# path to the .uploads.json important 
def read_data():
    with open('/uploads.json') as f:
        data = json.load(f)
        return data

def write_data(added_files, uploaded_files):
    with open('/uploads.json', 'w') as f:
        json.dump(added_files+uploaded_files, f)

def main():
    all_downloads = os.listdir(SRC_FOLDER)
    all_uploads = read_data()
    added_files = []
    for file_name in all_downloads:
        if file_name not in all_uploads:
            if "mkv" == file_name.split(".")[-1]:
                print file_name.split('.')[-1]
                added_files.append(file_name)
                file = open(DEST_FOLDER+file_name, 'wb')
                with open(SRC_FOLDER+file_name, 'rb') as f:
                    while True:
                        byte = f.read(20480)
                        if not byte:
                            break
                        file.write(byte)
    write_data(added_files, all_uploads)

if __name__ == '__main__':
    main()
