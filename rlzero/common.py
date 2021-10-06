import os
import rlzero.globals as Globals

def _gen_file_paths(name, extensions, folders):
    paths = []
    for folder in folders:
        for ext in extensions:
            paths.append(folder + os.path.sep + name + ext)
            paths.append(Globals.data_dir + os.path.sep + folder + os.path.sep + name + ext)
            paths.append(str(Globals.PATH / folder / name) + ext)
    return paths

def find_file(name, extensions, folders):
    for file in _gen_file_paths(name, extensions, folders):
        print("trying ",file)
        if os.path.isfile(file):
            return file
    raise Exception(f"file {file} does not exist")