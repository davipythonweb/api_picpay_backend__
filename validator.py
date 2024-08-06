from django.core.exceptions import ValidationError

def validate_cpf(value):
    # remover pontuação
    cpf = ''.join([char for char in value if char.isdigit()])

    # verificar se tem 11 digitos
    if len(cpf) != 11:
        raise ValidationError('CPF invalido')
    
    # verificar se todos os digitos sao iguais
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF invalido')
    
    # funçao para calcular os digitos verificadores
    def calcular_digito(cpf, multiplicadores):
        soma = sum(
            int(cpf[i]) * multiplicadores[i]
            for i in range(len(multiplicadores))
        )
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    # multiplicadores para o primeiro digito verificador
    multiplicadores_primeiro = list(range(10, 1, -1))
    primeiro_digito = calcular_digito(cpf, multiplicadores_primeiro)

    # multiplicadores para o segundo digito verificador
    multiplicadores_segundo = list(range(11, 1, -1))
    segundo_digito = calcular_digito(cpf, multiplicadores_segundo)

    # verificar se os digitos calculados sao iguais aos informados
    if not (cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito)):
        raise ValidationError('CPF invalido')