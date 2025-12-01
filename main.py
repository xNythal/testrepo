import sys
import subprocess


args = sys.argv[1:]

if not args:
    print("no command provided")
    sys.exit()

command = args[0]
options = args[1:]

match command:
    case "push":
        print("pushing...")
    case "pull":
        print("pulling...")
    case "clone":
        print("cloning...")
    case "add":
        subprocess.run(("git", "add", *options))
    case "remote":
        subprocess.run(("git", "remote", *options))
    case "init":
        subprocess.run(("git", "init", *options))
    case _:
        subprocess.run(("git", command, *options))
