# Atributos do modelo

Atributos_Categoricos = [
    'Q074',
    "J01802",
    "J023",
    "J024",
    "Q03001",
    "L01701",
    "L01702",
    "Q092",
    "Q09201",
    "Q09202",
    "R026",
    'R028',
    "R029",
    "V0001",
    "A005010",
    "A005012",
    "A01403",
    "A01501",
    "A016010",
    "A01901",
    "D001",
    "F007011",
    "VDE001",
    "VDE002",
    "VDE014",
    "M01001",
    "P02101",
    "P051",
    "P034",
    "P039",
    "P044",
    "P04405",
    "P04406",
    "P04801",
    "P02102",
    "P02401",
    "P03201",
    "M011031",
    "M009",
    "M011011",
    "M011051",
    "M011071",
    "A02201",
    "C009",
    "C006",
    "J01101",
    "N00101",
    "N012",
    "N016",
    "N017",
    "N018",
    "A00601",
    "A009010",
    "VDD004A",
    "P050",
    "P052",
    "P05401",
    "P05404",
    "P05407",
    "P05410",
    "P05413",
    "P05416",
    "P05419",
    "P067",
    "P06701",
    "P068",
    "P04501",
    "P04502",
    "P02601",
    "P027",
]

Atributos_Numericos = [
    "VDF003", # Renda_per_capita
    "P03701", # Pratica_Exercicio horas
    "P03702", # Pratica_Exercicio min
    "P00104", # Peso, transformar em IMC
    "P00404", # Altura, transformar em IMC
    "J012", # N° consultas no medico
    "P05402", # N° de cigarros dia
    "P05403", # N° de cigarros semana
    "P05405", # N° de cigarros dia
    "P05406", # N° de cigarros semana
    "P05408", # N° de cigarros dia
    "P05409", # N° de cigarros semana
    "P05411", # N° de cigarros dia
    "P05412", # N° de cigarros semana
    "P05414", # N° de cigarros dia
    "P05415", # N° de cigarros semana
    "P05417", # N° de cigarros dia
    "P05418", # N° de cigarros semana
    "P05421", # N° de cigarros dia
    "P05422", # N° de cigarros semana
    "P035", # Exercicio dias
    "P03904", # Exercicio dias
    "P03905", # Exercicio horas
    "P03906", # Exercicio min
    "P00901", # Alimentação dias
    "P01101", # Alimentação dias
    "P013", # Alimentação dias
    "P015", # Alimentação dias
    "P02001", # Alimentação dias
    "P01601", # Alimentação dias
    "P018", # Alimentação dias
    "P019", # Alimentação dias
    "P02002", # Alimentação dias
    "P023", # Alimentação dias
    "P02501", # Alimentação dias
    "P02602", # Alimentação dias
    "P02801", # Alimentação dias
    "P029", # Alimentação dias
    "P03202", # Alimentação dias
    "A02305", # N° gatos
    "A02306", # N° cachorros
    "A02307", # N° aves
    "C008" # Idade, Não retirar outliers - Não existe
]

def outlier_count(df):
    iqr = df.quantile(0.75) - df.quantile(0.25)

    iqr_outliers_Inf = (df < df.quantile(0.25) - 1.5 * iqr).sum() 
    iqr_outliers_Sup = (df > df.quantile(0.75) + 1.5 * iqr).sum()

    quantidade_outliers = ((df<iqr_outliers_Inf) | (df>iqr_outliers_Sup)).sum()

    print(f"Quantidade de outliers: {quantidade_outliers}")
