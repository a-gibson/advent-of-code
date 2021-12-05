#!/usr/bin/env python3

from collections import namedtuple

class instructions():
    instruction_index = 0
    route = []
    x = 0 # distance travelled forward
    y = 0 # equivalent to depth (where deeper is a larger positive number)

    def decodeInstruction(self, instruction):
        if instruction.direction == "forward":
            self.x += instruction.distance
        elif instruction.direction == "down":
            self.y += instruction.distance
        elif instruction.direction == "up":
            self.y -= instruction.distance
        else:
            raise Exception ("Invalid direction instruction: {}".format(instruction.direction))

    def getRoute(self, route_file):
        instruction = namedtuple("instruction", ["direction", "distance"])

        with open(route_file) as f:
            for line in f:
                i = instruction(line.rstrip().split(" ")[0], int(line.rstrip().split(" ")[1]))
                self.route.append(i)

    def nextInstruction(self):
        if self.instruction_index == len(self.route):
            return None
        else:
            i = self.route[self.instruction_index]
            self.instruction_index += 1
            return i


def main():
    inst = instructions()
    inst.getRoute("./input.txt")

    while True:
        i = inst.nextInstruction()

        if i == None:
            break

        inst.decodeInstruction(i)

    print(inst.x * inst.y)


if __name__ == "__main__":
    main()