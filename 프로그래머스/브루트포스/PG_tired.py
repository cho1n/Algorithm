def solution(K, dungeons):
    answer = []

    def dfs(elements, count, k):
        if not elements:
            answer.append(count)
            return

        for minimum, damage in elements:
            if k < minimum:
                answer.append(count)
                continue
            else:
                next_elements = elements[:]
                next_elements.remove([minimum, damage])
                dfs(next_elements, count + 1, k - damage)


    dfs(dungeons, 0, K)
    return max(answer)

print(solution(80, [[80,20], [50,40], [30,10]]))