import re

def normalize_phone(phone_number):
    phone_numer = ""
    patern = r"[^\+\d]"
    phone_numer = re.sub(patern, phone_number)
    phone_numer = phone_numer.split("0", maxsplit=1)
    phone_numer[0] = "+380"
    return phone_numer

if __name__ == "__main__":
    normalize_phone()

    