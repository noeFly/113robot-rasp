from os import makedirs as md
from os.path import exists as exist
from zipfile import ZipFile


def unzip(file_path: str, folder_name: str, file_name: str) -> None:
    if not exist(file_path):
        md(f'{file_path}/{folder_name}')
    with ZipFile(file=f'{file_path}/{file_name}', mode='r') as zipp:
        zipp.extractall(path=f'{file_path}/{folder_name}')
