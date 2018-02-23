print '-----------------------------------------------'
print 'Punch in existing list of servernames/instances'
print '-----------------------------------------------'
print "Press Ctrl-D to save it."
print '------------------------'
contents = []
while True:
    try:
        line = raw_input("")
    except EOFError:
        break
    contents.append(line)

print '-----------------------------------------------'
print 'Here is your fixed string for SS disabling:'
print '\n'
myString = '/'+"|".join(contents)+'/i'
print(myString)
print '\n'