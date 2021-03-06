from os import mkdir, path, remove
from json import dump
from wget import download


def mkfile(file_path):
    with open(file_path, "w") as _:
        pass


def create(package_name):
    if path.isdir(package_name):
        print("")
    mkdir(package_name)
    mkdir(package_name + "/Sources")
    mkdir(package_name + "/Headers")
    mkfile(package_name + "/Headers/__main__.jlh")
    mkdir(package_name + "/Versions")
    barebones_info = {
        "Version": "pre-release",
        "Supported Version": "",
        "Dependencies": []
    }

    download("https://raw.githubusercontent.com/Zorz42/jaclang/master/include/version.h", "newestjaclangversion.txt",
             bar=None)
    with open("newestjaclangversion.txt") as newest_version:
        newestjaclangversion = [line.split(" ")[2] for line in newest_version.read().split("\n")
                                if len(line.split(" ")) == 3]
        newestjaclangversion.pop()
        for i in range(2):
            newestjaclangversion[i] = newestjaclangversion[i][1:-1]
        barebones_info["Supported Version"] = f"{newestjaclangversion[0]}.{newestjaclangversion[1]}"
    remove("newestjaclangversion.txt")
    with open(package_name + "/Info.json", "w") as info_file:
        dump(barebones_info, info_file, indent=4)
        info_file.write('\n')
