import gen_qr as generator
import uuid
from qrcodegen import *
import random, string
from scipy import fft

def generate_ecl_set(set_size, ecl):
    for i in range(set_size):
        message = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        # message = str(uuid.uuid1())[:15] # random hexcode as message (for now)
        qr = generator.generate_QR(message, ecl, -1, 29)
        generator.file_output(qr, message, ecl)

def main():
    iterations = 1000 # currently at 1000 for testing
    
    f = open("codes.csv", "w") # initialize new file
    f.write(f'message, ecl, code, dft \n') # write col headers
    
    for ecl in ["low", "med", "quart", "high"]:
        print(f'create {ecl} ecl codes...')
        generate_ecl_set(iterations//4, ecl)
        
        
    # testing transform
    
    # array = [[1,0,1],[0,0,0],[1,1,0]] 
    # transform = fft.fft2(array)
    # print(transform)


if __name__ == "__main__":
    main()