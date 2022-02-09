import zipfile
import json


def read_zip_file(file_path):
    zip_file = zipfile.ZipFile(file_path)
    for file_info in zip_file.infolist():
        file = zip_file.open(file_info)
        read_json_file(file)


def read_json_file(file):
    data = json.load(file)
    for i in data['track']:
        print(i)
    file.close()

