#Tuple=(64,65,'A')
#Max=max(Tuple)
#print(Max)

Tuple = (64, 65, 'A')
# Filter out non-integer values
filtered_tuple = [x for x in Tuple if isinstance(x, int)]
Max = max(filtered_tuple)
print(Max)
