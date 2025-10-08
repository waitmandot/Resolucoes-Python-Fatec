senha = "Fatec Rio Preto"
senha = "Teste 123"
senha = "54323"

for ch in senha:
    if not ch.isdigit():
        print("Invalid")
        break
else:
    print("Valid")

# Invalid, Invalid, Valid