# Topsis-Ojasvi-102203960

## Introduction
This package implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS). TOPSIS is a multi-criteria decision analysis method that is used to evaluate the performance of a set of alternatives based on multiple criteria.

## Installation
You can install the package using pip:

pip install Topsis-Ojasvi-102203960


## Usage
You can use the package from the command line as follows:

topsis <input_file> <weights> <impacts> <output_file>


### Arguments:
- `input_file`: CSV file containing the data (alternatives and criteria).
- `weights`: Comma-separated list of weights for each criterion.
- `impacts`: Comma-separated list of impacts for each criterion ('+' for beneficial, '-' for non-beneficial).
- `output_file`: Name of the output CSV file that will contain the results.

### Example:
topsis data.csv "1,1,1,1" "+,+,-,+" result.csv




This command will calculate the TOPSIS score for the data in `data.csv` and save the results in `result.csv`.

## Input File Format
The input CSV file should have the following format:
- The first row should contain the criteria names.
- The first column should contain the alternative names.
- The remaining cells should contain the criteria values for each alternative.

### Example:
Alternative, Criterion1, Criterion2, Criterion3, Criterion4 A1, 250, 16, 12, 5 A2, 200, 16, 8, 3 A3, 300, 32, 16, 4 A4, 275, 32, 8, 4

yaml


## Output File Format
The output CSV file will contain the following columns:
- Alternatives: Names of the alternatives.
- TOPSIS Score: Calculated TOPSIS scores.
- Rank: Rank of each alternative based on the TOPSIS scores.

## Example Output:

Alternative, TOPSIS Score, Rank A1, 0.56, 2 A2, 0.32, 4 A3, 0.78, 1 A4, 0.45, 3


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The concept of TOPSIS was first developed by Hwang and Yoon in 1981.
- This package is inspired by the need to provide a simple, easy-to-use implementation of TOPSIS for Python users.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author
Ojasvi - [Your GitHub Profile](https://github.com/yourusername)
