import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),'../../..'))

import Tix as tix

import dummy_tin.matdb.srim_matdb as srim_matdb

if __name__ == '__main__':
    app = tix.Tk()

    #srimdata = os.path.abspath(os.path.join(os.path.dirname(__file__),'../Compound.dat'))
    srimdata = ''

    d = srim_matdb.Dialog(app, srimdata)

    app.wait_window(d)
    print d.result

    #app.mainloop()
