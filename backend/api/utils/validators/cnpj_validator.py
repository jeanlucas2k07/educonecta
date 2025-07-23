import requests

def __VerificarValidade(cnpj:str):
    response = requests.get(f'https://publica.cnpj.ws/cnpj/{cnpj}')

    if response.status_code == 200:
        data = response.json()
        inscricoes = data.get('estabelecimento', {}).get('inscricoes_estaduais', [])
        for inscricao in inscricoes:
            if inscricao.get('ativo') is True:
                return True
        return False
    return False

def VerificaCNPJ(cnpj: str):
    separadores = ('.', '/', '-')

    for separador in separadores:
        if separador in cnpj:
            cnpj = cnpj.replace(separador, '')

    cnpj_base_calculo = {
        'cnpj_base': [int(cnpj[i]) for i in range(12)],
        'pesos_dv1': [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
        'pesos_dv2': [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    }

    cnpj_produtos = {
        'dv1': [cnpj_base_calculo['cnpj_base'][i]*cnpj_base_calculo['pesos_dv1'][i] for i in range(12)],
        'dv2': []
    }

    soma1 = 0

    for i in cnpj_produtos['dv1']:
        soma1+= i
    
    dv1 = 0 if soma1% 11 < 2 else 11-soma1%11

    cnpj_base_calculo['cnpj_base'].append(dv1)

    cnpj_produtos['dv2'] = [cnpj_base_calculo['cnpj_base'][i]*cnpj_base_calculo['pesos_dv2'][i] for i in range(13)]

    soma2 = 0

    for i in cnpj_produtos['dv2']:
        soma2+=i

    dv2 = 0 if soma2%11 < 2 else 11-soma2%11

    if cnpj[12:] == str(dv1)+str(dv2):
        return __VerificarValidade(cnpj)
    
    else:
        return False