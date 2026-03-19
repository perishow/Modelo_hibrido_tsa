import pandas as pd

# file_path = "../datasets/2025/INMET_CO_DF_A001_BRASILIA_01-01-2025_A_30-11-2025.CSV"
file_path_2 = "../datasets/2025/INMET_CO_MT_A916_QUERENCIA_01-01-2025_A_30-11-2025.CSV"
dataset = pd.read_csv(file_path_2, encoding="latin1", sep=";", skiprows=8, decimal=",")

correlacoes = {}

for feature in dataset.columns:
    if feature != "Data" and feature != "Hora UTC" and feature != "HORÁRIO (mm)":
        # Correção feita aqui: Adicionado o ")" no final da string da coluna
        pearson = dataset[feature].corr(dataset["RADIACAO GLOBAL (Kj/m²)"])  # type: ignore

        correlacoes[feature] = pearson

# Ordena o dicionario
correlacoes_ordenadas = sorted(correlacoes.items(), key=lambda x: x[1], reverse=True)

for feature, pearson in correlacoes_ordenadas:
    print(f"{pearson:.4} : {feature}")
