# with formated strings you can use placeholders in strings

price = 56
txt = f"Your price is {price}, you wanna pay it now?"
print(txt)

# Formatting Types
# ------------------------------------------------------------------------
# :<    Left aligns the result (within the available space)
# :>    Right aligns the result (within the available space)
# :^    Center aligns the result (within the available space)
# :=    Places the sign to the left most position
# :+    Use a plus sign to indicate if the result is positive or negative
# :-    Use a minus sign for negative values only
# :     Use a space to insert an extra space before positive numbers
#       (and a minus sign before negative numbers)
# :,    Use a comma as a thousand separator
# :_    Use an underscore as a thousand separator
# :b    Binary format
# :c    Converts the value into the corresponding Unicode character
# :d    Decimal format
# :e    Scientific format, with a lower case e
# :E    Scientific format, with an upper case E
# :f    Fix point number format
# :F    Fix point number format, in uppercase format
#       (show inf and nan as INF and NAN)
# :g    General format
# :G    General format (using an upper case E for scientific notations)
# :o    Octal format
# :x    Hex format, lower case
# :X    Hex format, upper case
# :n    Number format
# :%    Percentage format
