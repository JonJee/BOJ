# a, b = input().split()
# aa = a.replace('6', '5')
# bb = b.replace('6', '5')
# aaa = a.replace('5', '6')
# bbb = b.replace('5', '6')
# print(int(aa) + int(bb), int(aaa) + int(bbb))
a=input().split();print(*map(sum,[[int(i.replace('6','5'))for i in a],[int(i.replace('5','6'))for i in a]]))