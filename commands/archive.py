import tarfile
from os import path
from json import load, dump


def filter_function(tarinfo):
    if tarinfo.name == "Archives":
        return None
    else:
        return tarinfo


def compress(input_dir, output_archive):
    with tarfile.open(output_archive, "w:gz") as tar:
        tar.add(input_dir, filter=filter_function)


def archive(version):
    if not path.isfile("Info.json"):
        print("Current directory is not a jaclang package!")
        exit(1)
    with open("Info.json", "r+") as info_file:
        info_dict = load(info_file)
        info_dict["Version"] = version
        info_file.seek(0)
        dump(info_dict, info_file, indent=4)
        info_file.truncate()
    compress(".", f"Archives/{version}.tar.gz")
