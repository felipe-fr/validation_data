import requests

class Cep:
    def __init__(self,cep):
        cep = str(cep)
        if self.valida(cep):
            self.cep = cep
        else:
            raise ValueError("CEP INVÁLIDO")
    
    def __str__(self):
        return self.formata()

    def formata(self):
        return f"{self.cep[0:5]}-{self.cep[5:]}"

    def valida(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def retorna_endereco(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        response = requests.get(url).json()
        if len(response) == 1:
            raise ValueError("CEP NÃO POSSUI ENDEREÇO")
        else:
            endereco = {
                "bairro": response["bairro"],
                "localidade": response["localidade"],
                "uf": response["uf"],
            }
            return endereco

    
