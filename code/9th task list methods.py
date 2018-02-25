
alpha = ["a", "b", "c", "d"]
alpha.append("e")       #funkcja dodająca zawartość do tablicy
alpha = alpha + ["f"]
#alpha = alpha + ["e","f"]
print(alpha)

d_index = alpha.index("d")          #funkcja sprawdzająca na którym miejscu jest komórka
print("d_index: " + str(d_index))
del alpha[d_index]                  #usuwanie indeksu z tablicy
print(alpha)

alpha.remove("c")
print(alpha)