"""
Generate basic masks for a computer processor.
"""

############################################################


class ProcessorMasks:

    def __init__(self, constants):

        self.WORD = int(bin(constants.WORD_SIZE - 1), base=2)

        self.OPCODE_ARGS = 0b11000000
        self.OPCODE_USES_ALU = 0b00100000
        self.OPCODE_SETS_POINTER = 0b00010000
        self.OPCODE_IDENTIFIER = self.WORD ^ (
            self.OPCODE_ARGS | self.OPCODE_USES_ALU | self.OPCODE_SETS_POINTER
        )

        self.FLAG_EQ = 2 ** 0
        self.FLAG_GT = 2 ** 1
        self.FLAG_LT = 2 ** 2
        self.FLAG_NEQ = self.FLAG_LT | self.FLAG_GT
        self.FLAG_NGT = self.FLAG_LT | self.FLAG_EQ
        self.FLAG_NLT = self.FLAG_EQ | self.FLAG_GT

        return

    def word_mask(self, value):
        """Mask the provided `value` to clip it to the required number of bits."""

        return self.and_mask(value)

    def and_mask(self, value, mask=None):
        """AND-Mask the provided `value`."""

        if mask is None:
            mask = self.WORD

        return (value & mask)

    def or_mask(self, value, mask=None):
        """OR-Mask the provided `value`."""

        if mask is None:
            mask = self.WORD

        return (value | mask)

    def xor_mask(self, value, mask=None):
        """XOR-Mask the provided `value`."""

        if mask is None:
            mask = self.WORD

        return (value ^ mask)
