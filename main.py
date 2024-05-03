import matplotlib.pyplot  as plt
import pandas             as pd

# Criação do dataframe e obtenção de dados
df_planilha = pd.read_csv('planilha_tratada.csv')

apoio_ao_samu  = int(df_planilha["APOIO AO SAMU"].sum())
import_sexual  = int(df_planilha["IMPORTUNAÇÃO SEXUAL"].sum())
veiculo_recup  = int(df_planilha["VEÍCULOS RECUPERADOS"].sum())
roubo_furto    = int(df_planilha["ROUBO / FURTO"].sum())
furto_recup    = int(df_planilha["FURTO RECUPERADO"].sum())
invasao_dano   = int(df_planilha["INVASÃO / DANO AO PATRIMÔNIO PÚBLICO"].sum())
violen_domest  = int(df_planilha["VIOLÊNCIA DOMÉSTICA"].sum())
apoio_transeun = int(df_planilha["APOIO A TRANSEUNTE"].sum())
apoio_transito = int(df_planilha["APOIO AO TRÂNSITO / OPERAÇÕES E INTERVENÇÕES EM VIA PÚBLICA"].sum())
abord_denuncia = int(df_planilha["ABORDAGENS MEDIANTE DENÚNCIA"].sum())

total = apoio_ao_samu + import_sexual + veiculo_recup + roubo_furto + furto_recup + invasao_dano + violen_domest + apoio_transeun + apoio_transito + abord_denuncia

# Preparando pra criar o gráfico
porcentagens = [apoio_ao_samu,import_sexual,veiculo_recup,roubo_furto,furto_recup,invasao_dano,violen_domest,apoio_transeun,apoio_transito,abord_denuncia]
cabecalhos = list(df_planilha.columns[2:])

# Criação do gráfico
plt.figure(figsize=(11, 7))
plt.pie(porcentagens, labels=cabecalhos, autopct='%1.1f%%',pctdistance=1.1, labeldistance=1.187)
plt.savefig('graficoGeral.png')
plt.close()