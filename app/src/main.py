from phonenumber_validator.number import Number
from document_validator.document import Document
from datetime_validator.datetime_br import DateTimeBR


register = DateTimeBR()

print(register.register_moment)
print(register.register_month())
print(register.register_weekday())
print(register)
print(register.register_time())
