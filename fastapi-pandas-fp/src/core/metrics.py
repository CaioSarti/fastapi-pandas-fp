from functools import reduce
from typing import List, Dict

def analisar(lista: List[int], limite: int) -> Dict[str, int]:
    filtrados = filter(lambda x: (x % 2 == 0) and (x > limite), lista)
    quadrados = map(lambda x: x * x, filtrados)
    def reducer(acc, v):
        soma, cont = acc
        return (soma + v, cont + 1)
    soma, cont = reduce(reducer, quadrados, (0, 0))
    media_inteira = soma // cont if cont != 0 else 0
    return {"soma_quadrados": soma, "contagem": cont, "media_inteira": media_inteira}
