"""CPU functionality."""

############################################################

import sys
import math

from tools.printing import print_line, print_heading

from .cpu__constants import ProcessorConstants
from .cpu__masks import ProcessorMasks
from .cpu__operations import ProcessorOperations

############################################################
#   CPU
############################################################


class CPU:
    """
    Main CPU class.
    """

    ############################################################

    CONSTANTS = ProcessorConstants(8)
    MASKS = ProcessorMasks(CONSTANTS)
    OPERATIONS = ProcessorOperations(CONSTANTS, MASKS)

    #-----------------------------------------------------------

    def __init__(self):
        """
        Construct a new CPU.
        """

        self.register = [0] * CPU.CONSTANTS.BIT_COUNT
        self.memory = [0] * CPU.CONSTANTS.WORD_SIZE
        self.flags = 0

        self.program_pointer = 0
        self.stack_pointer = 0xF4

        self.should_continue = False

        return

    #-----------------------------------------------------------

    @property
    def stack_pointer(self):
        return self.register[CPU.CONSTANTS.REGISTER_OF_STACK_POINTER]

    @stack_pointer.setter
    def stack_pointer(self, value):
        self.register[CPU.CONSTANTS.REGISTER_OF_STACK_POINTER] = value
        return

    @property
    def interrupt_status(self):
        return self.register[CPU.CONSTANTS.REGISTER_OF_STACK_POINTER]

    @interrupt_status.setter
    def interrupt_status(self, value):
        self.register[CPU.CONSTANTS.REGISTER_OF_STACK_POINTER] = value
        return

    @property
    def interrupt_mask(self):
        return self.register[CPU.CONSTANTS.REGISTER_OF_STACK_POINTER]

    @interrupt_mask.setter
    def interrupt_mask(self, value):
        self.register[CPU.CONSTANTS.REGISTER_OF_STACK_POINTER] = value
        return

    #-----------------------------------------------------------

    def format_value(self, value):

        return CPU.CONSTANTS.format_as_bin(value)

    def format_iterable(self, *args):

        return tuple(self.format_value(value) for value in args)

    def trace(self):
        """
        Handy function to print out the CPU state.
        You might want to call this from run() if you need help debugging.
        """

        print(
            "TRACE --- {} {} {} | {} {} {} | ".format(
                *self.format_iterable(
                    self.program_pointer,
                    self.stack_pointer,
                    self.flags,
                    self.read_register(self.program_pointer),
                    self.read_register(self.program_pointer + 1),
                    self.read_register(self.program_pointer + 2),
                ),
            ),
            end="",
        )

        print(
            " ".join(self.format_iterable(*self.register)),
            end="",
        )

        print()

        return

    ############################################################
    #   REGISTER
    ############################################################

    def read_register(self, address):
        """
        Read the `value` from the provided `address` in the register.
        """

        return self.register[address]

    def write_register(self, address, value):
        """
        Write the `value` to the provided `address` in the register.
        """

        self.register[address] = CPU.MASKS.word_mask(value)

        return

    ############################################################
    #   MEMORY
    ############################################################

    def read_memory(self, address):
        """
        Read the `value` from the provided `address` in the memory.
        """

        return self.memory[address]

    def write_memory(self, address, value):
        """
        Write the `value` to the provided `address` in the memory.
        """

        self.memory[address] = CPU.MASKS.word_mask(value)

        return

    ############################################################
    #   PROCESSING
    ############################################################

    def load(self, program_file):
        """
        Load a program into memory.
        """

        print()
        print_heading("reading program from file...", width=40)

        program = []

        with open(program_file) as file:

            for line in file:

                line_str = line.split("#")[0].strip()

                if line_str:

                    word = int(line_str, base=2)
                    program.append(word)
                    print(self.format_value(word))

        print()
        print_heading("writing program to memory...", width=40)

        for (i, word) in enumerate(program):

            self.write_memory(i, word)
            print("[{}]: {}".format(*self.format_iterable(i, word)))

        return

    #-----------------------------------------------------------

    def start(self):
        self.should_continue = True
        return

    def stop(self):
        self.should_continue = False
        return

    def run(self):
        """
        Run the CPU.
        """

        self.start()

        print()
        print_heading("running program from memory...", width=40)

        while self.should_continue:

            word = self.read_memory(self.program_pointer)
            print(self.format_value(word), end="")

            if word in self.OPERATIONS:

                operation = self.OPERATIONS[word]
                print(" <operation: {}>".format(operation["name"]), end="")

                if operation["code_name"] == "HLT":

                    self.stop()

            else:

                print(" <unknown>".format(), end="")

            self.program_pointer += 1
            print()

        print_line(width=40)
        print("done.")

        return

    ############################################################
    #   OPERATIONS
    ############################################################

    def alu(self, op, reg_a, reg_b):
        """
        ALU operations.
        """

        if op == "ADD":
            value_a = self.read_register(reg_a)
            value_b = self.read_register(reg_b)
            self.write_register(reg_a, value_a + value_b)
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

        return

    ############################################################
    #   PROPERTIES
    ############################################################

    @property
    def flag_eq(self):
        return CPU.MASKS.is_masked_by(self.flags, CPU.MASKS.FLAG_EQ)

    @flag_eq.setter
    def flag_eq(self, value):
        self.flags = CPU.MASKS.toggle_masked(value, self.flags, CPU.MASKS.FLAG_EQ)
        return

    #-----------------------------------------------------------

    @property
    def flag_gt(self):
        return CPU.MASKS.is_masked_by(self.flags, CPU.MASKS.FLAG_GT)

    @flag_gt.setter
    def flag_gt(self, value):
        self.flags = CPU.MASKS.toggle_masked(value, self.flags, CPU.MASKS.FLAG_GT)
        return

    #-----------------------------------------------------------

    @property
    def flag_lt(self):
        return CPU.MASKS.is_masked_by(self.flags, CPU.MASKS.FLAG_LT)

    @flag_lt.setter
    def flag_lt(self, value):
        self.flags = CPU.MASKS.toggle_masked(value, self.flags, CPU.MASKS.FLAG_LT)
        return

    #-----------------------------------------------------------

    @property
    def flag_neq(self):
        return CPU.MASKS.is_masked_by(self.flags, CPU.MASKS.FLAG_NEQ)

    @flag_neq.setter
    def flag_neq(self, value):
        self.flags = CPU.MASKS.toggle_masked(value, self.flags, CPU.MASKS.FLAG_NEQ)
        return

    #-----------------------------------------------------------

    @property
    def flag_ngt(self):
        return CPU.MASKS.is_masked_by(self.flags, CPU.MASKS.FLAG_NGT)

    @flag_ngt.setter
    def flag_ngt(self, value):
        self.flags = CPU.MASKS.toggle_masked(value, self.flags, CPU.MASKS.FLAG_NGT)
        return

    #-----------------------------------------------------------

    @property
    def flag_nlt(self):
        return CPU.MASKS.is_masked_by(self.flags, CPU.MASKS.FLAG_NLT)

    @flag_nlt.setter
    def flag_nlt(self, value):
        self.flags = CPU.MASKS.toggle_masked(value, self.flags, CPU.MASKS.FLAG_NLT)
        return
