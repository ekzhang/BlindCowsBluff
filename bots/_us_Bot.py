from keras.models import load_model
import sys

model = None

def init():
    print 'NAME NNBot'

def players(n, ids, ps):
    pass

def cards(x, k):
    pass

def ante(init, rtd):
    pass

def ready():
    pass

def round_start(rnum, start_id, ante):
    pass

def turn(ids, x, p, w, active):
    pass

def endround(winnings, ids, x, p):
    pass

def endgame():
    sys.exit(0)

def main():
    global model
    model = load_model('_us_model.10.hdf5')

    while True:
        pass


if __name__ == '__main__':
    main()
