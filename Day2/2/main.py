file = open('input.txt', 'r')
data = file.read() 
file.close()
opcodes = data.split(',')
import copy
class Instruction():
    def __init__(self, itype):
        self.itype = itype 
        if itype == 1:
            self.argCount = 3 
        elif itype == 2:
            self.argCount = 3 
        elif itype == 99:
            self.argCount = 0 
        self.args = []
    def nextArg(self, arg):
        self.args.append(arg)
        return len(self.args) == self.argCount
    def run(self):
        if self.itype == 1:
            lhs = int(opcodes[self.args[0]])
            rhs = int(opcodes[self.args[1]])
            location = int(self.args[2])
            opcodes[location] = lhs + rhs 
        elif self.itype == 2:
            lhs = int(opcodes[self.args[0]])
            rhs = int(opcodes[self.args[1]])
            location = int(self.args[2])
            opcodes[location] = lhs * rhs 
        elif self.itype == 99:
            # print(opcodes)
            return False 
        return True
            

goal = 19690720
output = 0
nextInstruction = True
instruction = None 
origOpcodes = copy.deepcopy(opcodes)
for noun in range(0, 100):
    for verb in range(0, 100):
        opcodes[1] = noun 
        opcodes[2] = verb

        for opcode in opcodes:
            opcode = int(opcode)
            if nextInstruction: 
                instruction = Instruction(opcode)
                nextInstruction = False
                continue 
            result = instruction.nextArg(opcode)
            if result:
                nextInstruction = True
                if not instruction.run():
                    break
                instruction = None 

        output = int(opcodes[0])
        if output == goal:
            print("Found result!")
            print("Noun: ", noun)
            print("Verb: ", verb)
            print("Result: ", noun*100 + verb)
            exit(0)
        if not instruction.run():
            opcodes = copy.deepcopy(origOpcodes)
            instruction = None
            nextInstruction = True
            continue


print("Result not found")