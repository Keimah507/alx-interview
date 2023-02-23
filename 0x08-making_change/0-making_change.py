#!/usr/bin/python3
"""
Module to solve the following problem:
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    determines the fewest number of coins needed to meet a given amount total
    :param coins: pile of coins
    :param total: total amount of coins
    :return: the fewest number of coins to meet total
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] < float('inf') else -1
