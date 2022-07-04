from document import Document


cpf = '05613136360'

cpf_object = Document.create_document(cpf)

print(cpf_object)

cnpj = '05555382000133'

cnpj_object = Document.create_document(cnpj)

print(cnpj_object)
