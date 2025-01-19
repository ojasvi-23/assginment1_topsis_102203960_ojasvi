import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, result_file):
    try:
        # Load input file
        data = pd.read_csv(input_file)

        # Validate the input file
        if data.shape[1] < 3:
            raise ValueError("Input file must contain three or more columns.")

        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')

        if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
            raise ValueError(
                f"Number of weights ({len(weights)}), impacts ({len(impacts)}), and columns ({data.shape[1] - 1}) must match."
            )

        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be '+' or '-'.")

        # Normalize the data
        numeric_data = data.iloc[:, 1:].values
        norm_data = numeric_data / np.sqrt((numeric_data ** 2).sum(axis=0))

        # Weighted normalized decision matrix
        weighted_norm = norm_data * weights

        # Calculate ideal best and worst
        ideal_best = np.max(weighted_norm, axis=0) if impacts == '+' else np.min(weighted_norm, axis=0)
        ideal_worst = np.min(weighted_norm, axis=0) if impacts == '+' else np.max(weighted_norm, axis=0)

        # Calculate distances and scores
        distance_best = np.sqrt(((weighted_norm - ideal_best) ** 2).sum(axis=1))
        distance_worst = np.sqrt(((weighted_norm - ideal_worst) ** 2).sum(axis=1))
        scores = distance_worst / (distance_best + distance_worst)

        # Add scores and rank to the dataframe
        data['Topsis Score'] = scores
        data['Rank'] = pd.Series(scores).rank(ascending=False).astype(int)

        # Save the result
        data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, result_file = sys.argv
        topsis(input_file, weights, impacts, result_file)

