# file = open('file.txt', 'r')
# try:
#     file.write('Hello')
# finally:
#     file.close()

# with open('file.txt', 'r') as file:
#     file.write('hello')
#     file.close()


class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print('enter')
        return self.file

    def __exit__(self, type, value, traceback):
        print(f'{type}, {value}, {traceback} ')
        print('exit')
        self.file.close()
        if type == Exception:
            return True


with File('file.txt', 'w') as f:
    print('middle')
    f.write('Say hello!')


from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    yield f
    f.close()
files = []
for _ in range(10):
    with open_file('file.txt','w') as f:
        files.append(f)

for f in files:
    if not f.closed:
        print('Not close')
    else:
        print(f)
        print('Closed!')
