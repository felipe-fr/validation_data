from validate_docbr import CPF
class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO!!")

    def __str__(self):
        return self.formata_cpf()

    def valida_cpf(self,documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("QUANTIDADE DE DÍGITOS INVÁLIDA")    

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)