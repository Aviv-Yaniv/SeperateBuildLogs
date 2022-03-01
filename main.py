import os
import re
import shutil
import sys
from pathlib import Path
from collections import defaultdict

ENCODING    = "utf-8"
DIRECTORY   = 'output'
LOG_FILE    = 'log.txt'

def parse_args():
    return sys.argv[1] if sys.argv else LOG_FILE

def match_file_line(line):
    reg = ' ([1-9]\d*|0)\>'
    m = re.search(reg, line)
    return m.group(1) if m else 'default'

if __name__ == '__main__':
    log_file_path = parse_args()
    log_files = defaultdict()
    try:
        if Path(DIRECTORY).exists():
            shutil.rmtree(DIRECTORY)
        os.mkdir(DIRECTORY)
        with open(log_file_path, encoding=ENCODING) as log_file:
            for line in log_file.readlines():
                group_identifier = match_file_line(line)
                group_log_file_name = Path(DIRECTORY) / Path(f'log_{group_identifier}.txt')
                if group_identifier not in log_files:
                    log_files[group_identifier] = open(group_log_file_name, mode='a', encoding=ENCODING)
                log_files[group_identifier].write(line)
    finally:
        for name, file in log_files.items():
            file.close()
