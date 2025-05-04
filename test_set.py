import gen_qr as generator
import uuid
from qrcodegen import *
import random, string
from scipy import fft

def generate_ecl_set(set_size, ecl, qr_size):
    for i in range(set_size):
        mask = -1
        message = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(134))
        # message = str(uuid.uuid1())[:15] # random hexcode as message (for now)
        qr = generator.generate_QR(message, ecl, mask, qr_size)
        generator.file_output(qr, message, ecl)
        if i % 1000 == 0:
            print(i)

def main():
    iterations = 60000 
    
    f = open("big_codes_nomask.csv", "w") # initialize new file
    f.write(f'message,ecl,code,dft \n') # write col headers
    
    generate_ecl_set(iterations, 'low', 41)
        
        
    # testing transform
    
    # array = [[1,0,1],[0,0,0],[1,1,0]] 
    # transform = fft.fft2(array)
    # print(transform)


if __name__ == "__main__":
    main()