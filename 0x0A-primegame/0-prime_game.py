#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of each game and returns the overall winner.

    Parameters:
        x (int): The number of rounds to play.
        nums (list): A list of integers, where each integer represents the value of n in a round.

    Returns:
        str: The name of the player that won the most rounds ("Maria" or "Ben"), or None if no winner.
    """
    
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
