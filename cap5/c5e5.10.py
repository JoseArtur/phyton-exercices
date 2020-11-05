pts=0
questao=1
while questao<=3:
  resposta=input(f"Resposta da questão {questao}: ")
  resposta=resposta.lower()
  if questao == 1 and resposta == "b":
    pts+=1
  if questao == 2 and resposta == "a":
    pts+=1
  if questao == 3 and resposta == "d":
    pts+=1
  questao+=1
print(f"O aluno fez {pts} ponto(s)")