# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    chislo = int(input())
    sotka = chislo // 100 
    desyatka = (chislo // 10) % 10
    edinica = chislo % 10 
    x = sotka + desyatka + edinica
    print(x)


    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()