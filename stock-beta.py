import yfinance as yf
import statsmodels.api as sm
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import numpy as np


def obter_dados(ativos, dias):
    """
    Obtém os dados históricos de fechamento ajustado para os ativos especificados.
    
    Parâmetros:
    ativos (list): Lista de símbolos dos ativos a serem analisados.
    dias (int): Número de dias anteriores à data atual para buscar os dados.
    
    Retorno:
    DataFrame: Tabela com os dados de fechamento ajustado dos ativos.
    """


    data_fim = datetime.now()
    data_inicio = data_fim - timedelta(days=dias)
    dados_cotacoes = yf.download(tickers=ativos, start=data_inicio, end=data_fim)['Adj Close']

    return dados_cotacoes.pct_change().dropna()


def regressao_linear(X, Y):
    """
    Executa a regressão linear entre dois conjuntos de dados.
    
    Parâmetros:
    X (Series): Série de retornos do IBOV.
    Y (Series): Série de retornos do ativo.
    
    Retorno:
    Tuple: Contém o intercepto, coeficiente beta e o modelo ajustado.
    """


    X = sm.add_constant(X)
    modelo = sm.OLS(Y, X).fit()
    beta = modelo.params.iloc[1]
    intercept = modelo.params.iloc[0]

    return intercept, beta, modelo


def plotar_regressao(X, Y, intercept, beta, ativo):
    """
    Plota os dados e a linha de regressão linear.
    
    Parâmetros:
    X (Series): Retorno do IBOV.
    Y (Series): Retorno do ativo.
    intercept (float): Intercepto da linha de regressão.
    beta (float): Coeficiente beta.
    ativo (str): Nome do ativo.
    """


    plt.scatter(X, Y, color='blue', label='Dados observados')
    
    X_vals = np.linspace(min(X), max(X), 100)
    Y_vals = intercept + beta * X_vals
    plt.plot(X_vals, Y_vals, color='red', label='Linha de Regressão')

    plt.title(f'Regressão Linear: {ativo} vs IBOV')
    plt.xlabel('Retorno do IBOV')
    plt.ylabel(f'Retorno da {ativo}')
    plt.legend()
    plt.show()


def analisar_ativos(ativos, dias):
    """
    Realiza a análise de regressão linear para uma lista de ativos em relação ao IBOV.
    
    Parâmetros:
    ativos (list): Lista de símbolos dos ativos a serem analisados.
    dias (int): Número de dias de dados a serem analisados.
    """


    retornos_diarios = obter_dados(ativos, dias)
    for ativo in ativos[:-1]:  # Excluímos o índice IBOV (^BVSP)
        X = retornos_diarios['^BVSP']
        Y = retornos_diarios[ativo]

        intercept, beta, modelo = regressao_linear(X, Y)
        
        # Exibindo resultados
        print(f"Ativo: {ativo}")
        print(f"Beta: {beta}")
        print(f"R-quadrado: {modelo.rsquared}")
        print('--------------------------')
        print(modelo.summary())
        print('--------------------------\n')
        
        # Plotando gráfico
        plotar_regressao(X, Y, intercept, beta, ativo)
        print('--' * 50)
        print('\n')


if __name__ == "__main__":
    ativos = ["WEGE3.SA", "PETR4.SA", "VALE3.SA", '^BVSP'] # lista de ativos
    dias = 1095  # Três anos
    analisar_ativos(ativos, dias)
