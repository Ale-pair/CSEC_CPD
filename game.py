def count_guest_uniform_games(n, uniforms):
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j:  # We don't check the game where the team is both the home and the guest
                hi = uniforms[i][0]
                aj = uniforms[j][1]
                if hi == aj:
                    count += 1
    return count

# Input Reading
n = int(input())
uniforms = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_guest_uniform_games(n, uniforms))
