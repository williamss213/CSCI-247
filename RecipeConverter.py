print "----Original Recipe----"
print "Enter the amount of flour {cups}: ",
flour = raw_input()
print "Enter the amount of water {cups}: ",
water = raw_input()
print "Enter the amount of salt {teaspoons}: ",
salt = raw_input()
print "Enter the amount of yeast {teaspoons}: ",
yeast = raw_input()
print "Enter the loaf adjustment factor (e.g. 2.0 double the size) "
ratio = raw_input()

print "\n ----Modified Recipe----"
print "Flour: %.2f cups" % (float(flour)*float(ratio))
print "Water: %.2f cups" % (float(water)*float(ratio))
print "Salt: %.2f teaspoons" % (float(salt)*float(ratio))
print "Yeast: %.2f teaspoons" % (float(yeast)*float(ratio))

print "\n ----Modified Recipe in Grams----"
print "Flour: %.2f grams" % (float(flour)*120*float(ratio))
print "Water: %.2f grams" % (float(water)*236.59*float(ratio))
print "Salt: %.2f grams" % (float(salt)* 5.69*float(ratio))
print "Yeast: %.2f grams" % (float(yeast) * 2.83*float(ratio))
print "Happy Baking!"

