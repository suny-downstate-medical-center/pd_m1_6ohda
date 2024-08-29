from wlutils import flattn
import numpy as np

def mvTL_PT ():
    with open('./sim/conn/conn_dend_PT.json') as f: ptconn=json.load(f)
    locs = np.array(flattn([y for x in ptconn.values() if type(x) is dict for y in x.values()]))


