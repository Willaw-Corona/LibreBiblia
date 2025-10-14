# Uhhh, ¿Como pongo un input aquí?

print("Hola, ¿Que versión de la Biblia quieres? (Reina Valera 1960 (A), La Biblia de las Américas (B), Nueva Versión Internacional (C), Biblia Dios Habla Hoy (D), La Biblia de Jerusalén (E), Biblia Latinoamericana (F), Biblia de las Américas 2020 (J), Nueva Traducción Viviente (K), La Santa Biblia (N), La Biblia Reina Valera Contemporánea (M), La Biblia del Oso (P) ) ")
version = input("Escribe la letra correspondiente a la versión: ").upper(A, B, C, D, E, F, J, K, N, M, P)
if version in ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'K', 'N', 'M', 'P']:
    print(f"Has seleccionado la versión {version}.")
else:
    print("Versión no válida. Por favor, selecciona una opción correcta.")