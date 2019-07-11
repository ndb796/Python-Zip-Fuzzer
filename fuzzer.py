import zipfile
import threading


def extract_file(_zip_file, _password):
    try:
        _zip_file.extractall(pwd= _password.encode())
        print('password found: {0}'.format(_password))
    except:
        pass


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--list', required=True)

    file_name = parser.parse_args().file
    list_name = parser.parse_args().list
    zip_file = zipfile.ZipFile(file_name)

    with open(list_name, 'r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            
            th = threading.Thread(target=extract_file, args=(zip_file, password))
            th.start()
