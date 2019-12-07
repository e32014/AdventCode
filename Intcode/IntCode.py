file = open("input.txt")

def compile_prog(noun, verb, program):
    pointer = 0
    optcode = 0
    program[1] = noun
    program[2] = verb
    while optcode != 99:
        optcode = program[pointer]
        if optcode == 1:
            pos1 = program[pointer+1]
            pos2 = program[pointer+2]
            dest = program[pointer+3]
            pointer += 4
            program[dest] = program[pos1] + program[pos2]
        elif optcode == 2:
            pos1 = program[pointer + 1]
            pos2 = program[pointer + 2]
            dest = program[pointer + 3]
            pointer += 4
            program[dest] = program[pos1] * program[pos2]
        elif optcode != 99:
            print("FUCK?")
            break
    return program[0]

for i in range(0, 99):
    for j in range(0, 99):
        file = open("input.txt")
        prog = [int(x) for x in file.readline().split(",")]
        file.close()
        result = compile_prog(i, j, prog)
        if result == 19690720:
            print(i*100 + j)
            exit(0)
