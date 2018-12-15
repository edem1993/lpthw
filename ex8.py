# Printing, Printing

formatter = "{} {} {} {}"

# puts numbers in {}
print(formatter.format(1, 2, 3, 4))
# puts "strings" in {}
print(formatter.format("one", "two", "three", "four"))
# puts boolean into {}
print(formatter.format(True, False, False, True))
# puts variable 'formatter' into {} => 4 {} into 1 {} == 16 {}
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))