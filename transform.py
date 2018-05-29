import numpy as np

lines = open('output.dat', 'r').read()
rows = lines.split('\n\n')
out = open('output.csv', 'w')
out2 = open('output-labels.csv', 'w')

cols = 'Cow,Action,Amount,ID0,Card0,Money0,Wager0,Alive0,ID1,Card1,Money1,Wager1,Alive1,ID2,Card2,Money2,Wager2,Alive2,ID3,Card3,Money3,Wager3,Alive3,ID4,Card4,Money4,Wager4,Alive4,ID5,Card5,Money5,Wager5,Alive5'.split(',')
out.write(','.join(cols) + '\n')
out2.write('Winner\n')

cards = []
pre = []

def clr():
    global pre

    winner = np.argmax(cards)
    for p in pre:
        if p == winner:
            out2.write('1\n')
        else:
            out2.write('0\n')
    pre = []

for r in rows:
    if not r:
        continue
    li = r.strip().split()
    if li[0] == 'ROUND_START':
        li = li[1:]
        if pre:
            clr()
        cards = [0 for _ in range(6)]

    li = li[1:2] + li[3:]
    out.write(','.join(li) + '\n')

    pre.append(int(li[0]))
    for i in range(6):
        col = 'Card' + str(i)
        val = li[cols.index(col)]
        if val != 0:
            cards[i] = val

if pre:
    clr()

out.close()
out2.close()
