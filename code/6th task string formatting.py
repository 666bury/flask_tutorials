n = 11
f = 1.2345678
s = "computer"

print("my number is {:d}".format(n))
print("my number is {:b}".format(n))
print("my number is {:x}".format(n))


#there are many format types such as:
#e - exponents
#b - binary (base 01)
#o - octal (base 8)
#d - decimal (base 16)
#x - hexadecimal (base 16)
#f - floats (decimal numbers)
#s - strings (default if none is specified)


# {:3f}.format(2) powoduje wstawienie trzech zer po przecinku
print("{:f}".format(f))
print("{:.3f}".format(f))
print("{:.1f}".format(20))

print("{0} {1} {2}".format(n,f,s))

print("{name} own(s) {amount} of {object}".format(
    name = "William",
    amount = 5,
    object = "cats"

))