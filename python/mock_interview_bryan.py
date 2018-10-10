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

# doggy
# alabs
# yogdg
# saalb

# out: [[doggy, yogdg], [alabs, saalb]]

# sorted(s)

def group_anagrams(arr):
    anagram_groupings = {}
    for s in arr:
        sorted_s = sorted(s)
        if sorted_s in anagram_groupings:
            anagram_groupings[sorted_s].append(s)
        else:
            anagram_groupings[sorted_s] = [s]

    return [anagram_groupings[k] for k in anagram_groupings.keys()]

#n = 3

#[
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
#]

def valid_parens(n):
    nestings = []

    def valid_parens_helper(s, oparens, parens_left):
        if oparens == 0 and parens_left == 0:
            nestings.append(s)
        if oparens > 0:
            valid_parens_helper(s + ")", oparens - 1, parens_left)
        if parens_left > 0:
            valid_parens_helper(s + "(", oparens + 1, parens_left - 1)

    valid_parens_helper("", 0, n)
    return nestings

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        PARENS = []

        def create_parens(p_str, num_opens, num_closed, balance):
            if balance < 0 or num_opens < 0 or num_closed < 0:
                return
            if num_opens == 0 and num_closed == 0 and balance == 0:
                PARENS.append(p_str)
                return
            create_parens(p_str + "(", num_opens-1, num_closed, balance+1)
            create_parens(p_str + ")", num_opens, num_closed-1, balance-1)

        create_parens("", n, n, 0)
        return PARENS

# https://leetcode.com/problems/unique-paths/description/
#

# row x col
# 2 x 3

# 2,3 2,2 2,1
# 1,3 1,2 1,1

# 1 1 1
# 1 2 3

def unique_paths(m, n):

    paths = 0
    def get_paths(m, n):
        nonlocal paths
        if m == 1 and n == 1:
            paths += 1
        if m > 1:
            get_paths(m - 1, n)
        if n > 1:
            get_paths(m, n - 1)

    get_paths(m, n)
    return paths

# memo[i][j] = memo[i-1][j] + memo[i][j-1]
def unique_paths(m, n):
    memo = [[1 for _ in range(m)] for _ in range(n)]
    if m == 1 or n == 1:
        return 1
    for r in range(1, n):
        for c in range(1, m):
            memo[r][c] = memo[r - 1][c] + memo[r][c - 1]

    return memo[-1][-1]
