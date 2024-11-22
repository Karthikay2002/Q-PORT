import paddle
import paddle_quantum
import pandas as pd
import numpy as np
from paddle_quantum.finance import DataSimulator, portfolio_optimization_hamiltonian
from qc_portfolio_utils import visualize_measurement_distribution, visualize_portfolio
from portfolio_core import generate_efficient_frontier, plot_efficient_frontier, calculate_sharpe_ratio
import os
import argparse

def load_stock_data(csv_file_path='largeStockData_50.csv', num_stocks=12):
    """Load stock data and select a subset for quantum portfolio optimization."""
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"File {csv_file_path} does not exist!")
    print("Loading stock data...")
    
    # Load the CSV data
    df = pd.read_csv(csv_file_path)
    
    # Extract the first 'num_stocks' ticker names from CSV headers
    ticker_names = df.columns[:num_stocks]  # Use the first 'num_stocks' columns as tickers
    selected_stocks = df.iloc[:, :num_stocks]  # Select the first 'num_stocks' columns of data
    data_list = selected_stocks.values.T.tolist()  # Transpose to get stocks as rows

    print(f"Number of stocks (rows): {len(data_list)}")
    print(f"Number of trading days (columns): {len(data_list[0])}")
    
    # Return the data list and actual ticker names
    return data_list, list(ticker_names)

def initialize_data_simulator(data_list, stock_names):
    """Initialize DataSimulator with stock data."""
    print("Initializing DataSimulator...")
    data_simulator = DataSimulator(stocks=stock_names, start=None, end=None)
    data_simulator.set_data(data_list)
    return data_simulator.get_asset_return_covariance_matrix(), data_simulator.get_asset_return_mean_vector()

def construct_hamiltonian(mean_vector, covariance_matrix, q, budget):
    """Construct the Hamiltonian for quantum portfolio optimization."""
    print("Constructing the Hamiltonian...")
    penalty = len(mean_vector)
    hamiltonian = portfolio_optimization_hamiltonian(penalty, mean_vector, covariance_matrix, q, budget)
    print("Hamiltonian constructed successfully.")
    return hamiltonian

def decode_and_evaluate_results(selected_bitstring, mean_vector, covariance_matrix, stock_names):
    """Decode bitstring to asset indices, calculate return, risk, and convert to stock tickers."""
    if len(selected_bitstring) != len(mean_vector):
        raise ValueError("Selected bitstring length does not match number of stocks!")
    selected_assets = [i for i, bit in enumerate(selected_bitstring) if bit == '1']
    portfolio_return = sum(mean_vector[i] for i in selected_assets)
    portfolio_risk = sum(covariance_matrix[i][j] for i in selected_assets for j in selected_assets)
    selected_tickers = [stock_names[i] for i in selected_assets]

    print(f"Selected Assets: {selected_tickers}")
    print(f"Portfolio Return: {portfolio_return:.6f}")
    print(f"Portfolio Risk: {portfolio_risk:.6f}")
    return selected_assets, portfolio_return, portfolio_risk

def main():
    # Argument parsing for flexibility
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_file', type=str, default='largeStockData_50.csv', help='Path to stock data CSV file')
    parser.add_argument('--num_stocks', type=int, default=12, help='Number of stocks to select')
    parser.add_argument('--q', type=float, default=0.5, help='Risk appetite')
    parser.add_argument('--budget', type=int, default=5, help='Number of assets to select')
    parser.add_argument('--risk_free_rate', type=float, default=0.01, help='Risk-free rate for Sharpe ratio calculation')
    args = parser.parse_args()

    # Step 1: Load stock data
    data_list, stock_names = load_stock_data(args.csv_file, args.num_stocks)

    # Step 2: Initialize DataSimulator
    covariance_matrix, mean_vector = initialize_data_simulator(data_list, stock_names)

    # Step 3: Construct the Hamiltonian
    hamiltonian = construct_hamiltonian(mean_vector, covariance_matrix, args.q, args.budget)

    # Step 4: Train the Quantum Neural Network (QNN)
    # Place QNN training code here if not moved to another file.

    # Step 5: Decode and Evaluate the Results
    selected_bitstring = '110001110000'  # Example bitstring result (adjust based on your quantum computation results)
    selected_assets, portfolio_return, portfolio_risk = decode_and_evaluate_results(
        selected_bitstring, mean_vector, covariance_matrix, stock_names
    )

    # Step 6: Calculate and Display Sharpe Ratio
    sharpe_ratio = calculate_sharpe_ratio(portfolio_return, portfolio_risk, args.risk_free_rate)
    print(f"Sharpe Ratio of Quantum Portfolio: {sharpe_ratio:.4f}")

    # Visualize Portfolio Contributions
    visualize_portfolio(selected_assets, mean_vector, covariance_matrix, portfolio_return, portfolio_risk, stock_names)

    # Generate and plot efficient frontier for comparison
    results = generate_efficient_frontier(mean_vector, covariance_matrix)
    plot_efficient_frontier(results, portfolio_return, portfolio_risk)

    # Example measurement probabilities (replace with actual values)
    prob_measure = {'110001': 0.4, '101110': 0.3, '000111': 0.3}
    visualize_measurement_distribution(prob_measure, stock_names)

if __name__ == "__main__":
    main()
