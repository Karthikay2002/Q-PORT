import numpy as np
import matplotlib.pyplot as plt
def generate_efficient_frontier(mean_returns, cov_matrix, num_portfolios=10000, risk_free_rate=0.02):
    """Generate the efficient frontier for a set of portfolios."""
    results = np.zeros((3, num_portfolios))
    for i in range(num_portfolios):
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        portfolio_return = np.sum(weights * mean_returns)
        portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk
        results[0, i] = portfolio_return
        results[1, i] = portfolio_risk
        results[2, i] = sharpe_ratio
    return results


def plot_efficient_frontier(results, quantum_return, quantum_risk):
    """Plot the efficient frontier with quantum portfolio performance."""
    plt.figure(figsize=(10, 6))
    plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap='viridis', marker='o', s=10, alpha=0.3)
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Risk (Standard Deviation)')
    plt.ylabel('Return')
    plt.title('Efficient Frontier')
    plt.scatter(quantum_risk, quantum_return, color='red', marker='*', s=200, label='Quantum Portfolio')
    plt.legend()
    plt.show()


def calculate_sharpe_ratio(portfolio_return, portfolio_risk, risk_free_rate=0.01):
    """Calculate the Sharpe Ratio for a portfolio."""
    return (portfolio_return - risk_free_rate) / (portfolio_risk ** 0.5)


def visualize_portfolio(selected_assets, mean_vector, covariance_matrix, portfolio_return, portfolio_risk, stock_names):
    """Visualize portfolio contributions."""
    selected_returns = [mean_vector[i] for i in selected_assets]
    selected_risks = [sum(covariance_matrix[i][j] for j in selected_assets) for i in selected_assets]
    tickers = [stock_names[i] for i in selected_assets]
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(tickers))
    width = 0.35
    ax.bar(x - width/2, selected_returns, width, label='Return Contribution')
    ax.bar(x + width/2, selected_risks, width, label='Risk Contribution')
    ax.set_xlabel('Selected Assets')
    ax.set_ylabel('Contribution')
    ax.set_title('Contribution of Selected Assets in Quantum Portfolio')
    ax.set_xticks(x)
    ax.set_xticklabels(tickers, rotation=45, ha="right")
    ax.legend()
    plt.tight_layout()
    plt.show()
