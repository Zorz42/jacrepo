import tarfile
from os import path
from json import load, dump


def compress(input_dir, output_archive):
    with tarfile.open(output_archive, "w:gz") as tar:
        tar.add(input_dir, arcname=path.basename(input_dir))


def archive(version):
    if not path.isfile("Info.json"):
        print("Current directory is not a jaclang package!")
        exit(1)
    with open("Info.json", "r+") as info_file:
        info_dict = load(info_file)
        info_dict["Version"] = version
        dump(info_dict, info_file, indent=4)
    compress(".", f"Archives/{version}.tar.gz")