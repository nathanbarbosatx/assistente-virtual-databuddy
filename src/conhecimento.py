from pathlib import Path


def carregar_conhecimento():
	caminho_base = Path(__file__).parent.parent / "data" / "base_conhecimento.md"
	return caminho_base.read_text(encoding="utf-8")
