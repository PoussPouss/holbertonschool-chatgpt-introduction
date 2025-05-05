#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.revealed_count = 0  # Initialisation du compteur de cases révélées
        self.total_safe_cells = width * height - len(self.mines)  # Calcul du nombre total de cases sans mines

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # Coordonnées invalides, continuer le jeu
            
        if self.revealed[y][x]:
            return True  # Case déjà révélée, continuer le jeu
            
        if (y * self.width + x) in self.mines:
            return False  # Mine touchée, fin du jeu
            
        self.revealed[y][x] = True
        self.revealed_count += 1
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):  # Méthode déplacée à l'intérieur de la classe
        while True:
            self.print_board()
            
            # Vérifier la condition de victoire
            if self.revealed_count >= self.total_safe_cells:
                self.print_board(reveal=True)
                print("Félicitations ! Vous avez gagné !")
                break
                
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordonnées hors limites. Veuillez entrer des valeurs entre 0 et {self.width-1} pour x et entre 0 et {self.height-1} pour y.")
                    continue
                    
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()