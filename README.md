# Road-Accident-Analysis-And-Traffic-Severity-Prediction

## Project Overview

This project, developed during my 4th semester in college, focuses on analyzing road accident data and predicting traffic severity using machine learning algorithms. After experimenting with various algorithms, XGBoost was found to provide the highest accuracy and has been deployed on a website for practical use.

## Features

- **Data Analysis**: Comprehensive analysis of road accident data to identify patterns and trends.
- **Severity Prediction**: Predicts the severity of traffic incidents based on input features.
- **Algorithm Comparison**: Evaluation of multiple machine learning algorithms to identify the best performer.
- **Deployment**: The model with the highest accuracy, XGBoost, has been deployed on a web platform for real-time predictions.

## Technologies Used

- **Python**: For data processing, analysis, and machine learning model development.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization.
- **Scikit-learn**: For implementing machine learning algorithms.
- **XGBoost**: For building and tuning the most accurate prediction model.
- **Flask**: For deploying the model as a web application.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/road-accident-analysis.git
    cd road-accident-analysis
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. To run the data analysis and model training script:
    ```bash
    python analysis_and_training.py
    ```

2. To start the web application:
    ```bash
    python app.py
    ```

3. Navigate to `http://127.0.0.1:5000` in your web browser to use the traffic severity prediction tool.

## Project Structure

```
road-accident-analysis/
│
├── data/
│   ├── accidents.csv                # Raw data
│   └── processed_data.csv           # Processed data for analysis
│
├── notebooks/
│   ├── data_analysis.ipynb          # Jupyter notebook for data analysis
│   └── model_evaluation.ipynb       # Jupyter notebook for model evaluation
│
├── src/
│   ├── data_preprocessing.py        # Script for data preprocessing
│   ├── model_training.py            # Script for training machine learning models
│   └── prediction.py                # Script for making predictions
│
├── templates/
│   └── index.html                   # HTML file for the web app
│
├── static/
│   ├── css/
│   │   └── styles.css               # CSS file for styling the web app
│   └── js/
│       └── scripts.js               # JavaScript file for web app functionality
│
├── analysis_and_training.py         # Main script for running analysis and training
├── app.py                           # Flask app script for deployment
├── requirements.txt                 # Python packages required
└── README.md                        # Project readme file
```

## Contributing

Contributions are welcome! Please create an issue to discuss any changes or improvements before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- My college professors for their guidance and support.
- The open-source community for providing valuable resources and tools.

---

Feel free to reach out if you have any questions or suggestions! Happy coding!

---

**Author**: Niharika Khanna  
**Contact**: khanna.niharika09@gmail.com

