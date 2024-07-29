# directory-file-listing

## Overview
This program recursively searches for files with specific extensions within a specified parent directory, generates a list of these files, and writes the list to `output.txt` file.

## Usage
1. Ensure Python is installed on your system before running the program.
2. Execute the program from the command line as follows:
```
python script.py path_to_parent_directory
```
Example:
```
python script.py /path/to/parent_dir
```

## Arguments
`parent_dir`：検索を開始する親ディレクトリのパスを指定します。

## Output
output.txt: A file containing the list of files with specific extensions. This file will be created in the directory where the script is executed.

#Notes
- The file extensions are specified in `extension` list. Please modify this list as needed.
- The output.txt file will be created in the directory where the script is executed. If a file with the same name already exists, it will be overwritten.
- All files path with the specified extensions within the parent directory will be included in the output list.
