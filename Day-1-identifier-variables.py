import keyword

# Identifiers are names used for variables, functions, classes, and other objects.

# Valid identifier examples
name = "Khan"             # starts with a letter
_score = 95                # may start with an underscore
student2 = "Ravi"          # may contain digits after the first character
total_marks = 180          # underscores can separate words
studentName = "Mina"       # valid, but snake_case is the usual Python style

# Python identifiers are case-sensitive: these are three different names.
value = 1
Value = 2
VALUE = 3
print("Case-sensitive values:", value, Value, VALUE)

# Invalid identifier examples (kept as strings so this file still runs)
invalid_names = ["2student", "first name", "total-marks", "class"]
print("\nIdentifier checks:")
for identifier in invalid_names:
	is_valid = identifier.isidentifier() and not keyword.iskeyword(identifier)
	print(identifier, "->", is_valid)

# Rules shown above:
# - Start with a letter or underscore, never a digit. Python supports Unicode letters too.
# - After the first character, use letters, digits, or underscores only.
# - Do not use spaces or punctuation such as hyphens.
# - Names are case-sensitive.
# - Python keywords such as 'class' cannot be used as identifiers.
# - Built-in names (functions) such as 'sum' are technically allowed, but avoid replacing them.

# Variables do not need a separate declaration; assignment creates them.
num1 = 5
num2 = 10
total = num1 + num2
print("\nThe sum of", num1, "and", num2, "is", total)

# A variable can be assigned a new value (and even a different type).
count = 3
count = count + 1
print("Updated count:", count)
count = "four"
print("Count as text:", count)

# Multiple assignment and swapping values
first, second = "red", "blue"
first, second = second, first
print("After swapping:", first, second)

# Uppercase names are a convention for values intended to stay constant.
MAX_RETRIES = 3
print("Maximum retries:", MAX_RETRIES)
