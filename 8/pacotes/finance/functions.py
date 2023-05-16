from .constants import DEFAULT_TAX 
# Assim, quando quiser mudar o valor da taxa, tem um arquivo só para infos constantes.

def calcular_valor_taxado(valor):
    valor_taxado = valor * (1 + DEFAULT_TAX)
    return valor_taxado