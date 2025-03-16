import carro, mota

m_carro = carro.Carro("Toyota", "Corola", "Gasolina", 4)
m_mota = mota.Mota("Yamaha", "YZF-R3", "Gasolina", 321)

# MOSTRAR INFORMAÇÃO DE CADA OBJECTO
print("Informação de carro:")
m_carro.mostrar_info()

print("\nInformação da mota:")
m_mota.mostrar_info()