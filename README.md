# Breast Cancer Predictor

This project is a web application that predicts whether a breast mass is benign or malignant based on cell nuclei measurements. The application uses a machine learning model trained on the Breast Cancer Wisconsin (Diagnostic) Data Set.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/CancerPrediction.git
    cd CancerPrediction
    ```
 

## Usage

1. Train the model:
    ```sh
    python model/main.py
    ```

2. Run the web application:
    ```sh
    streamlit run app/main.py
    ```

3. Open your web browser and go to `http://localhost:8501` to use the application.

## Features

- **Data Cleaning**: The data is cleaned by removing unnecessary columns and mapping diagnosis labels to binary values.
- **Sidebar Input**: Users can input cell nuclei measurements using sliders in the sidebar.
- **Radar Chart**: Visualizes the input data in a radar chart.
- **Prediction**: Predicts whether the breast mass is benign or malignant and shows the probabilities.

## Code Overview

- `app/main.py`: Contains the Streamlit application code.
  - `get_clean_data()`: Cleans the input data.
  - `add_sidebar()`: Adds input sliders to the sidebar.
  - `get_scaled_values(input_dict)`: Scales the input values.
  - `get_radar_chart(input_data)`: Generates a radar chart.
  - `add_predictions(input_data)`: Adds prediction results to the app.
  - `main()`: Main function to run the Streamlit app.

- `model/main.py`: Contains the code to train the machine learning model.
  - `createModel(data)`: Trains the logistic regression model.
  - `getCleanData()`: Cleans the training data.
  - `main()`: Main function to train the model and save it.

## Data

The dataset used is the Breast Cancer Wisconsin (Diagnostic) Data Set, which can be found [here](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)).

 
 
- The dataset is provided by the UCI Machine Learning Repository.
- The application uses [Streamlit](https://streamlit.io/) for the web interface.
- The machine learning model is built using [scikit-learn](https://scikit-learn.org/).

