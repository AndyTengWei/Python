import os

current_path = os.getcwd()
print(current_path)
print '------------------------------------'

i = 12

print id(i)

i += 3

print id(i)
print '------------------------------------'

l1 = range(3)
l2 = l1
l2 += [3]
print l1
print l2
print '------------------------------------'

l1 = range(3)
l2 = l1
l2 = l2 + [3]
print l1
print l2
print '------------------------------------'

x = range(3)
y = x

print 'X id is:' + str(id(x))
print 'Y id is:' + str(id(y))

x.append(3)
print x
print y
print id(x)
print id(y)

print '------------------------------------'

print hasattr(int, '__iadd__')
print hasattr(list, '__iadd__')

print '------------------------------------'

print str(2) + str(2) + '1'


edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
datebase = [edward, john]


greeting = 'Hello'

print (greeting[0] + greeting[2] + greeting[-3] + greeting[-1])

