import matplotlib.pyplot as plt

lista = [3, 7, 4, 9, 5, 2, 6, 1]

fig, ax = plt.subplots()
ax.set_title("Sortowanie przez wybieranie")
bar_rects = ax.bar(range(len(lista)), lista, align="edge")

def update(lista, rects):
    for rect, val in zip(rects, lista):
        rect.set_height(val)

for i in range(len(lista)):
    min_idx = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[min_idx]:
            min_idx = j
    lista[i], lista[min_idx] = lista[min_idx], lista[i]
    update(lista, bar_rects)
    plt.pause(0.5)

plt.show()
