from get_horoscopes import get_horoscope
from create_images import generate_images

import time


if __name__ == "__main__":
    t_0 = time.time()
    #get_horoscope()
    generate_images()
    
    print("\nTime elapsed: ", round(time.time() - t_0, 2), "seconds\n")