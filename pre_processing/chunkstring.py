def chunkstring(string, length):
    try:
        return [string[0+i:length+i] for i in range(0, len(string), length)]
    except ValueError:
        print(string, length)