# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    def zKZkzkzkz(evro):
        kupuri = [100, 20, 10, 5, 1]
        vsego = 0
        for kupura in kupuri:
            if evro >= kupura:
                num_kupuri =  evro // kupura
                vsego += num_kupuri
                evro -= num_kupuri * kupura
        return vsego

    evro = int(input())
    otvet = zKZkzkzkz(evro)
    print(otvet)



# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()