print("This program is based on real sensor network data collected in smart city environments.")
print("The purpose of this study is to predict Effective Signal Propagation (ESP) through a trained Decision Tree model, leveraging key environmental and network parameters.")
print("This work is described in the paper titled:")
print("\"Evaluating LoRaWAN Network Performance in Smart City Environments Using Machine Learning.\"")
print("We emphasize that the models and findings presented here are intended for research purposes only.")
print("Please refrain from using these models for any research or practical or commercial applications until the review process for the paper has been completed.")
print("We appreciate your understanding and adherence to the ethical use of this research.")


import subprocess
import sys

# List of required packages
print("the appropriate packets will be installed on your computer...")
print("pandas==2.2.3 \n","scikit-learn==1.6.0 \n","numpy==2.0.2 \n","pickle5==0.0.11\n")

permission=int(input("Type 1 for accepting the installation or 2 for aborting the installation \n"))
if permission==1:
        
    required_packages = [
        "pandas==2.2.3",
        "scikit-learn==1.6.0",
        "numpy==2.0.2",
        "pickle5==0.0.11"
    ]

    # Install each package if not already installed
    for package in required_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            sys.exit(1)

    # Proceed with the rest of the imports
    import pickle
    import numpy as np
    import pandas as pd 
    import pickle
    import numpy as np
    import pandas as pd

    # Specify the appropriate .pkl model
    choice=int(input("Type 1. for free scenario, 2. for covered case, 3 for underground"))

    if choice==1:
        
        file_path = 'free.pkl'
        print("you have chosen the free case model")
        print("minimum SNR is -12.00dB, maximum SNR is 13.25dB")
        print("minimum Tx Power is 2dB, maximum Tx Power is 16dB")
        print(" ")
    elif choice==2:
        
        file_path = 'covered.pkl'
        print("you have chosen the covered case model")
        print("minimum SNR is -12.00dB, maximum SNR is 13.75dB")
        print("minimum Tx Power is 2dB, maximum Tx Power is 16dB")

    elif choice==3:
        
        file_path = 'underground.pkl'
        print("you have chosen the underground case model")
        print("minimum SNR is -11.75dB, maximum SNR is 12.50dB")
        print("minimum Tx Power is 2dB, maximum Tx Power is 16dB")

    else:
        print("Try to type either 1 or 2 or 3. ")

    # Open the file and load the model
    with open(file_path, 'rb') as file:
        decision_tree_model = pickle.load(file)

    print("Number of Features Expected by the Model:", decision_tree_model.n_features_in_)

    SNR=float(input("SNR in dB: "))
    Tx=float(input("Tx Power in mW: "))
    Distance=float(input("Distance in m: "))
    MeanPER=float(input("PacketLoss as a decimal number : "))
    Month=int(input("Month (starting from integer number 1->January): "))

    # Input features in the same order as used in training model
    input_data = pd.DataFrame({
        0: [SNR],  # Replace with actual feature values
        1: [Tx],
        2: [Distance],
        3: [MeanPER],
        4: [Month]
    })

    # Predict using the model
    predicted_value = decision_tree_model.predict(input_data)
    print(f"Predicted Target Value: {predicted_value[0]}")

else:
    print("the program can not run without the appropriate Decision Tree models")
