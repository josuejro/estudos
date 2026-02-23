from datetime import date

trabalhadores = {}

ano_atual = date.today().year

trabalhadores['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
trabalhadores['idade'] = ano_atual - nascimento
trabalhadores['ctps'] = int(input('CTPS: '))

if trabalhadores['ctps'] != 0:
    trabalhadores['ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhadores['salario'] = float(input('Salário: '))
    aposentadoria = trabalhadores['idade'] + (35 - (ano_atual - trabalhadores['ano_contratacao']))
    trabalhadores['aposentadoria'] = aposentadoria

print()
print(f"{' FICHA DO FUNCIONÁRIO ':=^40}") 

print(f"{'Nome:':<20} {trabalhadores['nome']}")
print(f"{'Idade:':<20} {trabalhadores['idade']} anos")
print(f"{'CTPS:':<20} {trabalhadores['ctps']}")

if trabalhadores['ctps'] != 0:
    print("-" * 40)
    print(f"{'Contratação:':<20} {trabalhadores['ano_contratacao']}")
    print(f"{'Salário:':<20} R$ {trabalhadores['salario']:.2f}")
    print(f"{'Se aposenta com:':<20} {trabalhadores['aposentadoria']} anos")
    
print("=" * 40)