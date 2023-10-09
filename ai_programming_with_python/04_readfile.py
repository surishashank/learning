
filename = "files/camelot.txt"

with open(filename, 'r') as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
