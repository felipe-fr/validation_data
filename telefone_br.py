import re

class TelefoneBr:
    def __init__(self,telefone):
        if self.valida(telefone):
            self.telefone = telefone
        else:
            raise ValueError("NÚMERO INCORRETO")

    def __str__(self):
        return self.formata()
    
    def valida(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return False
    
    def formata(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,self.telefone)[0]
        if resposta[0]:
            return f"+{resposta[0]}({resposta[1]}){resposta[2]}-{resposta[3]}"
        else:
            return f"+55({resposta[1]}){resposta[2]}-{resposta[3]}"
