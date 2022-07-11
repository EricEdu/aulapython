
tv1 = 0
tv2 = 0
tv3 = 0
tv4 = 0
pv1 = 0
pv2 = 0
pv3 = 0
pv4 = 0
repeticoes = 5
for contador in range(repeticoes): 
    voto = int(input('voto: '))

    if (voto == 1):
        print('voce votou no candidato 1')
        tv1 = tv1 + 1
    elif(voto == 2):
        print('voce votou no candidato 2')
        tv2 = tv2 + 1
    elif(voto == 3):
        print('voce votou nulo')
        tv3 = tv3 + 1
    elif(voto == 4):
        print('voce votou em branco')
        tv4 = tv4 + 1
print('voto finalizado')
pv1= (tv1/5) * 100
pv2= (tv2/5) * 100
pv3= (tv3/5) * 100
pv4= (tv4/5) * 100
print('Total votos candidato 1: ',tv1)
print('votos candidato 1 %: ',pv1)
print('Total votos candidato 2: ',tv2)
print('votos candidato 2 %: ',pv2)
print('Total votos candidato 3: ',tv3)
print('votos candidato 3 %: ',pv3)
print('Total votos candidato 4: ',tv4)
print('votos candidato 4 %: ',pv4)


