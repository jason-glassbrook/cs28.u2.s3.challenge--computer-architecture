#!/usr/bin/env python3
"""
Main.
"""

############################################################

import os
import sys

from .cpu import CPU

############################################################


def normpath_join(*args):
    return os.path.normpath(os.path.join(*args))


############################################################

args = sys.argv
print(args)

current_dir = os.getcwd()
print(current_dir)
project_dir = normpath_join(args[0], "../../")
print(project_dir)
examples_dir = normpath_join(project_dir, "./ls8/examples")
print(examples_dir)
examples_ext = ".ls8"
print(examples_ext)
program_file = None
print(program_file)

if args[1] == "--example" or args[1] == "-e":

    try:

        example_name = args[2]

        if example_name.endswith(examples_ext):
            example_name = example_name[:-len(examples_ext)]

        program_file = normpath_join(examples_dir, example_name + examples_ext)

    except IndexError:

        raise Exception("MissingExampleName")

else:

    program_file = args[1]
    program_file = normpath_join(project_dir, program_file)

print(program_file)

#-----------------------------------------------------------

cpu = CPU()
cpu.load(program_file)
cpu.run()
