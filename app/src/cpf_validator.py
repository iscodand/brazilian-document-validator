from validate_docbr import CPF


class CPFValidator():
    def __init__(self, document):
        if self.validate(document):
            self.cpf = document
        else:
            raise ValueError('CPF Inválido!')

    def __str__(self):
        return self.format()

    def validate(self, document):
        validator = CPF()
        return validator.validate(document)

    def format(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)
