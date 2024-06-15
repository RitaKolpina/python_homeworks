def bank(x, y):
    rate = 0.10
    sum_after_y_years = x * (1 + rate) ** y
    return sum_after_y_years

x = float(input("What amount of money? "))
y = int(input("How many years? "))

result = bank(x, y)
print(f"If you deposit ${x} for {y} years you will have ${result:.2f} ")