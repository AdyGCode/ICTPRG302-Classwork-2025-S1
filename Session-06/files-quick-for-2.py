# Filename: files-quick-read.py

file_quick = open("quick.txt", "r")

for line in file_quick:
    print(line.strip())
