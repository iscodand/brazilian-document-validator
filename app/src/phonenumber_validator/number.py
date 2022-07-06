from phonenumber_validator.residential_phone_number import ResidentialPhoneNumber
from phonenumber_validator.landline_number import LandlineNumber


class Number():

    @staticmethod
    def create_number(number):
        number = str(number)
        if len(number) == 11:
            return ResidentialPhoneNumber(number)
        if len(number) == 10:
            return LandlineNumber(number)
        else:
            raise ValueError("Número Inválido!")
        