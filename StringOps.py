"""
Consider the given string "Python Programming" and perform the following operation on the string
Display "Python"
Display "Programmimg"
Find whether "java" is there or not. If not then include "java" in between "python" and "programming"
Find the length of the new string
Count the number of words in the string.
Capitalize each word in the string.
Remove all the spaces and print the string.
Print the frequency of "A", "P", "R" and "M".
"""
st = "Python Programming"
print(st[0:6])
print(st[7:])

if "java" not in st:
  jst = st.split()[0] + " " + "java" + " " + st.split()[1]
else:
  print(f"'java' is present in the string at index {st.find("java")}")

jst =  st.split()[0] + " " + "java" + " " + st.split()[1]
print(f"Length of the updated string is {len(jst)}")
print(f"Number of words is {len(jst.split())}")
c_st = jst.upper()
print(f"String after capitalization = {c_st}")
nospace_st = c_st.split()[0] + c_st.split()[1] + c_st.split()[2]
print(f"String after removing spaces {nospace_st}")
print(f"Frequency\n'A' = {nospace_st.count('A')} \n'P' = {nospace_st.count('P')} \n'R' = {nospace_st.count('R')} \n'M' = {nospace_st.count('M')}")
