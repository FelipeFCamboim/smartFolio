import pandas as pd
import numpy as np

"""
Esse módulo executa cálculos financeiros
"""

def log_return(price_series: pd.DataFrame) -> pd.DataFrame:
    '''
    This function calculate log-returns of stock DataFrame and with "np.log()"
    and return on pandas.Series.
    
    Arguments:
        price_series: a pd.DataFrame dtype float64
    '''
    log_returns = np.log(price_series).diff().fillna(0)
    log_returns.reset_index(inplace = True)
    return log_returns

def generate_wallets(returns, num_portfolios = 50000, risk_free = 0.000358):
    # vetores de dados
    portfolio_weights = []
    portfolio_exp_returns = []
    portfolio_vol = []
    portfolio_sharpe = []

    # média dos retornos
    returns.replace([np.inf, -np.inf], 0, inplace=True)
    mean_returns = returns.mean()

    # matriz de covariância 
    covariance = np.cov(returns[1:].T)

    for i in range(num_portfolios):
        # gerando pesos aleatórios
        k = np.random.rand(len(returns.columns))
        w = k / sum (k)

        # retorno
        R = np.dot(mean_returns, w)

        # risco
        vol = np.sqrt(np.dot(w.T, np.dot(covariance, w)))

        # sharpe ratio
        sharpe = (R - risk_free)/vol

        portfolio_weights.append(w)
        portfolio_exp_returns.append(R)
        portfolio_vol.append(vol)
        portfolio_sharpe.append(sharpe)

    wallets = {'weights': portfolio_weights,
              'returns': portfolio_exp_returns,
              'vol':portfolio_vol,
              'sharpe': portfolio_sharpe}

    return wallets