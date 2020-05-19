"""CPU functionality."""

############################################################

import sys
import math

from .constants import ProcessorConstants

############################################################

BIT_COUNT = 8
constants = ProcessorConstants(BIT_COUNT)

BIT__MASK = int(bin(constants.WORD_SIZE - 1), base=2)

NOT__MASK = BIT__MASK

FLAG_EQ__MASK = 2 ** 0
FLAG_GT__MASK = 2 ** 1
FLAG_LT__MASK = 2 ** 2
FLAG_NEQ__MASK = FLAG_LT__MASK | FLAG_GT__MASK
FLAG_NGT__MASK = FLAG_LT__MASK | FLAG_EQ__MASK
FLAG_NLT__MASK = FLAG_EQ__MASK | FLAG_GT__MASK

#-----------------------------------------------------------


def mask(value, binary_mask=BIT__MASK):
    """Mask the provided `value` to clip it to the required number of bits."""

    return (value & binary_mask)


############################################################
#   CPU
############################################################


class CPU:
    """Main CPU class."""

    ############################################################

    def __init__(self):
        """Construct a new CPU."""

        self.register = [0] * constants.BIT_COUNT
        self.register[constants.BIT_COUNT - 1] = 0xF4

        self.memory = [0] * constants.WORD_SIZE

        self.program_pointer = 0
        self.stack_pointer = 0

        self.flags = 0

        return

    ############################################################

    def format_value(self, value):

        return constants.format_as_hex(value)

    def format_iterable(self, *args):

        return tuple(self.format_value(value) for value in args)

    ############################################################

    def read_register(self, address):
        """Read the `value` from the provided `address` in the register."""

        return self.register[address]

    def write_register(self, address, value):
        """Write the `value` to the provided `address` in the register."""

        self.register[address] = mask(value)

        return

    ############################################################

    def read_memory(self, address):
        """Read the `value` from the provided `address` in the memory."""

        return self.memory[address]

    def write_memory(self, address, value):
        """Write the `value` to the provided `address` in the memory."""

        self.memory[address] = mask(value)

        return

    ############################################################

    def load(self):
        """Load a program into memory."""

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

    ############################################################

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            value_a = self.read_register(reg_a)
            value_b = self.read_register(reg_b)
            self.write_register(reg_a, value_a + value_b)
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    ############################################################

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
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

    ############################################################

    def run(self):
        """Run the CPU."""
        pass

    ############################################################
    #   PROPERTIES
    ############################################################

    @property
    def flag_eq(self):
        return (self.flags & CPU.FLAG_EQ__MASK)

    @flag_eq.setter
    def flag_eq(self, value):
        self.flags = (self.flags | CPU.FLAG_EQ__MASK)
        return

    #-----------------------------------------------------------

    @property
    def flag_gt(self):
        return (self.flags & CPU.FLAG_GT__MASK)

    @flag_gt.setter
    def flag_gt(self, value):
        self.flags = (self.flags | CPU.FLAG_GT__MASK)
        return

    #-----------------------------------------------------------

    @property
    def flag_lt(self):
        return (self.flags & CPU.FLAG_LT__MASK)

    @flag_lt.setter
    def flag_lt(self, value):
        self.flags = (self.flags | CPU.FLAG_LT__MASK)
        return

    #-----------------------------------------------------------

    @property
    def flag_neq(self):
        return (self.flags & CPU.FLAG_NEQ__MASK)

    @flag_neq.setter
    def flag_neq(self, value):
        self.flags = (self.flags | CPU.FLAG_NEQ__MASK)
        return

    #-----------------------------------------------------------

    @property
    def flag_ngt(self):
        return (self.flags & CPU.FLAG_NGT__MASK)

    @flag_ngt.setter
    def flag_ngt(self, value):
        self.flags = (self.flags | CPU.FLAG_NGT__MASK)
        return

    #-----------------------------------------------------------

    @property
    def flag_nlt(self):
        return (self.flags & CPU.FLAG_NLT__MASK)

    @flag_nlt.setter
    def flag_nlt(self, value):
        self.flags = (self.flags | CPU.FLAG_NLT__MASK)
        return
