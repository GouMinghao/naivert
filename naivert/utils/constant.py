import numpy as np

RT_MAX_DEPTH = 5

def get_rt_max_depth():
    global RT_MAX_DEPTH
    return RT_MAX_DEPTH

def set_rt_max_depth(max_depth):
    global RT_MAX_DEPTH
    RT_MAX_DEPTH = max_depth

NO_LOSS = np.array([1,1,1],dtype=np.float32)

__all__=('get_rt_max_depth','set_rt_max_depth')