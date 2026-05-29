# Atributos do modelo

Atributos_Categoricos = [
    "A001", "A002010", "A005010", "A005012", "A009010",
    "A01001", "A011", "A01403", "A01501", "A016010",  "A02201",
    "C006", "C009", "D001", "E001", "E002", "E003", "E011", "E022",
    "I00102",
    "J01802", "J023", "J024", "L01701", "M001", "M009", "M01001", "M011011",
    "M011031", "M011051", "M011071", "N012", "N016", "N017", "N018", "P02101",
    "P02102", "P02401", "P02601", "P027", "P034", "P038", "P039",  "P044", "P04401", "P050", "P051", "P052",
    "P068", "Q074",  "R025", "R026", "R028", "R029",
    "V0001", "VDD004A", "VDE001", "VDE002", "VDE014","VDF004"
]

Atributos_Numericos = [
    "A02305", "A02306", "A02307", "C008", "P00104", "P00404", "P006", "P00901",
    "P01001", "P01101", "P013", "P015", "P01601", "P018", "P019", "P02001",
    "P02002", "P023", "P02501", "P02602", "P02801", "P035", "P03904", "P04001",
    'C001'
]

import pandas as pd


def filtrar_e_dropar_coluna(df, lista_colunas):
    """
    Mantém apenas registros que possuem o valor mais frequente
    (incluindo nulos) e remove a coluna após o filtro.
    """
    # Criamos uma cópia para evitar o Warning de SettingWithCopy
    df_result = df.copy()

    for col in lista_colunas:
        if col in df_result.columns:
            # 1. Encontrar o valor mais frequente (dropna=False inclui nulos)
            valor_mais_frequente = df_result[col].value_counts(dropna=False).idxmax()

            # 2. Filtrar o DataFrame mantendo apenas as linhas com esse valor
            # Tratamento especial para NaN (já que np.nan != np.nan)
            if pd.isna(valor_mais_frequente):
                df_result = df_result[df_result[col].isna()]
            else:
                df_result = df_result[df_result[col] == valor_mais_frequente]

            # 3. Dropar a coluna
            df_result = df_result.drop(columns=[col])

    return df_result

# Exemplo de uso:
# df_final = filtrar_e_dropar_coluna(meu_dataframe, Atributos_Categoricos)

def remove_outliers_iqr(df: pd.DataFrame, columns: list = None, factor: float = 3.0) -> pd.DataFrame:
    """
    Remove outliers usando IQR com fator ajustado (padrão 3.0 DP) para distribuições desbalanceadas.

    Parâmetros:
    -----------
    df      : DataFrame original
    columns : lista de colunas para aplicar (default: todas numéricas)
    factor  : multiplicador do IQR (default 3.0, mais conservador para dist. assimétricas)

    Retorna:
    --------
    DataFrame sem outliers e relatório de remoção por coluna.
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()

    mask = pd.Series(True, index=df.index)
    report = []

    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - factor * IQR
        upper = Q3 + factor * IQR

        col_mask = df[col].between(lower, upper)
        outliers = (~col_mask).sum()

        report.append({
            "coluna": col,
            "Q1": round(Q1, 4),
            "Q3": round(Q3, 4),
            "IQR": round(IQR, 4),
            "limite_inferior": round(lower, 4),
            "limite_superior": round(upper, 4),
            "outliers_removidos": outliers,
            "pct_removido": round(outliers / len(df) * 100, 2)
        })

        mask &= col_mask

    df_clean = df[mask].reset_index(drop=True)

    print(pd.DataFrame(report).to_string(index=False))
    print(f"\nTotal removido: {(~mask).sum()} linhas ({round((~mask).sum() / len(df) * 100, 2)}%)")
    print(f"Shape: {df.shape} → {df_clean.shape}")

    return df_clean