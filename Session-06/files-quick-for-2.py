# Filename: files-quick-read.py

file_quick = open("assets/quick.txt", "r")

for line in file_quick:
    print(line.strip())
