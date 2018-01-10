#!/usr/bin/env python3.6
import os
import sys
import json

from glob import iglob
from subprocess import check_output, Popen, PIPE

from joblib import Parallel, delayed

# from collections import namedtuple
# State = namedtuple('State',  ['player', 'round_num', 'ts'])


def build_tesseract(*extra):
    r = ('tesseract', 'stdin', 'stdout')
    if extra:
        return r + extra
    return r


def build_crop(f, crop):
    return ('convert', f, '-crop', crop, 'png:-')


def single(fname):
    start_index = fname.index('thumb') + len('thumb')

    round_crop = Popen(build_crop(fname, '55x18+312+70'), stdout=PIPE)
    player_crop = Popen(build_crop(fname, '225x35+110+970'), stdout=PIPE)

    player = check_output(build_tesseract(), stdin=player_crop.stdout), 
    round_num = check_output(build_tesseract('./round.config'),
        stdin=round_crop.stdout), 

    os.remove(fname)

    return {
            'player': player[0].decode('utf-8').strip(),
            'round_num': round_num[0].decode('utf-8').strip(),
            'ts': fname[start_index:-4]
        }


if __name__ == '__main__':
    r = Parallel(n_jobs=7, verbose=5)(
            delayed(single)(i) 
            for i in iglob(f'{sys.argv[-1]}/thumb*png')
        )

    with open(f'{sys.argv[-1]}.json', 'w') as f:
        json.dump(r, f, indent=2)
