"""
Generate basic constants for a computer processor.
"""

############################################################

import math

from tools.numbers import int_to_str

############################################################


class ProcessorConstants:

    def __init__(self, BIT_COUNT):

        self.BIT_COUNT = BIT_COUNT
        self.WORD_SIZE = 2 ** self.BIT_COUNT

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
