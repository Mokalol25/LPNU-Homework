import ast

def flood_fill(grid, start_r, start_c, new_color):
    rows = len(grid)
    cols = len(grid[0])
    
    target_color = grid[start_r][start_c]
    
    if target_color == new_color:
        return grid
    
    stack = [(start_r, start_c)]
    
    while stack:
        r, c = stack.pop()
        
        if grid[r][c] == target_color:
            grid[r][c] = new_color
            
            if r > 0: 
                stack.append((r - 1, c))
            if r < rows - 1: 
                stack.append((r + 1, c))
            if c > 0: 
                stack.append((r, c - 1))
            if c < cols - 1: 
                stack.append((r, c + 1))
                
    return grid

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Помилка: Файл input.txt не знайдено!")
        return


    dimensions = lines[0].strip().split(',')
    rows, cols = int(dimensions[0]), int(dimensions[1])
    
    start_coords = lines[1].strip().split(',')
    start_r, start_c = int(start_coords[0]), int(start_coords[1])
    

    new_color = 'C'
    
    grid = []
    for line in lines[3:]:
        line = line.strip()
        if not line:
            continue
            
        clean_line = line.replace("‘", "'").replace("’", "'").rstrip(',')
        row = ast.literal_eval(clean_line)
        grid.append(row)
        
    filled_grid = flood_fill(grid, start_r, start_c, new_color)
    
    with open('output.txt', 'w', encoding='utf-8') as f:
        for row_list in filled_grid:
            f.write(str(row_list) + '\n')
            
    print("Успішно! Алгоритм відпрацював.Перевір файл output.txt")

if __name__ == '__main__':
    main()