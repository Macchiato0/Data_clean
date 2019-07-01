import re
"""
search() takes the pattern and text to scan, 
and returns a Match object when the pattern is found. If the pattern is not found, search() returns None.
search() looks for single instances of literal text strings
"""
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print 'Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e])

"""
Compiling Expressions
re includes module-level functions for working with regular expressions as text strings, but it is usually more efficient 
to compile the expressions your program uses frequently. The compile() function converts an expression string into a RegexObject.
"""

#Multiple Matches
text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print 'Found "%s"' % match

#Found "ab"
#Found "ab"
"""
finditer() returns an iterator that produces Match instances instead of the strings returned by findall().
"""
text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print 'Found "%s" at %d:%d' % (text[s:e], s, e)
#Found "ab" at 0:2
#Found "ab" at 5:7

"""
splite and sub
"""

re.split("\s", text)
#return a list of strings split by space

re.sub("\s", "9", text)
#return text with its all spaces "\s" substituded by 9

"""
remove punctuatuion
substituting(re.sub) all NON[alphanumeric characters(\w) and spaces(\s)] with empty string
structure: [^arn] :Returns a match for any character EXCEPT a, r, and n
"""
s = "string. With. Punctuation?"
s = re.sub(r'[^\w\s]','',s)


"""
\w
Returns a match where the string contains any word characters 
(characters from a to Z, digits from 0-9, and the underscore _ character)
"""
