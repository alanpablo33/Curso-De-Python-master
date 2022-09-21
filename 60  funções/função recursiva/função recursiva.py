def soma_ate_100(n):
    if n < 100:
        n += 1
        return soma_ate_100(n)
    else:
        return n

numero = 99

num_100 = soma_ate_100(numero)

print(num_100)

# função chama ela mesma