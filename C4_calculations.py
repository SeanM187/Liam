def to_celsius(to_convert):
    answer = (to_convert - 32) * 5 / 9
    return answer


def to_fahrenheit(to_convert):
    answer = to_convert * 1.8 + 32
    return answer


to_C_test = [0, 100, -459]
to_F_test = [0, 100, 40, -273]

for item in to_C_test:
    print("{} F is {:.0f} C".format(item, to_celsius(item)))

print()

for item in to_C_test:
    print("{} F is {:.0f} C".format(item, to_celsius(item)))

print()
