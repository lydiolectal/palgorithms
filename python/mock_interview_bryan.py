# A substring is a DNA substring if it contains only the following characters:
# 'A', 'C', 'T', 'G'. Given a string, write a function that determines the
# length of the longest DNA substring.

def substring_length(s):

    longest_length = 0
    cur_length = 0
    dna = {'A', 'C', 'T', 'G'}

    for c in s:
        if c in dna:
            cur_length += 1
        else:
            longest_length = max(longest_length, cur_length)
            cur_length = 0

    longest_length = max(longest_length, cur_length)
    return longest_length

# Let's say we're given a 2D array containing characters and a target word.
# A word can be created from this 2D array by moving up, down, left, or right,
# but you aren't allowed to double back/re-use steps in the same word path.
# Write a function that determines if the array contains the word.

def is_valid(coord, board, visited):
    row, col = coord
    width = len(board[0])
    height = len(board)
    return row >= 0 and row < width and \
        col >= 0 and col < board and \
        not visited[row][col]

def contains(board, target):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for _ in range(len(board[0])] for _ in range(len(board)]
    found = False
    def helper(coord, cur_index):
        nonlocal found
        row, col = coord
        if board[row][col] != target[cur_index]:
            return
        if cur_index == len(target) - 1:
            found = True
            return

        visited[row][col] = True
        for d in directions:
            r, c = d
            next = (row + r, col + c)
            if is_valid(next, board, visited):
                helper(next, cur_index + 1)
        visited[row][col] = False

    for row in range(len(board)):
        for col in range(len(row)):
            helper((row, col), 0)
            if found:
                return True

    return False
