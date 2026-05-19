import os

def solve_ijones(W: int, H: int, grid: list[str]) -> int:
    if W == 1:
        return 1 if H == 1 else 2

    letter_sum = [0] * 26
    
    prev_paths = [1] * H

    for i in range(H):
        char_idx = ord(grid[i][0]) - ord('a')
        letter_sum[char_idx] += 1

    for j in range(1, W):
        curr_paths = [0] * H
        
        for i in range(H):
            ch = grid[i][j]
            char_idx = ord(ch) - ord('a')
            
            ways = letter_sum[char_idx]
            
            if grid[i][j-1] != ch:
                ways += prev_paths[i]
                
            curr_paths[i] = ways
            
        for i in range(H):
            char_idx = ord(grid[i][j]) - ord('a')
            letter_sum[char_idx] += curr_paths[i]
            
        prev_paths = curr_paths

    if H == 1:
        return prev_paths[0]
    else:
        return prev_paths[0] + prev_paths[H-1]
