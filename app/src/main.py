from phonenumber_validator.number import Number
from document_validator.document import Document
from datetime_validator.datetime_br import DateTimeBR


register = DateTimeBR()

print(register.register_moment)
print(DateTimeBR.register_month())
print(DateTimeBR.register_weekday())
