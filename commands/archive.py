import tarfile
from os import path
from json import load, dump
from shutil import copyfile

ignored_files = ("./Versions", "./Latest.json")


def filter_function(tarinfo):
    if tarinfo.name in ignored_files:
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
    compress(".", f"Versions/{version}.tar.gz")
    copyfile("Info.json", "Latest.json")
    print(f"Archived to version {version}!")
