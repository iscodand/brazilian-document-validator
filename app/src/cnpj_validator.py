from validate_docbr import CNPJ


class CNPJValidator():
    def __init__(self, document):
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValueError('CNPJ Inválido!')

    def __str__(self):
        return self.format()

    def validate(self, document):
        validator = CNPJ()
        return validator.validate(document)

    def format(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)
