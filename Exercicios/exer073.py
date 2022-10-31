times = ("palmeiras", "internacional", "flamengo", "fluminense", "corinthians", "atletico-pr", "atletico-mg",
    "america-mg", "fortaleza", "botafogo", "santos", "sao paulo", "bragantino", "goias", "coritiba", "ceara",
         "cuiaba", "atletico-go", "avai", "juventude",)
print(f'Ordem de classificação{times}')
print("-" *200)
print(f'Os 5 primeiro colocados sao{times[0:5]}')
print("-" *200)
print(f'Os ultimos 4 colocados sao{times[-4:]}')
print("-" *200)
print(f'Times em ordem alfabetica{sorted(times)}')
print("-" *200)
print(f'O america-mg esta na {times.index("america-mg") + 1} posicao')