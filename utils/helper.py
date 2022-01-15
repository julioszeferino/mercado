def formata_float_str_moeda(valor: float) -> str:
    '''
    Funcao que formata uma variavel float para o formato moeda.

    :params valor: o valor a ser ajustado.
    :return: retorna o valor no formato de moeda brasileiro.
    '''
    return f'R$ {valor:,.2f}'

