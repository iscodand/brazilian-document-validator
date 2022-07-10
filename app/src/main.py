from phonenumber_validator.number import Number
from document_validator.document import Document
from datetime_validator.datetime_br import DateTimeBR
from cep_validator.cep_validator import CEPValidator
import requests

cep = CEPValidator(65700000)

print(cep.information())