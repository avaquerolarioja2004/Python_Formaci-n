from calculos_arquitectonicos import area_circulo, area_rectangulo, volumen_cilindro


def planificar_proyecto():
    ar = area_rectangulo(10, 20)
    vc = volumen_cilindro(5, 10)
    ac = area_circulo(10)
    return ar, vc, ac


print(planificar_proyecto())
