from NumPartAlgosTesting import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

num_sim = 50
dim = 100
n = 10**12
max_iter = 25000

# Prepare a DataFrame to store results
columns = ['Instance', 'Algorithm', 'Representation', 'Residue']
results_df = pd.DataFrame(columns=columns)

for i in range(num_sim):
    print(f"Running simulation {i + 1}")
    A = GenRandomProblem(n, dim)
    S = GenerateRandomSolution(dim)
    P = GenerateRandomPrePart(dim)
    
    # Run Karmarkar-Karp
    kk_residue = KarmarkarKarp(A)
    new_row = pd.DataFrame({'Instance': [i + 1], 'Algorithm': ['Karmarkar-Karp'], 'Representation': ['Karmarkar-Karp'], 'Residue': [kk_residue]})
    results_df = pd.concat([results_df, new_row], ignore_index=True)
    
    # Repeated Random, Hill Climbing, Simulated Annealing for both representations
    for representation in ['standard', 'prepartition']:
        # Repeated Random
        rr_residue, _ = RepeatedRandom(A, max_iter, S, P, representation=representation)
        new_row = pd.DataFrame({'Instance': [i + 1], 'Algorithm': ['Repeated Random'], 'Representation': [representation], 'Residue': [rr_residue]})
        results_df = pd.concat([results_df, new_row], ignore_index=True)

        # Hill Climbing
        hc_residue, _ = HillClimbing(A, max_iter, S, P, representation=representation)
        new_row = pd.DataFrame({'Instance': [i + 1], 'Algorithm': ['Hill Climbing'], 'Representation': [representation], 'Residue': [hc_residue]})
        results_df = pd.concat([results_df, new_row], ignore_index=True)
        
        # Simulated Annealing
        sa_residue, _ = simAnneal(A, max_iter, S, P, representation=representation)
        new_row = pd.DataFrame({'Instance': [i + 1], 'Algorithm': ['Simulated Annealing'], 'Representation': [representation], 'Residue': [sa_residue]})
        results_df = pd.concat([results_df, new_row], ignore_index=True)

# Visualization
plt.figure(figsize=(12, 8))
sns.boxplot(x='Algorithm', y='Residue', hue='Representation', data=results_df)
plt.title('Algorithm Performance Comparison')
plt.yscale('log')  # Use logarithmic scale if residues vary widely
plt.legend(title='Representation')
plt.show()

