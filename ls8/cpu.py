"""CPU functionality."""

############################################################

import sys
import math

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

    CONSTANTS = ProcessorConstants(8)
    MASKS = ProcessorMasks(CONSTANTS)
    OPERATIONS = ProcessorOperations(CONSTANTS, MASKS)

    def __init__(self):
        """
        Construct a new CPU.
        """

        self.register = [0] * CPU.CONSTANTS.BIT_COUNT
        self.register[CPU.CONSTANTS.BIT_COUNT - 1] = 0xF4

        self.memory = [0] * CPU.CONSTANTS.WORD_SIZE

        self.program_pointer = 0
        self.stack_pointer = 0

        self.flags = 0

        return

    ############################################################

    def format_value(self, value):

        return CPU.CONSTANTS.format_as_hex(value)

    def format_iterable(self, *args):

        return tuple(self.format_value(value) for value in args)

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

    def load(self):
        """
        Load a program into memory.
        """

        # For now, we've just hardcoded a program:

        self.program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        return

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

    def run(self):
        """
        Run the CPU.
        """

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
