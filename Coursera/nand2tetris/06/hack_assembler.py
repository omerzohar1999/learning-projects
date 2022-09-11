import argparse
from re import I

jumpers = {"JMP": "111", "JLE": "110", "JNE": "101",
           "JLT": "100", "JGE": "011", "JEQ": "010", "JGT": "001"}

computations = {"0": ("101010", "0"), "1": ("111111", "0"),
                "-1": ("111010", "0"), "D": ("001100", "0"),
                "A": ("110000", "0"), "M": ("110000", "1"),
                "!D": ("001101", "0"), "!A": ("110001", "0"),
                "!M": ("110001", "1"), "-D": ("001111", "0"),
                "-A": ("110011", "0"), "-M": ("110011", "1"),
                "D+1": ("011111", "0"), "A+1": ("110111", "0"),
                "M+1": ("110111", "1"), "D-1": ("001110", "0"),
                "A-1": ("110010", "0"), "M-1": ("110010", "1"),
                "D+A": ("000010", "0"), "D+M": ("000010", "1"),
                "D-A": ("010011", "0"), "D-M": ("010011", "1"),
                "A-D": ("000111", "0"), "M-D": ("000111", "1"),
                "D&A": ("000000", "0"), "D&M": ("000000", "1"),
                "D|A": ("010101", "0"), "D|M": ("010101", "1")}

symbol_table = {"R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11,
               "R12": 12, "R13": 13, "R14": 14, "R15": 15, "SCREEN": 16384, "KBD": 24576, "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4}
    

def add_new_symbol(s: str):
    i = 16
    while i in symbol_table.values():
        i += 1
    symbol_table[s] = i
    return i


def parse_a_inst(line: str):
    if not line.isnumeric():
        if line not in symbol_table:
            val = add_new_symbol(line)
        else:
            val = symbol_table[line]
    else:
        val = int(line)
    binary_rep = bin(val)[2:]
    num_of_padding = 16 - len(binary_rep)
    return ("0" * num_of_padding) + binary_rep


def parse_c_inst(line: str):
    print("Parsing", line)
    a = "0"
    dest = ""
    comp = "000000"
    jumper = "000"
    start_of_comp = 0
    end_of_comp = len(line)
    if ";" in line:
        end_of_comp = line.find(";")
        jumper_str = line[end_of_comp + 1:]
        jumper = jumpers[jumper_str]

    if "=" in line:
        i = line.find("=")
        start_of_comp = i+1
        dest_str = line[:i]
        dest += ("1" if "A" in dest_str else "0")
        dest += ("1" if "D" in dest_str else "0")
        dest += ("1" if "M" in dest_str else "0")
    else:
        dest = "000"

    comp_str = line[start_of_comp:end_of_comp]
    if len(comp_str) > 0 and comp_str[-1] == "\n":
        comp_str = comp_str[:-1]
    comp, a = computations[comp_str]

    hack_code = "111" + a + comp + dest + jumper
    print("Hack code is", hack_code)
    return hack_code


def parse_line(line: str):
    if line[0] == '@':
        return parse_a_inst(line[1:])
    else:
        return parse_c_inst(line)


def main():
    input_file = open("pong/Pong.asm", "r")
    output_file = open("Hacks/Pong.hack", "w")
    program = input_file.readlines()
    input_file.close()
    print("io done")

    num_of_symbols_removed = 0
    index = 0
    problematic_line = ""
    while index < len(program):  # first pass - add (declerations)
        if program[index].find("//") != -1:
            comment_index = program[index].find("//")
            program[index] = program[index][:comment_index]
            print(program[index])
        program[index] = program[index].strip()
        program[index].replace(" ", "")
        print(program[index])
        if len(program[index]) == 0 or program[index][0] == '\n':
            program.pop(index)
        elif program[index][0] == "(":
            last_index = program[index].find(")")
            new_symbol_name = program[index][1:last_index]
            symbol_table[new_symbol_name] = index
            program.pop(index)
        else:
            index += 1
    
    index = 0
    for line in program:
        print("Line ", index)
        new_line = parse_line(line)
        output_file.write(new_line)
        output_file.write("\n")
        index += 1
    print("The symbol table was", symbol_table)
    output_file.close()
    print(program[8400])


main()
