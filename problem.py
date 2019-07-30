# Problem:
# In a Cricket League, the amount that each player is paid varies from match to match. The match fee depends on the quality of opposition, the venue etc. The match fees for each match in the new season have been announced in advance. Each team has to enforce a mandatory rotation policy so that no player ever plays three matches in a row during the season. Vijay is the captain and chooses the team for each match. He wants to allocate a playing schedule for himself to maximize his earnings through match fees during the season. 

# Input format
# Line 1: A single integer N, the number of games in the league season.

# Line 2: N non-negative integers, where the integer in position i represents the fee for match i.

# Output format
# The output consists of a single non-negative integer, the maximum amount of money that Vijay can earn during this the season. 

# Sample Input 1
# 5
# 10 3 5 7 3

# Sample Output 1
# 23
# (Explanation: 10+3+7+3)

# Sample Input 2
# 8
# 3 2 3 2 3 5 1 3

# Sample Output 2
# 17
# (Explanation: 3+3+3+5+3)


max_consec = 2
matches = int(input())
amounts = [int(amount) for amount in input().split(' ')]
total = sum(amounts)

if max_consec == matches:
    print(total)
else:
    sub_list = amounts[: max_consec + 1]
    
    minimum_val = min(sub_list)
    minimum_idx = sub_list.index(minimum_val)
    
    for idx in range(max_consec + 1, matches):
        
        if idx - minimum_idx >= max_consec:
            minimum_val = min(sub_list[idx - (max_consec + 1) : idx + 1])
            minimum_idx = sub_list.index(minimum_val)

        sub_list.append(minimum_val + amounts[idx])

        if sub_list[idx] < minimum_val:
            minimum_val = sub_list[idx]
            minimum_idx = idx

    print(total - min(sub_list[matches - (max_consec + 1) :]))


# Rather than checking it iteratively and find the max amount. We here need to find the least amount that we can remove from the total amount. This is a dynamic programming problem.
# I'm using a min-heap here.

# So I'm initially taking first (max consecutive numbers allowed + 1) numbers.
# Every time I move to the next element I add the minimum number from the previous set, pop out the head element and add a new number from the tail.

# Taking your sample input
# Initial input => [3, 2, 3, 2, 3, 5, 1, 3]
# Taking the first 3 numbers that are [3, 2, 3] and taking the minimum from it
# Now moving to the next element that is == 2
# Adding the minimum number to it i.e. 2 and popping the head element.
# So the next list is [2, 3, 4]
# Then following the same pattern.
# These are the lists that are found in the respective order.
# [3, 2, 3] - initial
# [2, 3, 4] - removing the head and adding min == 2 to next element and appending
# [3, 4, 5] - removing the head and adding min == 2 to next element and appending
# [4, 5, 8] - removing the head and adding min == 3 to next element and appending
# [5, 8, 5] - removing the head and adding min == 4 to next element and appending
# [8, 5, 8] - removing the head and adding min == 5 to next element and appending.
# Now taking the minimum from this and subtracting from the total of the original list of numbers.
