cash = 19867324678987.99  
print("${:,.2f}".format(cash))

# Divide cash evenly by 5
evenSplit = float(cash) / 5
# format using US Currency
evenSplit = "${:,.2f}".format(evenSplit)
print(evenSplit)


# For Fun - print cash in currency format
print("${:,.2f}".format(cash))

