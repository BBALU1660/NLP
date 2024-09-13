def min_edit_distance(str1, str2):
    len1, len2 = len(str1), len(str2)
    
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Fill the dp table
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    i, j = len1, len2
    operations = []
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i-1] == str2[j-1]:
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            operations.append(f"Delete '{str1[i-1]}' from position {i}")
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
            operations.append(f"Insert '{str2[j-1]}' at position {i+1}")
            j -= 1
        else:
            operations.append(f"Replace '{str1[i-1]}' with '{str2[j-1]}' at position {i}")
            i -= 1
            j -= 1

    operations.reverse()
    return dp[len1][len2], operations

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

distance, ops = min_edit_distance(str1, str2)
print("Minimum Edit Distance:", distance)
print("Operations performed:")
for op in ops:
    print(op)
