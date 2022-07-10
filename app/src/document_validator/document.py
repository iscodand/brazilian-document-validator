from document_validator.cnpj_validator import CNPJValidator
from document_validator.cpf_validator import CPFValidator


# Factory Pattern Project
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
