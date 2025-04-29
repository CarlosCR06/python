paises = ["España", "Rusia", "Japón", "Australia"]
estaturas = np.random.randint(140, 211, (4, 10))

print(f"{'PAÍS':<10} {'MED':<4} {'MIN':<4} {'MAX':<4}")
for i, pais in enumerate(paises):
    media = int(estaturas[i].mean())
    minimo = estaturas[i].min()
    maximo = estaturas[i].max()
    print(f"{pais:<10} {media:<4} {minimo:<4} {maximo:<4}")
