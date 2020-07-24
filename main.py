from sys import argv
from commands.create import create

if len(argv) == 1:
    print("jacrepo help:")
    print("jacrepo create [package name] - create a package in this folder")
    print("jacrepo archive [version] - update current package to version and archive package")
    exit(0)

if argv[1] == "create":
    if len(argv) == 2:
        print("Name a package!")
        exit(1)
    create(argv[2])
elif argv[1] == "archive":
    if len(argv) == 2:
        print("Name a version")
        exit(1)
    pass
else:
    print(f"Unknown argument: {argv[1]}")
    exit(1)