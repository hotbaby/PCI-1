import docclass2

# docclass2.getwords('python is a dynamic language')

cl = docclass2.naivebayes(docclass2.getwords)

cl.train('pythons are constrictors', 'snake')
cl.train('python has dynamic types', 'language')
cl.train('python was developed as scripting language', 'language')

print cl.classify('dynamic programming')
print cl.classify('boa constrictors')
exit()
