lines = open('output.dat', 'r').read()
rows = lines.split('\n\n')
out = open('output.csv', 'w')
out.write('Cow,Action,Amount,ID0,Card0,Money0,Wager0,Alive0,ID1,Card1,Money1,Wager1,Alive1,ID2,Card2,Money2,Wager2,Alive2,ID3,Card3,Money3,Wager3,Alive3,ID4,Card4,Money4,Wager4,Alive4\n')
for r in rows:
    li = r.strip().split()
    out.write(','.join(li[1:2] + li[3:]) + '\n')
out.close()
