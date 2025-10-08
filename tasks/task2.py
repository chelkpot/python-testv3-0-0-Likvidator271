# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    vremya = int(input())
    Z_vremya = vremya % 1440
    chasiki = Z_vremya // 60
    minutki = Z_vremya % 60
    print(chasiki, minutki)



   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()