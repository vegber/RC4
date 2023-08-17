def EncryptStep(fileName):
    try:
        with open(fileName, 'r') as file:
            file = file.read().encode()
        return file
    except FileNotFoundError:
            print("The file 'plaintext.txt' was not found in the current directory.")
    except IOError:
            print("There was an error opening or reading the file 'plaintext.txt'.")
    return None


def DecryptStep(fileName):
    f = open(fileName, 'r')
    file = f.read()
    x = bytes.fromhex(file)
    return x


