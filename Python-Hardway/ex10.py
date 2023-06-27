# What was that 

# how to put a slash inside a string and \t -> tab
# //


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\ non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Finishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# Escape Sequences 
# Escape
# \\ -> backslash (\)
# \' -> Single-quote (')
# \" -> Double-quote (")
# \a -> ASCII bell (BEL)
# \b -> ASCII backspace (BS)
# \f -> ASCII formfeed (FF)
# \n -> ASCII linefeed (LF)
# \N{name} -> Character named name in the Unicode database (unicode only)
# \r -> carriage return (CR)
# \t -> Horizontal tab (TAB)
# \uxxxx -> Character with 16-bit hex value xxxx
# \Uxxxxxxx -> Character with 32-bit hex value xxxxxxx
# \v - ASCII vertical tab (VT)
# \ooo -> Character with octal value 000
# \xhh -> Character with hex value hh
