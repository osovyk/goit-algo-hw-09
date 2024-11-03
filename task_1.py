import timeit

def time_function(func, *args, number=1000):
    execution_time = timeit.timeit(lambda: func(*args), number=number)
    return execution_time / number

# Жадібний алгоритм
def find_coins_greedy(amount, denominations):
    denominations.sort(reverse=True)
    result = {}
    for coin in denominations:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

# Алгоритм динамічного програмування
def find_min_coins(amount, denominations):
    denominations.sort()
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in denominations:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin > 0:
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1
            amount -= coin

    # Повертаємо результат у відсортованому порядку
    sorted_result = dict(sorted(result.items()))
    return sorted_result


denominations = [50, 25, 10, 5, 2, 1]
amount = 113

greedy_result = find_coins_greedy(amount, denominations)
min_coins_result = find_min_coins(amount, denominations)

# Вимірюємо час
greedy_time = time_function(find_coins_greedy, amount, denominations)
min_coins_time = time_function(find_min_coins, amount, denominations)

print("Час виконання жадібного алгоритму:", greedy_time)
print("Жадібний алгоритм:", greedy_result)
print("Час виконання динамічного програмування:", min_coins_time)
print("Динамічне програмування:", min_coins_result)

