from wlutils import flattn
import numpy as np
import json

def mvTL_PT ():
    with open('./sim/conn/conn_dend_PT.json') as f: ptconn=json.load(f)
    locs = np.array(flattn([y for x in ptconn.values() if type(x) is dict for y in x.values()]))
    rlocs = np.array([x-ptconn['fixedSomaY'] for x in locs])
    print("Length: %d; Range: %g (%d) to %g (%d)\n"%(len(rlocs),rlocs.min(),np.sum(rlocs<0),rlocs.max(),np.sum(rlocs>0)))
