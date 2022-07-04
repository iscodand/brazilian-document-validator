from cnpj_validator import CNPJValidator
from cpf_validator import CPFValidator


class Document:

    @staticmethod
    def create_document(document):
        document = str(document)

        if len(document) == 11:
            return CPFValidator(document)
        elif len(document) == 14:
            return CNPJValidator(document)
        else:
            raise ValueError('Documento Inválido!')
