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

    def mask_or_word(self, mask=None):
        """
        Use `mask` if given. Otherwise, use `self.WORD`.
        """

        return (self.WORD if mask is None else mask)

    def word_mask(self, value):
        """
        Mask the provided `value` to clip it to the world length `self.WORD`.
        """

        return self.and_mask(value)

    def and_mask(self, value, mask=None):
        """
        AND-mask the provided `value` with `mask`.
        """

        return (value & self.mask_or_word(mask))

    def or_mask(self, value, mask=None):
        """
        OR-mask the provided `value` with `mask`.
        """

        return (value | self.mask_or_word(mask))

    def xor_mask(self, value, mask=None):
        """
        XOR-mask the provided `value` with `mask`.
        """

        return (value ^ self.mask_or_word(mask))
