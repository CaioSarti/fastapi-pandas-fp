import os, json, random
from pathlib import Path
import pandas as pd
from core.modelos import DataLoader, StatsService

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
CSV_PATH = DATA_DIR / "dados.csv"
STATS_PATH = ROOT / "stats.json"

def ensure_csv(path: Path):
    if path.exists():
        print(f"Encontrado {path}")
        return
    produtos = []
    for i in range(1, 101):
        produto = f"produto_{i}"
        preco = round(random.uniform(1.0, 100.0), 2)
        qtd = random.randint(1, 20)
        produtos.append({"produto": produto, "preco": preco, "qtd": qtd})
    pd.DataFrame(produtos).to_csv(path, index=False)

def main():
    ensure_csv(CSV_PATH)
    loader = DataLoader(str(CSV_PATH))
    df = loader.load()
    df["receita"] = df["preco"] * df["qtd"]
    service = StatsService(df)
    stats = {
        "qtd_total": service.qtd_total(),
        "receita_total": service.receita_total(),
        "preco_medio": service.preco_medio(),
        "desafio_fp": service.desafio_fp("qtd", 2),
    }
    with open(STATS_PATH, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"Gerado {STATS_PATH}")

if __name__ == "__main__":
    main()
