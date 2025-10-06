from typing import Dict, List

COINS = [50, 25, 10, 5, 2, 1]

# --- Жадібний алгоритм ---
def find_coins_greedy(amount: int, coins: List[int] = COINS) -> Dict[int, int]:
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# --- Алгоритм динамічного програмування ---
def find_min_coins(amount: int, coins: List[int] = COINS) -> Dict[int, int]:
    dp = [0] + [float("inf")] * amount
    prev = [-1] * (amount + 1)
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin
    res = {}
    curr = amount
    while curr > 0:
        coin = prev[curr]
        if coin == -1:
            return {}
        res[coin] = res.get(coin, 0) + 1
        curr -= coin
    return res

if __name__ == "__main__":
    amount = 113
    print("Жадібний алгоритм:", find_coins_greedy(amount))
    print("Динамічне програмування:", find_min_coins(amount))