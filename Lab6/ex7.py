import re


def verify_valid_cnp(cnp):
    regex = re.compile(r'^[1-9]'
                       r'\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])'#an+luna+zi
                       r'(0[1-9]|[1-4]\d|5[0-2]|99)'#judet
                       r'(00[1-9]|0[1-9]\d|[1-9]\d\d)'#seria numerica
                       r'\d$')#nu am verificare pentru cifra de control
    if regex.match(cnp):
        return True
    return False

if __name__ == '__main__':
    print(verify_valid_cnp("5010229046239"))

