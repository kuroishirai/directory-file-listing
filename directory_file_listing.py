import os

# target directory
parent_dir = '/Users/tatsuya-shi/research'

# output file path
output_file = '/Users/tatsuya-shi/research/program/__test/output.txt'

# Please change to Build Log extension
extension = ['', '.txt']

file_list = []

# Get files by directory
for dirpath, dirnames, filenames in os.walk(parent_dir):
    for filename in filenames:
        # ファイルの拡張子を取得
        file_name, ext = os.path.splitext(filename)
        
        # match extension
        if ext in extension:
            # file_list.append(f'{dirpath.replace(parent_dir,'')}/{filename}')
            file_list.append(f'{dirpath}/{filename}')
# for file in file_list:
#     print(file)

# Write to textfile
with open(output_file, 'w') as f:
    for item in file_list:
        f.write("%s\n" % item)