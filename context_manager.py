class ContextManager:
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')

class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print('enter method called')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            print('close method called')
            self.file.close()

with FileManager('data.txt', mode='w') as file:
    pass
