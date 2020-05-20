############################################################
#   NUMBERS
############################################################

DEFAULT__ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DEFAULT__BASE = 10

#-----------------------------------------------------------


def int_as_base(
    number,
    base=DEFAULT__BASE,
    alphabet=DEFAULT__ALPHABET,
):

    result = ""

    while number:

        result += alphabet[number % base]
        number //= base

    return result[::-1] or "0"


#-----------------------------------------------------------


def int_to_str(
    number,
    base=DEFAULT__BASE,
    alphabet=DEFAULT__ALPHABET,
    fill=None,
    width=None,
):

    if fill is None:
        fill = alphabet[0]

    if width is None:
        width = ""

    return "{0:{fill}>{width}}".format(
        int_as_base(number, base=base, alphabet=alphabet),
        fill=fill,
        width=width,
    )
