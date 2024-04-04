candidatos = [
  ['candidato 1', 'e5_t10_p8_s8'],
  ['candidato 2', 'e10_t7_p7_s8'],
  ['candidato 3', 'e8_t5_p4_s9'],
  ['candidato 4', 'e2_t2_p2_s1'],
  ['candidato 5', 'e10_t10_p8_s9'],
]

def procurar_candidatos (criterios) =
  for candidato in candidatos:
    if criterios["e"] in candidato[1] and \
        criterios["t"] in candidato[1] and \
        criterios["p"] in candidato[1] and \
        criterios["s"] in candidato[1]:
          return f"Candidato {candidato[0]} - {candidato[1]}"
  return "Candidato não encontrado"

criterios = {
    "e": "10",
    "t": "10",
    "p": "8",
    "s": "9"
}
print(procurar_candidato(criterios))
