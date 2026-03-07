def max_hamsters(S, C, hamsters):
    left, right = 0, C
    answer = 0

    while left <= right:
        k = (left + right) // 2

        if k == 0:
            left = 1
            continue

        costs = []
        for H, G in hamsters:
            costs.append(H + G * (k - 1))

        min_cost = min(costs)
        max_cost = max(costs)

        count = [0] * (max_cost - min_cost + 1)

        for cost in costs:
            count[cost - min_cost] += 1

        total = 0
        taken = 0

        for i in range(len(count)):
            while count[i] > 0 and taken < k:
                total += i + min_cost
                count[i] -= 1
                taken += 1

            if taken == k:
                break

        if total <= S:
            answer = k
            left = k + 1
        else:
            right = k - 1

    return answer