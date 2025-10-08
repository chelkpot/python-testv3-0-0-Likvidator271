# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    z = int(input())
    z2 = z + (2 - (z & 1))
    print(z2)

    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()