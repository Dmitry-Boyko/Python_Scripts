# ------------------- #
# v1
# ------------------ #

#!/usr/bin/python
with open('first.txt', 'r') as file1:
    with open('second.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('some_output_file.txt', 'a') as file_out:
    for line in same:
        file_out.write(line)

# ------------------- #
# v2
# ------------------- #

#!/usr/bin/python

# find the difference between two texts
# tested with Python24   vegaseat  6/2/2005
import difflib
text1 = """The World's Shortest Books:
Human Rights Advances in China
Add some text lines that are not in either
1. first different line
2. line 2 added
3. also a third
"My Plan to Find the Real Killers" by OJ Simpson
"Strom Thurmond:  Intelligent Quotes"
America's Most Popular Lawyers
Career Opportunities for History Majors
Different Ways to Spell "Bob"
Dr. Kevorkian's Collection of Motivational Speeches
Spotted Owl Recipes by the EPA
The Engineer's Guide to Fashion
Ralph Nader's List of Pleasures
"""
text2 = """The World's Shortest Books:
Human Rights Advances in China
"My Plan to Find the Real Killers" by OJ Simpson
"Strom Thurmond:  Intelligent Quotes"
America's Most Popular Lawyers
Career Opportunities for History Majors
Different Ways to Sell "Bob"
Dr. Kevorkian's Collection of Motivational Speeches
Spotted Owl Recipes by the EPA
The Engineer's Guide to Passion
Ralph Nader's List of Pleasures
Another line that is different
1. first different line
"""
# create a list of lines in text1
text1Lines = text1.splitlines(1)
text1Lines.sort()                 ## uncommented to sort
print "Lines of text1:"
for line in text1Lines:
  print line,
print
# dito for text2
text2Lines = text2.splitlines(1)
text2Lines.sort()                 ## uncommented to sort
print "Lines of text2:"
for line in text2Lines:
  print line,
print
diffInstance = difflib.Differ()
diffList = list(diffInstance.compare(text1Lines, text2Lines))
print '-'*50
print "Lines different in text1 from text2:"
for line in diffList:
  if line[0] == '-':
    print line,
print
