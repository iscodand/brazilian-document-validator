import requests


class CEPValidator():
    def __init__(self, cep):
        cep = str(cep)

        if self.validate(cep):
            self.cep = cep
        else:
            raise ValueError("Número de Dígitos Inválido!")

    def __str__(self):
        return self.mask()

    def validate(self, cep):
        if len(cep) == 8:
            return True
        return False

    def mask(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def information(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)

        cep = r.json()

        for values, keys in cep.items():
            information = str(print(f"{values.upper()} = {keys.upper()}"))

        return information



