import sys


def solve_bracelet_case(s1, s2):
    # optimize strings
    set_a = set(s1)
    set_b = set(s2)
    common_alphabet = set_a & set_b
    if not common_alphabet:
        return 0
    brace1 = ''.join(c for c in s1 if c in common_alphabet)
    brace2 = ''.join(c for c in s2 if c in common_alphabet)
    if not brace1 or not brace2:
        return 0
    if len(brace2) < len(brace1):
        brace1, brace2 = brace2, brace1
    # find the maximum common length
    max_len = 0
    for variation in get_all_variations(brace1):
        local_len = edit_dist_delete_only(variation,brace2)
        max_len = max(max_len, local_len)
    return max_len


def get_all_variations(s):
    variants = []
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        variants.append(rotated)
        variants.append(rotated[::-1])  # Auch umgekehrt

    return variants

def edit_dist_delete_only(s,t):
    n = len(s)
    m = len(t)
    # initialize table D for edit distances
    D = [[0] * (m + 1) for _ in range(n + 1)]
    # Base cases
    """
    # DANG Zu langsam
    for i in range(n + 1):
        D[i][0] = i  # Lösche alle i Zeichen aus s
    for j in range(m + 1):
        D[0][j] = j  # Lösche alle j Zeichen aus t
    # Fill D, only delete operations!
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                D[i][j] = D[i - 1][j - 1]  # Keine Operation nötig
            else:
                D[i][j] = min(
                    D[i - 1][j] + 1,  # Lösche aus s
                    D[i][j - 1] + 1  # Lösche aus t
                )
            
    total_deletions = D[n][m]
    lcs_length = (n + m - total_deletions) // 2
    return lcs_length
    """
    #--- test obs reicht ---
    # longest common subsequence
    # Use only two rows for space optimization
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return prev[m]
    # ----



input = sys.stdin.readline
t = int(input())
for case in range(1, t + 1):
    if case > 1:
        line = input()
    a = input().strip()
    b = input().strip()

    result = solve_bracelet_case(a, b)
    print(f"Case #{case}: {result}")
