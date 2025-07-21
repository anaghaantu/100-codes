def count_decodings(digits):
    n = len(digits)
    if n == 0 or digits[0] == '0':
        return 0

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        one_digit = int(digits[i - 1])
        two_digit = int(digits[i - 2:i])

        if one_digit >= 1:
            dp[i] += dp[i - 1]

        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


sequence = input("Enter digit sequence: ")
print("Total possible decodings:", count_decodings(sequence))
