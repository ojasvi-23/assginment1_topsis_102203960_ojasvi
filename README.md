# assginment1_topsis_102203960_ojasvi

This repository contains a Python implementation of the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**, a multi-criteria decision-making method to rank alternatives based on their closeness to the ideal solution.

## Features
- Handles multiple alternatives and criteria.
- Allows custom weights and impacts (+/-) for criteria.
- Outputs ranked alternatives with scores.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/topsis-python.git
   cd topsis-python
Install dependencies:
bash
Copy
Edit
pip install pandas numpy
Usage
Prepare a CSV file:
csv
Copy
Edit
Alternative, Criterion1, Criterion2, Criterion3
A1, 250, 16, 12
A2, 200, 32, 8
A3, 300, 24, 16
Run the script:
bash
Copy
Edit
python topsis.py <input_file> <weights> <impacts> <output_file>
Example:
bash
Copy
Edit
python topsis.py data.csv 0.4,0.3,0.3 +,-,+ result.csv
Example
Input:
CSV file with alternatives and criteria.
Weights: 0.4,0.3,0.3, Impacts: +, -, +

Output:

csv
Copy
Edit
Alternative, Score, Rank
A3, 0.68, 1
A1, 0.56, 2
A2, 0.32, 3
Requirements
Python 3.x
Libraries: pandas, numpy
Install dependencies using:
bash
Copy
Edit
pip install pandas numpy
License
This project is open-source under the MIT License.
