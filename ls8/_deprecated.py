############################################################
#   "Binary" helper classes
############################################################


class BinaryItem:
    """A class to manage binary items."""

    def __init__(self, value):

        self.value = value
        return

    def __str__(self):

        # return (f"0o%0{OCT__COUNT}o" % self.value)
        return (FORMAT % self.value)

    @property
    def value(self):

        return self.__value

    @value.setter
    def value(self, value):

        self.__value = mask(value)
        return


class BinaryItemSequence:
    """A class to manage sequences of binary items."""

    def __init__(self, sequence):

        self.sequence = sequence
        return

    def __str__(self):

        return ("[" + ", ".join(str(item) for item in self.sequence) + "]")

    def __len__(self):

        return len(self.sequence)

    def __getitem__(self, key):

        return self.sequence[key]

    def __setitem__(self, key, value):

        self.sequence[key].value = value
        return

    @property
    def sequence(self):

        return self.__sequence

    @sequence.setter
    def sequence(self, sequence):

        self.__sequence = [BinaryItem(value) for value in sequence]
        return
