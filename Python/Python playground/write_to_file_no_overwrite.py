import os

filepath = './Python/Python playground/write_to_file_no_overwrite.txt'
# with open(filepath, 'a') as file:
#     for i in range(0,5):
#         file.write(f'This is line {i+1}.\n')

# for i in range(0,5):
#     print(i)

# delete file contents
with open(filepath, 'w') as file:
    file.seek(0)
    file.truncate()
    file.write('')

# append to file
with open(filepath, 'a') as file:
    for i in range(0,5):
        file.write(f'This is line {i+1}.\n')

# delete file
def deleteFile():
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print(f'{filepath} does not exist.')

# rename file
def renameFile(filepath, newname):
    if os.path.exists(filepath):
        os.rename(filepath, newname)
    else:
        print(f'{filepath} does not exist.')

# copy file contents from one file to another
def copyFileContent(src, dest):
    with open(src, 'r') as source_file:
        with open(dest, 'w') as target_file:
            target_file.write(source_file.read())

# copy specific words from one file to another
def copySpecificWords(source, target):
    with open(source, 'r') as source_file:
        with open(target, 'w') as target_file:
            for line in source_file:
                if 'line 1' in line:
                    target_file.write(line)

# match regex pattern in file
def matchRegexPattern(file, pattern):
    with open(file, 'r') as file:
        for line in file:
            if pattern in line:
                print(line)