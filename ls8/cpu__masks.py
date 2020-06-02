"""
Generate basic masks for a computer processor.
"""

############################################################


def _block(width, shift):

    return (((2 ** width) - 1) << shift)


def _unblock(width, shift, bits):

    return (bits >> shift)


#-----------------------------------------------------------


class ProcessorMasks:

    def __init__(self, constants):

        self.WORD = int(bin(constants.WORD_SIZE - 1), base=2)

        # opcode part masks

        self.OPERATION_ARGS = _block(
            constants.OPERATION_ARGS__WIDTH,
            constants.OPERATION_ARGS__SHIFT,
        )
        self.OPERATION_USES_ALU = _block(
            constants.OPERATION_USES_ALU__WIDTH,
            constants.OPERATION_USES_ALU__SHIFT,
        )
        self.OPERATION_SETS_POINTER = _block(
            constants.OPERATION_SETS_POINTER__WIDTH,
            constants.OPERATION_SETS_POINTER__SHIFT,
        )
        self.OPERATION_IDENTIFIER = _block(
            constants.OPERATION_IDENTIFIER__WIDTH,
            constants.OPERATION_IDENTIFIER__SHIFT,
        )

        # flag part masks

        self.FLAG_EQ = _block(
            constants.FLAG__WIDTH,
            constants.FLAG_EQ__SHIFT,
        )
        self.FLAG_GT = _block(
            constants.FLAG__WIDTH,
            constants.FLAG_GT__SHIFT,
        )
        self.FLAG_LT = _block(
            constants.FLAG__WIDTH,
            constants.FLAG_LT__SHIFT,
        )
        self.FLAG_NEQ = self.FLAG_LT | self.FLAG_GT
        self.FLAG_NGT = self.FLAG_LT | self.FLAG_EQ
        self.FLAG_NLT = self.FLAG_EQ | self.FLAG_GT
        self.FLAG_COMPARE = self.FLAG_EQ | self.FLAG_LT | self.FLAG_GT

        return

    def __str__(self):

        return str(self.__dict__)

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
