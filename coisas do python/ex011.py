alt = float(input('Insira a altura da parede: '))
larg = float(input('Insira a largura da parede: '))
area = larg * alt
tinta = area / 2
print(f'A dimensão da sua parede é de {alt}x{larg}, a área total da parede é de {area:.2f} m² e, portanto, serão precisos {tinta:.2f} litros de tinta para pintá-la.')