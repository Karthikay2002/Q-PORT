import numpy as np
import matplotlib.pyplot as plt
from portfolio_core import generate_efficient_frontier, plot_efficient_frontier
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

def compare_sharpe_ratios(quantum_return, quantum_risk, results, risk_free_rate=0.02):
    """Calculate and compare Sharpe Ratios for quantum and classical portfolios."""
    quantum_sharpe_ratio = (quantum_return - risk_free_rate) / quantum_risk
    max_classical_sharpe_ratio = np.max(results[2, :])
    print(f"Quantum Portfolio Sharpe Ratio: {quantum_sharpe_ratio:.4f}")
    print(f"Max Classical Portfolio Sharpe Ratio: {max_classical_sharpe_ratio:.4f}")

def calculate_sharpe_ratio(portfolio_return, portfolio_risk, risk_free_rate):
    """Calculate Sharpe ratio for a given portfolio."""
    return (portfolio_return - risk_free_rate) / portfolio_risk

def main(mean_vector, covariance_matrix, portfolio_return, portfolio_risk, risk_free_rate=0.02):
    """Run the analysis and visualization for quantum and classical portfolios."""
    # Step 1: Generate Efficient Frontier
    mean_returns = np.array(mean_vector)
    cov_matrix = np.array(covariance_matrix)
    results = generate_efficient_frontier(mean_returns, cov_matrix, risk_free_rate=risk_free_rate)

    # Step 2: Plot Efficient Frontier and Quantum Portfolio
    plot_efficient_frontier(results, portfolio_return, portfolio_risk)

    # Step 3: Sharpe Ratio Comparison
    compare_sharpe_ratios(portfolio_return, portfolio_risk, results, risk_free_rate)

# If running this script directly, replace the placeholders with actual values from your main script.
if __name__ == "__main__":
    # Example placeholder values - replace with actual values when calling from qc_portfolio_main
    example_mean_vector = [0.001, 0.002, 0.0015, 0.003, 0.0025]  # Replace with actual mean vector from data
    example_covariance_matrix = np.eye(5) * 0.001  # Replace with actual covariance matrix
    example_portfolio_return = 0.01  # Replace with quantum portfolio's calculated return
    example_portfolio_risk = 0.02  # Replace with quantum portfolio's calculated risk
    risk_free_rate = 0.01

    # Run analysis with example values (replace with actual values from main script)
    main(example_mean_vector, example_covariance_matrix, example_portfolio_return, example_portfolio_risk, risk_free_rate)
