file = open("input.txt")


def compile_prog(program):
    pointer = 0
    optcode = 0
    while optcode != 99:
        optcode = program[pointer]
        strOpt = str(optcode).rjust(5, '0')
        optcode = int(strOpt[3:])
        imm1 = int(strOpt[2:3])
        imm2 = int(strOpt[1:2])
        imm3 = int(strOpt[0:1])
        if optcode == 1:
            pos1 = program[pointer + 1]
            val1 = pos1 if imm1 == 1 else program[pos1]
            pos2 = program[pointer + 2]
            val2 = pos2 if imm2 == 1 else program[pos2]
            dest = program[pointer + 3]
            pointer += 4
            program[dest] = val1 + val2
        elif optcode == 2:
            pos1 = program[pointer + 1]
            val1 = pos1 if imm1 == 1 else program[pos1]
            pos2 = program[pointer + 2]
            val2 = pos2 if imm2 == 1 else program[pos2]
            dest = program[pointer + 3]
            pointer += 4
            program[dest] = val1 * val2
        elif optcode == 3:
            dest = program[pointer + 1]
            val = input("Enter a value: ")
            pointer += 2
            program[dest] = int(val)
        elif optcode == 4:
            pos = program[pointer + 1]
            print(pos if imm1 == 1 else program[pos])
            pointer += 2
        elif optcode == 5:
            pos1 = program[pointer + 1]
            dest = program[pointer + 2]
            check = pos1 if imm1 else program[pos1]
            jumpTo = dest if imm2 else program[dest]
            if check != 0:
                pointer = jumpTo
            else:
                pointer += 3
        elif optcode == 6:
            pos1 = program[pointer + 1]
            dest = program[pointer + 2]
            check = pos1 if imm1 else program[pos1]
            jumpTo = dest if imm2 else program[dest]
            if check == 0:
                pointer = jumpTo
            else:
                pointer += 3
        elif optcode == 7:
            pos1 = program[pointer + 1]
            pos2 = program[pointer + 2]
            dest = program[pointer + 3]
            val1 = pos1 if imm1 else program[pos1]
            val2 = pos2 if imm2 else program[pos2]
            pointer += 4
            if val1 < val2:
                program[dest] = 1
            else:
                program[dest] = 0
        elif optcode == 8:
            pos1 = program[pointer + 1]
            pos2 = program[pointer + 2]
            dest = program[pointer + 3]
            val1 = pos1 if imm1 else program[pos1]
            val2 = pos2 if imm2 else program[pos2]
            pointer += 4
            if val1 == val2:
                program[dest] = 1
            else:
                program[dest] = 0
        elif optcode != 99:
            print("FUCK?")
            break
    return program[0]


prog = [int(x) for x in file.readline().split(",")]
file.close()
result = compile_prog(prog)