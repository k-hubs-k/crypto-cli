class ProgressFile:
    def __init__(self, fileobj, progress_bar):
        self.fileobj = fileobj
        self.progress_bar = progress_bar

    def read(self, size=-1):
        data = self.fileobj.read(size)
        self.progress_bar.update(len(data))
        return data

    def __getattr__(self, name):
        return getattr(self.fileobj, name)
