# LoRaWAN Network Performance Evaluation Program

This repository contains a Python program that predicts Effective Signal Propagation (ESP) in LoRaWAN networks using trained Decision Tree models. The work is based on real sensor network data collected in smart city environments. 

---

## Description
This program is designed to:

- Predict ESP based on key environmental and network parameters such as SNR, transmission power, distance, packet loss, and the month of the year.
- Leverage pre-trained Decision Tree models to provide accurate predictions under various scenarios:
  1. **Free scenario**
  2. **Covered scenario**
  3. **Underground scenario**

This study is part of the research described in the paper:

> *"Evaluating LoRaWAN Network Performance in Smart City Environments Using Machine Learning"*

### Important Notice:
- The provided models and code are intended **only for research purposes**.
- These models should **not** be used for any practical or commercial applications until the review process for the paper has been completed.

---

## Prerequisites
The program requires Python 3 and the following Python packages:

- `pandas==2.2.3`
- `scikit-learn==1.6.0`
- `numpy==2.0.2`
- `pickle5==0.0.11`

The program will automatically install these dependencies if you give permission during execution.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/lorawan-network-evaluation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd lorawan-network-evaluation
   ```

3. Run the program:

   ```bash
   python main.py
   ```

---

## Usage

1. **Dependencies Installation**: 
   The program will prompt you to install the required packages. Type `1` to proceed or `2` to abort.

2. **Select Scenario**:
   Choose the appropriate scenario by typing one of the following:
   - `1` for Free scenario
   - `2` for Covered scenario
   - `3` for Underground scenario

3. **Input Parameters**:
   Provide the following inputs:
   - Signal-to-Noise Ratio (SNR) in dB
   - Transmission Power (Tx) in mW
   - Distance in meters
   - Mean Packet Loss (as a decimal value)
   - Month (integer between 1 and 12, representing January to December)

4. **Predicted Output**:
   The program will use the Decision Tree model to predict the ESP value based on the input parameters.

---

## File Structure

- `main.py`: The main program file.
- `free.pkl`: Pre-trained Decision Tree model for the Free scenario.
- `covered.pkl`: Pre-trained Decision Tree model for the Covered scenario.
- `underground.pkl`: Pre-trained Decision Tree model for the Underground scenario.

---

## Citation
You are not al;lowed to use this code until the paper review process finishes


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Disclaimer
This program is intended solely for use by reviewers and exclusively for the purposes of the review process, ensuring its evaluation aligns with the study's objectives and ethical standards.
This program and its associated models are provided "as is" without warranty of any kind. Use of this program is subject to ethical research practices and adherence to publication guidelines. The models should NOT be used for any purpose until the review process of the associated paper is completed.
