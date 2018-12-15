# What Was That?

# \a bell, \v vertical tab, \t horizontal tab, \N{insert unicode here}, \n new line, \r carriage return

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
blackslash_cat = "I'm \\ a \\ cat."

fat_cat =''' 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(tabby_cat)        #      I'm tabbed in.
print(persian_cat)      # I'm split \n on line.
print(blackslash_cat)   # I'm \ a \ cat.
print(fat_cat)
                        # I'll do a list
                        #       * Cat food
                        #       * Fishies
                        #       * Catnip
                        #       * Grass