a = ['India','Australia','Turkey']
a.append('Sweden')
a.remove(a[2])
a.insert(2, 'Poland')
print(a)

b = {'India','Australia','Turkey'}
b.update(['Sweden'])
b.remove('Turkey')
print(id(b))