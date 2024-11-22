import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from qc_portfolio_main import load_stock_data, initialize_data_simulator
from portfolio_core import generate_efficient_frontier, plot_efficient_frontier

def classical_portfolio_optimization(mean_returns, cov_matrix, risk_free_rate=0.01):
    """Classical Markowitz's Modern optimization to find the portfolio with the maximum Sharpe Ratio."""
    num_assets = len(mean_returns)
    
    # Objective function: minimize negative Sharpe Ratio
    def neg_sharpe_ratio(weights):
        weights = np.array(weights)
        portfolio_return = np.sum(weights * mean_returns)
        portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk
        return -sharpe_ratio
    
    # Constraints: weights sum to 1
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    # Bounds: no short-selling (weights between 0 and 1)
    bounds = tuple((0, 1) for _ in range(num_assets))
    # Initial guess: equally distributed weights
    initial_weights = num_assets * [1.0 / num_assets]
    
    # Optimize using SLSQP
    result = minimize(neg_sharpe_ratio, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
    
    if not result.success:
        raise ValueError("Optimization failed!")
    
    optimal_weights = result.x
    optimal_return = np.sum(optimal_weights * mean_returns)
    optimal_risk = np.sqrt(np.dot(optimal_weights.T, np.dot(cov_matrix, optimal_weights)))
    optimal_sharpe = (optimal_return - risk_free_rate) / optimal_risk
    
    return optimal_weights, optimal_return, optimal_risk, optimal_sharpe

def main():
    # Step 1: Load stock data
    csv_file_path = 'largeStockData_50.csv'
    num_stocks = 12
    data_list, stock_names = load_stock_data(csv_file_path, num_stocks)
    
    # Step 2: Initialize DataSimulator
    covariance_matrix, mean_vector = initialize_data_simulator(data_list, stock_names)
    
    # Step 3: Quantum Results
    quantum_selected_bitstring = '110001110000'  # Adjust based on quantum computation results
    quantum_selected_assets = [i for i, bit in enumerate(quantum_selected_bitstring) if bit == '1']
    quantum_return = sum(mean_vector[i] for i in quantum_selected_assets)
    quantum_risk = sum(covariance_matrix[i][j] for i in quantum_selected_assets for j in quantum_selected_assets)
    quantum_sharpe_ratio = (quantum_return - 0.01) / quantum_risk

    # Step 4: Classical Portfolio Optimization
    optimal_weights, classical_return, classical_risk, classical_sharpe_ratio = classical_portfolio_optimization(
        np.array(mean_vector), np.array(covariance_matrix)
    )
    classical_selected_assets = [stock_names[i] for i in range(len(optimal_weights)) if optimal_weights[i] > 0.05]

    # Step 5: Print Results
    print("\nQuantum Portfolio:")
    print(f"Selected Assets: {[stock_names[i] for i in quantum_selected_assets]}")
    print(f"Return: {quantum_return:.6f}, Risk: {quantum_risk:.6f}, Sharpe Ratio: {quantum_sharpe_ratio:.4f}")
    
    print("\nClassical Portfolio:")
    print(f"Selected Assets: {classical_selected_assets}")
    print(f"Return: {classical_return:.6f}, Risk: {classical_risk:.6f}, Sharpe Ratio: {classical_sharpe_ratio:.4f}")
    
    # Step 6: Visualizations
    # Plot efficient frontiers
    classical_results = plot_efficient_frontier(
        generate_efficient_frontier(np.array(mean_vector), np.array(covariance_matrix)),
        classical_return, classical_risk
    )
    plt.scatter(quantum_risk, quantum_return, color='red', marker='*', s=200, label='Quantum Portfolio')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
