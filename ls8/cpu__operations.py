"""
Generate operations for the LS-8 CPU.
"""

############################################################

from .cpu__masks import _block, _unblock

############################################################

OPERATIONS = {
    0b00000000: {
        "name": "NO OPERATION",
        "code_name": "NOP",
    },
    0b00000001: {
        "name": "HALT",
        "code_name": "HLT",
    },
    0b00010001: {
        "name": "RETURN FROM CALL",
        "code_name": "RET",
    },
    0b00010011: {
        "name": "RETURN FROM INTERRUPT",
        "code_name": "IRET",
    },
    0b01000101: {
        "name": "PUSH",
        "code_name": "PUSH",
    },
    0b01000110: {
        "name": "POP",
        "code_name": "POP",
    },
    0b01000111: {
        "name": "PRINT NUMBER",
        "code_name": "PRN",
    },
    0b01001000: {
        "name": "PRINT ALPHA",
        "code_name": "PRA",
    },
    0b01010000: {
        "name": "CALL",
        "code_name": "CALL",
    },
    0b01010010: {
        "name": "INTERRUPT",
        "code_name": "INT",
    },
    0b01010100: {
        "name": "JUMP",
        "code_name": "JMP",
    },
    0b01010101: {
        "name": "JUMP WHEN FLAGGED EQUAL",
        "code_name": "JEQ",
    },
    0b01010110: {
        "name": "JUMP WHEN FLAGGED NOT EQUAL",
        "code_name": "JNE",
    },
    0b01010111: {
        "name": "JUMP WHEN FLAGGED GREATER THAN",
        "code_name": "JGT",
    },
    0b01011000: {
        "name": "JUMP WHEN FLAGGED LESS THAN",
        "code_name": "JLT",
    },
    0b01011001: {
        "name": "JUMP WHEN FLAGGED LESS THAN OR EQUAL",
        "code_name": "JLE",
    },
    0b01011010: {
        "name": "JUMP WHEN FLAGGED GREATER THAN OR EQUAL",
        "code_name": "JGE",
    },
    0b01100101: {
        "name": "INCREMENT",
        "code_name": "INC",
    },
    0b01100110: {
        "name": "DECREMENT",
        "code_name": "DEC",
    },
    0b01101001: {
        "name": "BITWISE NOT",
        "code_name": "NOT",
    },
    0b10000010: {
        "name": "LOAD IMMEDIATE",
        "code_name": "LDI",
    },
    0b10000011: {
        "name": "LOAD",
        "code_name": "LD",
    },
    0b10000100: {
        "name": "STORE",
        "code_name": "ST",
    },
    0b10100000: {
        "name": "ADD",
        "code_name": "ADD",
    },
    0b10100001: {
        "name": "SUBTRACT",
        "code_name": "SUB",
    },
    0b10100010: {
        "name": "MULTIPLY",
        "code_name": "MUL",
    },
    0b10100011: {
        "name": "DIVISION",
        "code_name": "DIV",
    },
    0b10100100: {
        "name": "MODULO",
        "code_name": "MOD",
    },
    0b10100111: {
        "name": "COMPARE",
        "code_name": "CMP",
    },
    0b10101000: {
        "name": "BITWISE AND",
        "code_name": "AND",
    },
    0b10101010: {
        "name": "BITWISE OR",
        "code_name": "OR",
    },
    0b10101011: {
        "name": "BITWISE XOR",
        "code_name": "XOR",
    },
    0b10101100: {
        "name": "BITWISE SHIFT LEFT",
        "code_name": "SHL",
    },
    0b10101101: {
        "name": "BITWISE SHIFT RIGHT",
        "code_name": "SHR",
    },
}

############################################################


class ProcessorOperations:

    def __init__(self, constants, masks):

        operations = OPERATIONS

        for code in operations:

            operations[code]["args"] = _unblock(
                constants.OPERATION_ARGS__WIDTH,
                constants.OPERATION_ARGS__SHIFT,
                masks.and_mask(code, masks.OPERATION_ARGS),
            )
            operations[code]["uses_alu"] = _unblock(
                constants.OPERATION_USES_ALU__WIDTH,
                constants.OPERATION_USES_ALU__SHIFT,
                masks.and_mask(code, masks.OPERATION_USES_ALU),
            )
            operations[code]["sets_pointer"] = _unblock(
                constants.OPERATION_SETS_POINTER__WIDTH,
                constants.OPERATION_SETS_POINTER__SHIFT,
                masks.and_mask(code, masks.OPERATION_SETS_POINTER),
            )
            operations[code]["identifier"] = _unblock(
                constants.OPERATION_IDENTIFIER__WIDTH,
                constants.OPERATION_IDENTIFIER__SHIFT,
                masks.and_mask(code, masks.OPERATION_IDENTIFIER),
            )

        self.operations = operations

        return

    def __getitem__(self, key):

        return self.operations[key]

    def __contains__(self, key):

        return (key in self.operations)

    def __iter__(self):

        for key in self.operations:
            yield key

        return
