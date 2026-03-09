from functools import reduce

funcionarios = [
    ("Ana Silva",    "Engenheira de Software",  8500.00),
    ("Bruno Costa",  "Analista Junior",          2800.00),
    ("Carla Mendes", "Gerente de Produto",      11200.00),
    ("Daniel Rocha", "Designer UX",              4300.00),
    ("Eduarda Lima", "Estagiaria",               1500.00),
    ("Fabio Souza",  "DevOps Engineer",          7000.00),
]

limite = 3000.00

# filter: Filtrar aqueles que ganha acima do limite
elegíveis = list(filter(lambda f: f[2] > limite, funcionarios))

# map: adiciona o valor do bonus em cada tupla
com_bonus = list(map(lambda f: (f[0], f[1], f[2], f[2] * 0.10), elegíveis))

# reduce: soma todos os bonus
total = reduce(lambda acc, f: acc + f[3], com_bonus, 0.0)

for nome, cargo, salario, bonus in com_bonus:
    print(f"{nome} | Salario: R$ {salario:.2f} | Bonus: R$ {bonus:.2f}")

print(f"\nTotal gasto com bonus: R$ {total:.2f}")
print(f"Funcionarios que recebem bonus: {len(com_bonus)}")
