a = 10
x = "There are %d types of people." % a
binary = "Binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print(x)
print(y)
z = "There are 10 types of people."

print("I said: %s." % x)
print("I also said: %s"  % y)
hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"
print("Isn't that joke so funny?! %r" % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)