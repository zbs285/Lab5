from PIL import Image
import numpy as np

def person_detected(inamge1_file, image2_file, t1):
    buffer1 = np.asarray(inamge1_file)
    buffer2 = np.asarray(inamge2_file)
    buffer3 = buffer1 - buffer2
    a = buffer3.abs()
    sum = a.sum()
    if sum > t1:
        return True
    else:
        return False
    
