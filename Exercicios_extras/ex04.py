# ===================================================
# DESAFIO 4 – CONJUNTOS
# ---------------------------------------------------
# Dados dois conjuntos:
# A = {1,2,3,4,5}
# B = {4,5,6,7}
# Compute e imprima, em linhas separadas:
# - A ∪ B (união)
# - A ∩ B (interseção)
# - A - B (diferença)
# - B - A (diferença inversa)
# - A Δ B (diferença simétrica)
# ===================================================

conjuntoA = {1,2,3,4,5}
conjuntoB = {4,5,6,7}

uniao = conjuntoA.union(conjuntoB)

interseccao = conjuntoA.intersection(conjuntoB)

diferencaA = conjuntoA.difference(conjuntoB)

diferencaB = conjuntoB.difference(conjuntoA)

simetrico = conjuntoA.symmetric_difference(conjuntoB)

print(f"união = {uniao}\nintersecção = {interseccao}\ndiferença de A = {diferencaA}\ndiferença de B = {diferencaB}\ndiferença simétrica = {simetrico}")