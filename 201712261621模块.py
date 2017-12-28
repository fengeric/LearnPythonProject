import sys

print('the command line grguments are:')
for i in sys.argv:
    print(i)

print('\n\nthe pythonpath is', sys.path, '\n')
#-----------------------------------------------------------------------------
print(sys.version_info) #sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)
print(sys.version_info.major == 3) #True
