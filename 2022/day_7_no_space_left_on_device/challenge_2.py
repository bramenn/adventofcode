"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused
space of at least 30000000. You need to find a directory you can delete that will free up enough
space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used
space) is 48381165; this means that the size of the unused space must currently be 21618835, which
isn't quite the 30000000 required by the update. Therefore, the update still requires a directory
with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

    Delete directory e, which would increase unused space by 584.
    Delete directory a, which would increase unused space by 94853.
    Delete directory d, which would increase unused space by 24933642.
    Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up enough space. However,
directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run
the update. What is the total size of that directory?


"""

from __future__ import annotations

from typing import Dict, List

directories: Dict[str, Dir] = {}


class Dir:

    path: str
    sub_dirs: Dict[str, Dir]
    files: List[int]

    def __init__(self, path: str):
        self.path = path
        self.sub_dirs = {}
        self.files = []

    @property
    def size(self):
        counter = 0
        for sub_dir in self.sub_dirs.values():
            counter += sub_dir.size
        return sum(self.files) + counter

    def add_sub_dir(self, dir_name: str):
        new_dir = Dir(path=self.path + dir_name + "/")
        self.sub_dirs[dir_name] = new_dir
        directories[new_dir.path] = new_dir


f = open("commands.txt", "r")


current_path = ""
last_path = ""
current_dir: Dir = None


def is_command(cmd: str) -> (bool, List):
    if cmd.startswith("$"):
        return True, cmd.split(" ")[1:]

    return False, cmd.split(" ")


for cmd in f:
    cmd = cmd.replace("\n", "")

    is_cmd, args = is_command(cmd)

    if is_cmd:
        if args[0] == "cd":
            if args[1] == "..":
                current_path = "/".join(current_path.split("/")[:-2]) + "/"
                current_dir = directories[current_path]
                continue

            current_path += args[1] + ("/" if args[1] != "/" else "")

            if not current_path in directories:
                directories[current_path] = Dir(path=current_path)

            current_dir = directories[current_path]
            continue

    if args[0] in ["dir", "ls"]:
        if args[0] == "dir":
            current_dir.add_sub_dir(args[1])
        continue

    current_dir.files.append(int(args[0]))


total_size = 0
total_size_device = 70000000
required_size = 30000000

current_unused_space = total_size_device - directories["/"].size
unused_space_required = required_size - current_unused_space


used_space = [item.size for item in directories.values()]

used_space_find = 0


for size in used_space:

    if size >= unused_space_required:
        used_space_find = size

print("used_space_find ->", used_space_find)
f.close()
