# łączenie stringów
prefix = " python is an "
suffix = "awesome language"

astr = prefix + suffix
print(astr)

astr = astr.replace("language", "snake.")   #.replace zmienia zadeklarowane słowo
astr = astr * 2
astr = astr.replace("snake.", "language",1)
print(astr)

print(astr.count("an"))