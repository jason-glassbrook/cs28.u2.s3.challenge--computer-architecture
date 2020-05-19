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

    def word_mask(self, bits):
        """
        Mask the provided `bits` to clip it to the word length `self.WORD`.
        """

        return self.and_mask(bits)

    def and_mask(self, bits, mask=None):
        """
        AND-mask the provided `bits` with `mask`.
        """

        mask = self.mask_or_word(mask)
        return (bits & mask)

    def or_mask(self, bits, mask=None):
        """
        OR-mask the provided `bits` with `mask`.
        """

        mask = self.mask_or_word(mask)
        return (bits | mask)

    def xor_mask(self, bits, mask=None):
        """
        XOR-mask the provided `bits` with `mask`.
        """

        mask = self.mask_or_word(mask)
        return (bits ^ mask)

    def is_masked_by(self, bits, mask=None):
        """
        Test if `bits` is masked by `mask`.
        Returns `True` if the AND-masked `bits` is equal to `mask`.
        Otherwise, returns `False`.
        """

        mask = self.mask_or_word(mask)
        return (self.and_mask(bits, mask) == mask)

    def is_not_masked_by(self, bits, mask=None):
        """
        Test if `bits` is _not_ masked by `mask`.
        Returns the opposite of `self.is_masked_by`.
        """

        return (not self.is_masked_by(bits, mask))

    def equal_with_mask(self, bits_a, bits_b, mask=None):
        """
        Test if the `mask`ed portions of `bits_a` and `bits_b` are equal.
        """

        mask = self.mask_or_word(mask)
        masked_a = self.and_mask(bits_a, mask)
        masked_b = self.and_mask(bits_b, mask)
        return (masked_a == masked_b)

    def not_equal_with_mask(self, bits_a, bits_b, mask=None):
        """
        Test if the `mask`ed portions of `bits_a` and `bits_b` are _not_ equal.
        Returns the opposite of `self.equal_with_mask`.
        """

        return (not self.equal_with_mask(bits_a, bits_b, mask))

    def turn_on_masked(self, bits, mask=None):
        """
        Turn "on" the `mask`ed portions of `bits`.
        """

        mask = self.mask_or_word(mask)
        return self.or_mask(bits, mask)

    def turn_off_masked(self, bits, mask=None):
        """
        Turn "off" the `mask`ed portions of `bits`.
        """

        mask = self.mask_or_word(mask)
        return self.and_mask(bits, self.WORD - mask)

    def toggle_masked(self, toggle, bits, mask=None):
        """
        Toggle "on" or "off" the `masked` portions of `bits` based on `toggle`.
        """

        mask = self.mask_or_word(mask)
        toggled = (
            self.turn_on_masked(bits, mask)
            if toggle else self.turn_off_masked(bits, mask)
        )
        return toggled
