# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.
#
# Using his technique, try to decode this matrix.
#
# Hints:
# Use
# ● lists for storing data
# ● Loops for going through the data
# ● if/else statements to check the data
# ● String for the output of the secret message
#
# Hint (if needed) : Look at the remote learning “Matrix” videos

matrix = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', '',  '#'],
    ['s', 'M', ''],
    ['$', 'a', ''],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]

message = ''

for x in range(3):
    for y in range(8):
        if matrix[y][x].isalpha():
            message += matrix[y][x]

print(message)
