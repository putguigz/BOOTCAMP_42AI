t = (0, 4, 132.42222, 10000, 12345.67)

print("module_0%d, ex_0%d" % (t[0], t[1]), end=' : ')
print("{:.2f}".format(t[2]), "{:.2e}".format(t[3]), "{:.2e}".format(t[4]), sep=", ")