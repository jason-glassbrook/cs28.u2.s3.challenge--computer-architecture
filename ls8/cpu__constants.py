"""
Generate basic constants for a computer processor.
"""

############################################################

import math

from tools.numbers import (
    int_to_str,
    DEFAULT__INCLUDE_BASE__BETWEEN as BETWEEN,
    DEFAULT__INCLUDE_BASE__BEFORE_BASE as BEFORE_BASE,
    DEFAULT__INCLUDE_BASE__AFTER_BASE as AFTER_BASE,
)

############################################################


class ProcessorConstants:

    def __init__(self, bit_count):

        self.BIT_COUNT = bit_count
        self.WORD_SIZE = 2 ** self.BIT_COUNT

        self.REGISTER_OF_STACK_POINTER = self.BIT_COUNT - 1
        self.REGISTER_OF_INTERRUPT_STATUS = self.REGISTER_OF_STACK_POINTER - 1
        self.REGISTER_OF_INTERRUPT_MASK = self.REGISTER_OF_INTERRUPT_STATUS - 1

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

    def __str__(self):

        return str(self.__dict__)

    def _format_as_base(self, number, base, width):

        base_str = f"{BEFORE_BASE}{base}{AFTER_BASE}"
        number_str = int_to_str(number, base=base, width=width)

        return f"{base_str}{BETWEEN}{number_str}"

    def format_as_bin(self, number):

        return self._format_as_base(number, 2, self.BIN_WIDTH)

    def format_as_tet(self, number):

        return self._format_as_base(number, 4, self.TET_WIDTH)

    def format_as_oct(self, number):

        return self._format_as_base(number, 8, self.OCT_WIDTH)

    def format_as_hex(self, number):

        return self._format_as_base(number, 16, self.HEX_WIDTH)
