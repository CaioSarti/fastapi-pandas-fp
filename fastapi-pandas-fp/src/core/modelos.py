from typing import List
import pandas as pd
from .metrics import analisar

class DataLoader:
    def __init__(self, path: str):
        self.path = path

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)
        required = {"produto", "preco", "qtd"}
        if not required.issubset(set(df.columns)):
            raise ValueError(f"CSV deve conter colunas: {required}")
        return df

class StatsService:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        if "receita" not in self.df.columns:
            self.df["receita"] = self.df["preco"] * self.df["qtd"]

    def qtd_total(self) -> int:
        return int(self.df["qtd"].sum())

    def receita_total(self) -> float:
        return float(self.df["receita"].sum())

    def preco_medio(self) -> float:
        return float(self.df["preco"].mean())

    def desafio_fp(self, coluna: str, limite: int):
        lista = list(map(int, self.df[coluna].tolist()))
        return analisar(lista, limite)
