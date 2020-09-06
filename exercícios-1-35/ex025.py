nom = str(input('Digite o seu nome completo:')).strip()
print('Seu nome tem Silva?{}'.format('Silva' in nom.title()))



nome = str(input('Digite o seu nome completo:')).strip()
nn = nome.upper()
print('O seu nome ({})tem Silva? {}'.format(nome,'SILVA'in nn))