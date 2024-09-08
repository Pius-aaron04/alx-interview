#!/usr/bin/python3

""" Function to determine the winner of a game played x times
with the numbers in nums.
By Maria and Ben taking turns picking prime numbers from a list.
"""


def isWinner(x, nums):
    """
    Function that determines the winner of a game played x times
    with the numbers in nums.

    Args:
      x (int): Number of rounds to be played.
      nums (list): List of integers where each integer represents
                  the maximum number in the range [1, n] for each game.

    Returns:
      str: "Maria" if Maria wins more games, "Ben" if Ben wins more games.
          None if there's a tie.
    """
    # If there are no games to be played or the nums list is empty, return None
    if x < 1 or not nums:
        return None

    def primeSeive(n):
        """
        function to find all prime numbers less than
        or equal to n.

        Args:
          n (int): The upper limit to find primes within.

        Returns:
          list: A list of prime numbers up to n.
        """
        # initialize a boolean list to find prime numbers up to n
        isPrime = [True] * (n + 1)
        isPrime[0] = isPrime[1] = False
        p = 2
        # Loop over each number to mark its multiples as non-prime
        while (p * p <= n):
            if isPrime[p]:
                for multiple in range(p * p, n + 1, p):
                    isPrime[multiple] = False
            p += 1

        return [num for num, prime in enumerate(isPrime) if prime]

    # find the maximum number in nums to determine the range for the sieve
    primes = primeSeive(max(nums))  # generate all primes up to max_n

    def play_game(n):
        """
        Simulate the game for a given n and return the winner.

        Args:
        n (int): The maximum number in the range [1, n] for the game.

        Returns:
        int: 0 if Ben wins, 1 if Maria wins.
        """
        # set of all prime numbers up to n
        primesSet = set(primes)
        # list of primes that are within the range [1, n]
        gamePrimes = [p for p in primes if p <= n]
        currentPlayer = 0  # 0 for Maria, 1 for Ben

        # simulate the game until there are no primes left to pick
        while gamePrimes:
            # Maria or Ben picks the smallest prime number available
            prime = gamePrimes.pop(0)
            primesSet.remove(prime)
            # remove all multiples of the picked prime number from the game
            multiples = range(prime, n + 1, prime)
            gamePrimes = [p for p in gamePrimes if p not in multiples]
            # switch player after each pick
            currentPlayer = 1 - currentPlayer  # 0 to 1 or 1 to 0

        # If current_player is 0, Ben wins, otherwise Maria wins
        return currentPlayer

    # Initialize counters for wins by Maria and Ben
    mariaWins = 0
    benWins = 0

    # Play the game for each number in nums
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            benWins += 1
        else:
            mariaWins += 1

    # Determine the overall winner based on the number of games won by each
    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
