import psycopg2
import random
from config import host, database, user, password

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

cur = conn.cursor()


def gerar_cpf():
    cpf = ""
    for i in range(11):
        cpf += str(random.randint(0, 9))
    return cpf

nomes = ["Ana Luiza", "Bianca Maria", "Carla Fernanda", "Diego Rafael", "Eduarda Beatriz", "Fernando Henrique",
         "Gabriel Antônio", "Henrique Eduardo", "Isabela Cristina", "João Lucas", "Karine Beatriz", "Laura Victoria",
         "Ana Julia", "Ana Luiza",
         "Natália Carolina", "Otávio Augusto", "Pedro Henrique", "Quirino José", "Rafaela Fernanda", "Sofia Isabel",
         "Thiago Felipe", "Úrsula Maria", "Valentina Raquel", "William Eduardo", "Xavier Matheus", "Yasmin Vitória",
         "Zoe Juliana", "Maria Gabriela",
         "Ricardo Henrique", "Renata Beatriz", "Paulo André", "Juliana Gabriela", "Amanda", "Bruno", "Cecília",
         "Daniel", "Elisa", "Felipe", "Giovanna", "Henrique", "Isadora", "José", "Karina", "Larissa", "Matheus",
         "Natália", "Otto", "Priscila", "Sara",
         "Quentin", "Roberto", "Samuel", "Thalita", "Ulisses", "Vanessa", "Wagner", "Ximena", "Yasmin", "Zélia",
         "Rafaela", "Ricardo", "Paula", "Júlio", "Ana", "Beatriz", "Carlos", "Diego", "Eduarda", "Fernanda", "Gabriel",
         "Hugo", "Isabel", "João",
         "Karine", "Lucas", "Mariana", "Nathalia", "Otávio", "Pedro", "Quirino", "Rafael", "Sofia", "Thiago", "Ursula",
         "Valentina", "William", "Xavier", "Yuri", "Zoe", "Ricardo", "Renata", "Paulo", "Juliana", "Victor", "Vinicius",
         "Gabriela"]

sobrenomes = ["Silva", "Souza", "Oliveira", "Pereira", "Costa", "Ferreira", "Rodrigues", "Almeida", "Lima", "Melo",
              "Garcia", "Martins", "Gomes", "Ribeiro", "Mendes", "Carvalho", "Coelho", "Moura", "Santos", "Nascimento",
              "Fernandes", "Marques", "Araújo", "Cardoso", "Barbosa", "Freitas", "Pena", "Cavalcante", "Ramos",
              "Basílio",
              "Pinto", "Vasco", "Gama", "Vasconcelos", "Cunha", "Amaral", "Correia", "Dantas", "Leite", "Leal",
              "Magalhães", "Guimarães"]

cidades = [
    "Londres", "Nova York", "Paris", "Tóquio", "Istambul", "Dubai", "Sydney", "Roma", "Barcelona", "Moscou",
    "Rio de Janeiro", "Berlim", "Cidade do Cabo", "Toronto", "Amsterdã", "Atenas", "Bangkok", "Pequim",
    "Budapeste", "Cairo", "Chicago", "Delhi", "Edimburgo", "Havana", "Hong Kong", "Jacarta", "Joanesburgo",
    "Carachi", "Cazã", "Copenhague", "Las Vegas", "Los Angeles", "Madri", "Manila", "México", "Miami", "Montevidéu",
    "Montreal", "Mumbai", "Nairóbi", "Paris", "Praga", "Reiquiavique", "Riad", "Roma", "São Francisco", "São Paulo",
    "Seul", "Singapura", "Sydney", "Tóquio", "Toronto", "Varsóvia", "Viena", "Xangai", "Zurique", "Buenos Aires",
    "Cidade do México", "Santiago", "Lima", "Bogotá", "Quito", "Panamá", "San Juan", "San José", "Santo Domingo",
    "Havana", "Kingston", "Montego Bay", "Liverpool", "Fortaleza", "Belo Horizonte", "Veneza", "Copenhague",
    "Florença", "Dublin", "Edimburgo", "Viena", "Buenos Aires", "Cusco", "São Francisco", "Los Angeles",
    "Las Vegas", "Miami", "Bangkok", "Sydney", "Melbourne", "Auckland", "Cairo", "Cidade do Cabo", "Johannesburg",
    "Toronto", "Montreal", "Vancouver", "Tóquio", "Quioto", "Osaka", "Seul", "Pequim", "Xangai", "Hong Kong",
    "Mumbai", "Delhi", "Moscou", "São Petersburgo"
]

profissoes = [
    "Médico", "Engenheiro civil", "Professor", "Advogado", "Enfermeiro", "Psicólogo", "Programador de computador",
    "Designer gráfico", "Contador", "Policial", "Arquiteto", "Farmacêutico", "Dentista", "Jornalista",
    "Administrador de empresas", "Veterinário", "Economista", "Consultor financeiro", "Analista de sistemas",
    "Assistente social", "Terapeuta ocupacional", "Chef de cozinha", "Piloto", "Astrônomo", "Cientista de dados",
    "Eletricista", "Bombeiro", "Escritor", "Personal trainer", "Psiquiatra", "Geólogo", "Fotógrafo", "Nutricionista",
    "Músico", "Ator/atriz", "Engenheiro de software", "Designer de moda", "Engenheiro ambiental",
    "Administrador de redes", "Engenheiro mecânico", "Fisioterapeuta", "Biólogo", "Desenvolvedor de jogos",
    "Analista de negócios", "Engenheiro eletricista", "Pedagogo", "Operador de máquinas", "Mecânico automotivo",
    "Consultor de vendas", "Estatístico", "Gerente de projetos", "Gestor de recursos humanos",
    "Engenheiro de produção", "Artista plástico", "Técnico em informática", "Engenheiro químico", "Bancário",
    "Gerente de marketing", "Analista de marketing", "Técnico em radiologia", "Psicopedagogo",
    "Motorista de ônibus", "Tradutor", "Engenheiro de telecomunicações", "Cirurgião-dentista", "Padeiro",
    "Engenheiro de petróleo", "Cabeleireiro", "Meteorologista", "Engenheiro de controle e automação",
    "Fonoaudiólogo", "Escultor", "Corretor de imóveis", "Esteticista", "Projetista de móveis", "Arqueólogo",
    "Pesquisador científico", "Analista de segurança da informação", "Engenheiro de dados", "Engenheiro de sistemas",
    "Engenheiro de rede", "Arquiteto de soluções", "Engenheiro de DevOps", "Engenheiro de IA (Inteligência Artificial)",
    "Engenheiro de cibersegurança", "Desenvolvedor de aplicativos móveis", "Engenheiro de realidade virtual",
    "Engenheiro de blockchain", "Engenheiro de IoT (Internet das Coisas)", "Especialista em nuvem (Cloud)",
    "Cientista de dados", "Engenheiro de automação", "Engenheiro de robótica", "Engenheiro de machine learning",
    "Engenheiro de sistemas embarcados", "Desenvolvedor de software", "Engenheiro de testes", "Engenheiro de Dados",
    "Engenheiro de computação"
]

num_habitantes = 100000

cur.execute("""
    CREATE TABLE habitantes (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50),
        sobrenome VARCHAR(50),
        cpf NUMERIC(11),
        cidade VARCHAR(50),
        profissao VARCHAR(50),
        idade INTEGER,
        salario NUMERIC(10,2)
    )
""")

for i in range(num_habitantes):
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    cpf = gerar_cpf()
    cidade = random.choice(cidades)
    profissao = random.choice(profissoes)
    idade = random.randint(18, 73)
    salario = round(random.uniform(1300.0, 25000.0), 2)

    cur.execute(
        "INSERT INTO habitantes (nome, sobrenome,cpf, cidade, profissao, idade, salario) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (nome, sobrenome, cpf, cidade, profissao, idade, salario))
    conn.commit()

cur.close()
conn.close()

print("Operação Criada com Sucesso!")
