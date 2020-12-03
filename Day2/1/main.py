file = open('input.txt', 'r')
data = file.read() 
file.close()
opcodes = data.split(',')

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
            print(opcodes)
            exit(0)
            

nextInstruction = True
instruction = None 
print(opcodes)
for opcode in opcodes:
    opcode = int(opcode)
    if nextInstruction: 
        instruction = Instruction(opcode)
        nextInstruction = False
        continue 
    result = instruction.nextArg(opcode)
    if result:
        nextInstruction = True
        instruction.run()
        instruction = None 

if instruction is not None:
    instruction.run()

