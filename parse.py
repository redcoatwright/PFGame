class ParsedInput:
    def __init__(self, verb, noun=None):
        self.verb = verb
        self.noun = noun

def parseInput(input):
    input_len = len(input)

    if input_len == 0:
        return None
    elif input_len == 1:
        return ParsedInput(input[0])
    elif input_len == 2:
        return ParsedInput(input[0], input[1])
    elif input_len > 2:
        return ParsedInput(input[0], input[input_len-1])
