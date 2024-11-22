import numpy as np
import matplotlib.pyplot as plt


def visualize_portfolio(selected_assets, mean_vector, covariance_matrix, portfolio_return, portfolio_risk, stocks):
    """
    Visualizes the contribution of each asset in the selected quantum portfolio.
    """
    # Check if inputs are consistent
    if len(selected_assets) > len(mean_vector):
        raise ValueError("Selected assets exceed the available assets in the mean vector!")

    # Calculate contributions for each selected asset
    selected_returns = [mean_vector[i] for i in selected_assets]
    selected_risks = [sum(covariance_matrix[i][j] for j in selected_assets) for i in selected_assets]
    tickers = [stocks[i] for i in selected_assets]  # Assuming `stocks` contains ticker names

    # Plot contributions
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(tickers))
    width = 0.35

    # Plot return and risk contributions
    ax.bar(x - width/2, selected_returns, width, label='Return Contribution')
    ax.bar(x + width/2, selected_risks, width, label='Risk Contribution')

    # Labeling
    ax.set_xlabel('Selected Assets')
    ax.set_ylabel('Contribution')
    ax.set_title('Contribution of Selected Assets in Quantum Portfolio')
    ax.set_xticks(x)
    ax.set_xticklabels(tickers, rotation=45, ha="right")
    ax.legend()

    plt.tight_layout()
    plt.show()


def visualize_measurement_distribution(prob_measure, stock_names):
    """
    Visualizes the measurement distribution of the final quantum states, mapping binary states to stock tickers.
    """
    # Decode binary states into meaningful labels
    decoded_states = []
    for state in prob_measure.keys():
        selected_indices = [i for i, bit in enumerate(state) if bit == '1']
        selected_tickers = [stock_names[i] for i in selected_indices]
        decoded_states.append(", ".join(selected_tickers))

    # Convert the dictionary into lists for plotting
    probabilities = list(prob_measure.values())

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(decoded_states, probabilities, color='skyblue')
    ax.set_xlabel('Measured Quantum States (Mapped to Tickers)')
    ax.set_ylabel('Probability')
    ax.set_title('Measurement Distribution of Quantum Portfolio States')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def check_data_consistency(mean_vector, covariance_matrix):
    """
    Validates the consistency of mean vector and covariance matrix dimensions.
    """
    if len(mean_vector) != len(covariance_matrix):
        raise ValueError("Mean vector and covariance matrix dimensions do not match!")
    for row in covariance_matrix:
        if len(row) != len(mean_vector):
            raise ValueError("Covariance matrix is not square or does not match mean vector dimensions.")
    print("Data consistency check passed.")


# Example main function for testing utilities independently
if __name__ == "__main__":
    # Example placeholder data
    mean_vector = [0.001, 0.002, 0.0015, 0.003, 0.0025]  # Replace with actual data
    covariance_matrix = np.eye(5) * 0.001  # Replace with actual data
    selected_assets = [0, 1, 3]  # Example selected assets (indices)
    portfolio_return = 0.01  # Replace with actual portfolio return
    portfolio_risk = 0.02  # Replace with actual portfolio risk
    stocks = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'META']  # Example stock names
    prob_measure = {'00011': 0.5, '10101': 0.3, '11000': 0.2}  # Example quantum measurement probabilities

    # Run utility functions
    check_data_consistency(mean_vector, covariance_matrix)
    visualize_portfolio(selected_assets, mean_vector, covariance_matrix, portfolio_return, portfolio_risk, stocks)
    visualize_measurement_distribution(prob_measure)
