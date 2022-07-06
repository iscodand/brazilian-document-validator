import re


class ResidentialPhoneNumber():
    def __init__(self, number):
        number = str(number)

        if self.validate(number):
            self.number = number
        else:
            raise ValueError("Formato Incorreto!")
    
    def __str__(self):
        return self.mask()

    def validate(self, number):
        pattern = r"[1-9]{2,3}?[1-9]{2}9[0-9]{4}[0-9]{4}"
        answer = re.findall(pattern, number)
        if answer:
            return True 
        else:
            return False
        
    def mask(self):
        return f"({self.number[:2]}) 9{self.number[3:7]}-{self.number[7:]}"

