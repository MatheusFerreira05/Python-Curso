catetoOposto = float(input('Qual é o valor do cateto oposto? '))
catetoAdjacente = float(input('Qual é o valor do cateto Adjacente? '))

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print('Para um triângulo retângulo onde os catetos valem {} e {} a hipotenusa é {:.2f}'.format(catetoOposto,catetoAdjacente,hipotenusa))