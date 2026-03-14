class Directory:
    def __init__(self, name: str, root: Directory|None, files: list[File], sub_directories: list[Directory]) -> None:
        self.name = name
        self.root = root
        self.files = files
        self.sub_directories = sub_directories

    def add_sub_directory(self, directory: Directory) -> None:
        self.sub_directories.append(directory)
        directory.root = self

    def remove_sub_directory(self, directory: Directory) -> None:
        self.sub_directories.remove(directory)
        directory.root = None

    def add_file(self, file: File) -> None:
        self.files.append(file)
        file.directory = self

    def remove_file(self, file: File) -> None:
        self.files.remove(file)
        file.directory = None

class File:
    def __init__(self, name: str, directory: Directory|None) -> None:
        self.name = name
        self.directory = directory

