# AUTOR: Carlos Castro

import numpy as np

# Lista de países
paises = ["España", "Rusia", "Japón", "Australia"]

# Generar estaturas aleatorias (entre 140 y 210 cm) para 10 personas por país
estaturas = np.random.randint(140, 211, (4, 10))

# Mostrar encabezado de tabla
print(f"{'PAÍS':<12} {'MEDIA':<6} {'MÍNIMO':<8} {'MÁXIMO':<8}")

# Calcular y mostrar media, mínimo y máximo por país
for i, pais in enumerate(paises):
    media = int(estaturas[i].mean())
    minimo = estaturas[i].min()
    maximo = estaturas[i].max()
    print(f"{pais:<12} {media:<6} {minimo:<8} {maximo:<8}")
