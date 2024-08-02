import pandas as pd
import FuncoesDados
from Main import ColunasUsadas, materia

# Gemini Carregar os dados
dados = FuncoesDados.MicrodadosENEM.ler_microdados("MICRODADOS_ENEM_2020.csv",
                                                            ColunasUsadas,
                                                            materia)

# Agrupar os dados por cor do caderno e calcular a média da nota
dados_agrupados = dados.groupby("TX_COR")["NU_NOTA_MT"].mean()
print(dados_agrupados)
