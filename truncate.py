with open('file.txt', 'r') as f:
    print(type(f))
    f.seek(10)
    data=f.read(3)
    print(data)