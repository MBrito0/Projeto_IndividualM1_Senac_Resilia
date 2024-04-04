candidatos = [
  ['candidato 1', 'e5_t10_p8_s8'],
  ['candidato 2', 'e10_t7_p7_s8'],
  ['candidato 3', 'e8_t5_p4_s9'],
  ['candidato 4', 'e2_t2_p2_s1'],
  ['candidato 5', 'e10_t10_p8_s9'],
]

critérios = []
for i, etapa in enumerate(['entrevista', 'teste teórico', 'teste prático', 'soft skills']):
    critério = int(input(f"Informe a nota mínima para a etapa {etapa}: "))
    critérios.append(critério)

print("Candidatos que atendem aos critérios:")
for candidato in candidatos:
    notas_candidato = [int(nota[1:]) for nota in candidato[1].split('_')]
    if all(nota >= crit for nota, crit in zip(notas_candidato, critérios)):
        print(candidato[0])
