from phonenumber_validator.number import Number
from document_validator.document import Document

number = Number.create_number(99985296891)
number2 = Number.create_number(9985296891)

print(number, number2)
