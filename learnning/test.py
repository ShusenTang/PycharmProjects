import sys
print 'The command line arguments are:'
for i in sys.argv:
    print i
print '\n\nThe PYTHONPATH is', sys.path, '\n'


if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'

print dir(sys)
a=5
del a
print dir()