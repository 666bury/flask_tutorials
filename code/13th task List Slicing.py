
a = list(range(0, 10))
print(a)                #wyświetlenie całego predziału

print(a[0:5])           #wyświetlenie przedziału od 0 do 5
print(a[2:len(a)])      #wyśwetlenie przedziału od 2 i do końca
print(a[:])

print(a[:])             #bez podania początku i końca funkcja wyświetla cały przedział
print(a[1:8:2])         #wyświetlenie przedziału i kroku

print(a[-1])            #wyświetlanie komórek od końca nie ma komórki -0
print((a[2:-2]))        #przedział od 2 do 7
print(a[::-1])          #odwrócenie listy z krokiem 1
print((a[::-2]))        #wyświetlenie listy z kirokiem 2