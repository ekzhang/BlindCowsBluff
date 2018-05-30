from keras.models import load_model
import sys

try:
    input = raw_input
except:
    pass

n = None
model = None
my_id = None
card_range = None

def init(id_):
    print('NAME SVMBot')
    global my_id
    my_id = id_

def players(n, ids, ps):
    # TODO: get model
    global model
    model = load_model('_us_model.01.hdf5')

def cards(x, k):
    global card_range
    card_range = x

def ante(init, rtd):
    # not needed
    pass

def ready():
    # not needed
    pass

def round_start(rnum, start_id, ante):
    # not needed
    pass

def turn(ids, x, p, w, active):
    global model
    global n

    def rotate(li, amt):
        return li[amt:] + li[:amt]

    ids    = rotate(ids, my_id)
    x      = rotate(x, my_id)
    p      = rotate(p, my_id)
    w      = rotate(w, my_id)
    active = rotate(active, my_id)

    x = np.array([x, p, w, active]).T.flatten()[1:]
    p = model.predict(x)
    if p > 0.5:
        print 'CALL'
    else:
        print 'FOLD'

def endround(winnings, ids, x, p):
    # not needed
    pass

def endgame():
    sys.exit(0)

def main():
    global n

    while True:
        line = input().split()
        func = line[0]
        if func == 'INIT':
            init(int(line[1]))
        elif func == 'PLAYERS':
            n = int(line[1])
            ids = []
            ps = []
            for i in range(n):
                i, p = [int(x) for x in input().split()]
                ids.append(i)
                ps.append(p)
            players(int(line[1]), ids, ps)
        elif func == 'CARDS':
            cards(int(line[1]), int(line[2]))
        elif func == 'ANTE':
            ante(int(line[1]), int(line[2]))
        elif func == 'READY':
            ready()
        elif func == 'ROUND':
            round_start(int(line[1]), int(line[2]), int(line[3]))
        elif func == 'TURN':
            args = zip(*[[int(x) for x in input().split()] for _ in range(n)])
            turn(*args)
        elif func == 'ENDROUND':
            args = zip(*[[int(x) for x in input().split()] for _ in range(n)])
            endround(winnings, *args)
        elif func == 'ENDGAME':
            endgame()
        else:
            raise ValueError("Protocol not found: " + func)

if __name__ == '__main__':
    main()
