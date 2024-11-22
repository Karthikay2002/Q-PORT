# Q-PORT
Quantum Portfolio Optimization in Real-Time: Quantum Vertical Integrated Project @ Georgia Tech
# Q-Port: Quantum Portfolio Optimization

**Q-Port** is a quantum-inspired solution to portfolio optimization that leverages the power of quantum computing techniques, such as Variational Quantum Eigensolvers (VQE) and Quantum Hamiltonians, to achieve efficient, high-performing portfolio selections. It compares quantum-based strategies with classical approaches to highlight the potential of quantum algorithms in real-world finance.

---

## **Overview**

Portfolio optimization is a crucial task in finance, involving the selection of assets that maximize returns while minimizing risk. Classical methods face limitations when handling complex datasets or scaling to higher dimensions. 

**Q-Port** introduces quantum algorithms to solve this challenge by:
- Exploring multiple portfolio combinations simultaneously using quantum superposition.
- Encoding optimization problems into quantum Hamiltonians, where the lowest energy state represents the optimal portfolio.
- Balancing risk and return using tunable parameters.

---

## **Features**

1. **Quantum Optimization**:
   - Encodes the portfolio problem into a quantum system using a Hamiltonian approach.
   - Optimizes the system using hybrid quantum-classical algorithms like VQE.
   
2. **Comparison with Classical Optimization**:
   - Benchmarks quantum results against classical optimization methods.
   - Highlights performance improvements in terms of returns, risk, and Sharpe ratios.

3. **Visualizations**:
   - Efficient frontier plots to compare portfolio risk-return trade-offs.
   - Asset contribution breakdown showing individual return and risk contributions.
   - Measurement distribution of quantum states.
  
## Results

| Metric               | Quantum Portfolio              | Classical Portfolio |
|-----------------------|--------------------------------|---------------------|
| **Selected Assets**   | AAPL, MSFT, META, NVDA, ORCL  | NVDA                |
| **Portfolio Return**  | 0.029486                      | 0.011445            |
| **Portfolio Risk**    | 0.008381                      | 0.034697            |
| **Sharpe Ratio**      | 2.3250                        | 0.0416              |

---

## Visualizations

- **Efficient Frontier**:  
  Quantum portfolios outperform classical portfolios in risk-return trade-offs.
  
  ![Efficient Frontier](/efficient_frontier.png)

- **Asset Contributions**:  
  Shows individual asset return and risk contributions in the quantum portfolio.

  ![Asset Contributions](/asset_contribution.png)

---

## Challenges

- Translating quantum states into actionable portfolio decisions.
- Optimizing parameters for both risk and return balance.

