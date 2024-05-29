class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        temp = ""
        for i in range(len(command)):
            if command[i] == "(" and command[i+1] == ")":
                output += "o"
            elif command[i] == "(":
                output += ""
            elif command[i] == ")":
                output += ""
            else:
                output += command[i]

        return output

