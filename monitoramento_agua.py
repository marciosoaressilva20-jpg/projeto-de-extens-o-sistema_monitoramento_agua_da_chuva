print("=== sistema de monitoramento de água da chuva ===")

# Entrada de dados
area_telhado= float (input ("informe o tamanho do telhado(m²):"))
chuva_mm= float (input ("informe a quantidade de chuva(mm):"))

#cálculo do volume captado(1 mm = 1 litro/m²)
litros_captados=area_telhado*chuva_mm

#estimativa de economia(R$ 10 por 1000 litros)
economia=(litros_captados/1000)* 10

#saida de resultados
print(f"você poderia captar aproximadamente  {litros_captados:.2f}litros de água")
print(f"economia estimada: R${economia:.2f}")
print("com essa água, seria possivel lavar calçadas, regar plantas ou usar em descargas!")
