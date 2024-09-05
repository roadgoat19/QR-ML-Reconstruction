import gen_qr as generator
import uuid
from qrcodegen import *

def generate_ecl_set(set_size, ecl):
    for i in range(set_size):
        message = str(uuid.uuid1())[:15] # random hexcode as message (for now)
        qr = generator.generate_QR(message, ecl, -1, 29)
        generator.file_output(qr, message, ecl)
def main():
    iterations = 1000
    for ecl in ["low", "med", "quart", "high"]:
        print(ecl)
        generate_ecl_set(iterations//4, ecl)


if __name__ == "__main__":
    main()