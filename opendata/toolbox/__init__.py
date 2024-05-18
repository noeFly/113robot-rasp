from datetime import datetime as dt
from os import listdir, makedirs
from os.path import exists
from shutil import rmtree


def log(level: int = 0, source: int = None, message: str = None) -> None:
    log_level = [' Info', ' Warn', 'Error', 'Debug']
    log_source = ['dev', 'opendata', 'sam', 'tool_box', 'way_control']
    print(f'{log_level[level]} ` {unix_timestamp()} ` {log_source[source]}: {message}')


def unix_timestamp() -> int:
    return round((dt.now() - dt(1970, 1, 1)).total_seconds())


def make_dir(path: str) -> None:
    if not exists(path):
        makedirs(path)


def remove_dir(path: list) -> None:
    for d in path:
        if exists(d):
            rmtree(d)


def get_file_list(path: str) -> list:
    file_list = [name for name in listdir(path)]
    return file_list


def list2str(source: list) -> str:
    result: str = ' '.join(str(i) for i in source)
    return result
