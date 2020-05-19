"""
Generate basic constants for a computer processor.
"""

############################################################

import math

from tools.numbers import int_to_str

############################################################


class ProcessorConstants:

    def __init__(self, bit_count):

        self.BIT_COUNT = bit_count
        self.WORD_SIZE = 2 ** self.BIT_COUNT

        # operations specification

        self.OPERATION_ARGS__WIDTH = 2
        self.OPERATION_ARGS__SHIFT = self.BIT_COUNT - 2

        self.OPERATION_USES_ALU__WIDTH = 1
        self.OPERATION_USES_ALU__SHIFT = self.BIT_COUNT - 3

        self.OPERATION_SETS_POINTER__WIDTH = 1
        self.OPERATION_SETS_POINTER__SHIFT = self.BIT_COUNT - 4

        self.OPERATION_IDENTIFIER__WIDTH = 4
        self.OPERATION_IDENTIFIER__SHIFT = 0

        # flags specification

        self.FLAG__WIDTH = 1
        self.FLAG_EQ__SHIFT = 0
        self.FLAG_GT__SHIFT = 1
        self.FLAG_LT__SHIFT = 2

        # formatting info

        self.BIN_WIDTH = self.BIT_COUNT
        self.TET_WIDTH = math.ceil(self.BIN_WIDTH / 2)
        self.OCT_WIDTH = math.ceil(self.BIN_WIDTH / 3)
        self.HEX_WIDTH = math.ceil(self.BIN_WIDTH / 4)

        return

    def format_as_bin(self, number):

        return f"2n{int_to_str(number, base=2, width=self.BIN_WIDTH)}"

    def format_as_tet(self, number):

        return f"4n{int_to_str(number, base=4, width=self.TET_WIDTH)}"

    def format_as_oct(self, number):

        return f"8n{int_to_str(number, base=8, width=self.OCT_WIDTH)}"

    def format_as_hex(self, number):

        return f"16n{int_to_str(number, base=16, width=self.HEX_WIDTH)}"
