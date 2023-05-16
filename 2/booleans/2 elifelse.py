has_money = True
has_job = True

if has_money:
    print("Então vou viajar")
elif has_job:
    print("Então pelo menos vou guardar dinheiro")
else:
    print("Só me resta chorar")

# Resultado -> "Então vou viajar"

has_money = False
has_job = True

if has_money:
    print("Então vou viajar")
elif has_job:
    print("Então pelo menos vou guardar dinheiro")
else:
    print("Só me resta chorar")

# Resultado -> "Então pelo menos vou guardar dinheiro"

has_money = False
has_job = False

if has_money:
    print("Então vou viajar")
elif has_job:
    print("Então pelo menos vou guardar dinheiro")
else:
    print("Só me resta chorar")

# Resultado -> "Só me Resta Chorar"