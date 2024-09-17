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
    iterations = 10000
    for ecl in ["low", "med", "quart", "high"]:
        print(ecl)
        generate_ecl_set(iterations//4, ecl)

    array = [[1,0,1],[0,0,0],[1,1,0]] 
    transform = fft.fft2(array)
    print(transform)


if __name__ == "__main__":
    main()