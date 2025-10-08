# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    sekundi = int(input()) 
    chasi = sekundi // 3600 
    ostatki_secund = sekundi % 3600
    minetki = ostatki_secund // 60 
    sekundi = ostatki_secund % 60

    print(f"{chasi}:{minetki:02d}:{sekundi:02d}")






   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()