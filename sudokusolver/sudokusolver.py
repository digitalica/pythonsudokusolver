

# In de definitie staat 0 voor een lege positie
Sudoku = [
[7, 8, 0, 0, 0, 1, 0, 0, 4],
[1, 9, 0, 0, 0, 7, 3, 8, 0],
[0, 4, 0, 0, 2, 0, 0, 1, 5],
[0, 0, 0, 0, 5, 0, 0, 9, 0],
[0, 0, 6, 3, 1, 9, 8, 0, 0],
[0, 7, 0, 0, 6, 0, 0, 0, 0],
[2, 1, 0, 0, 9, 0, 0, 3, 0],
[0, 3, 9, 2, 0, 0, 0, 4, 6],
[5, 0, 0, 1, 0, 0, 0, 7, 9]]

def printsudoku(sudoku):
    '''Printen van een sudoku op scherm'''
    for row in sudoku:
        print(row)

def solvesudoku(sudoku):
    '''Oplossen van een sudoku. De methode is  
    niet goed genoeg voor moeilijke sudoku's'''

    # De opties voor elke positie
    options = []
    for r in range(0, 9):
        options.append([0] * 9)
        for c in range(0, 9):
            options[r][c] = set(range(1, 10))    

    # Zet een cijfer op een positie
    def setKnownValueAt(row, col, value):
        # verwijder als optie in de rij
        for c in range(0, 9):
            if value in options[row][c]:
                options[row][c].remove(value)
        # verwijder als optie in de kolom
        for r in range(0, 9):
            if value in options[r][col]:
                options[r][col].remove(value)
        # verwijder als optie in het 3x3 blok
        rs, cs = (row // 3) * 3, (col // 3) * 3
        for r in range(rs, rs + 3):
            for c in range(cs, cs + 3):
                if value in options[r][c]:
                    options[r][c].remove(value)
        # het cijfer is de enige optie hier
        options[row][col] = set([value])
        
    # stel de gegeven cijfers (en dus opties) in 
    for r in range(0, 9):
        for c in range(0, 9):
            value = sudoku[r][c]
            if value != 0:
                setKnownValueAt(r, c, value)

    # Elke positie die nu nog maar 1 optie heeft,
    # is duidelijk, daar zetten we dat cijfer.
    # Dit herhalen we zolang het kan.
    makingProgress = True
    while makingProgress:
         makingProgress = False
         for r in range(0, 9):
            for c in range(0, 9):
                if sudoku[r][c] == 0:
                    if len(options[r][c]) == 1:
                        value = list(options[r][c])[0]
                        sudoku[r][c] = value
                        setKnownValueAt(r, c, value)
                        makingProgress = True

#  Het hoofdprogramma is nu eenvoudig
print("Begin sudoku:")
printsudoku(Sudoku)
print("Oplossing (of zo ver als we gekomen zijn:")
solvesudoku(Sudoku)
printsudoku(Sudoku)
