# Laptop Price Predictor

This repository contains a Streamlit web application that predicts the price of a laptop based on various user inputs. The application leverages a pre-trained machine learning model to provide price estimations based on the selected laptop specifications.

## Features

- **Brand Selection**: Choose from a variety of laptop brands.
- **Type Selection**: Select the type of laptop (e.g., Ultrabook, Gaming, Notebook).
- **RAM**: Specify the amount of RAM (in GB).
- **Weight**: Input the weight of the laptop (in kg).
- **Touchscreen**: Indicate whether the laptop has a touchscreen.
- **IPS Display**: Indicate whether the laptop has an IPS display.
- **Screen Size**: Input the screen size (in inches).
- **Screen Resolution**: Select the screen resolution.
- **CPU**: Choose the CPU brand.
- **HDD**: Specify the HDD capacity (in GB).
- **SSD**: Specify the SSD capacity (in GB).
- **GPU**: Choose the GPU brand.
- **Operating System**: Select the operating system.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/laptop-price-predictor.git
    ```
2. Navigate to the project directory:
    ```sh
    cd laptop-price-predictor
    ```
3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Place the `pipe.pkl` and `df.pkl` files in the project directory. These files contain the pre-trained model and the dataset respectively.
6. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open your web browser and go to `http://localhost:8501`.
2. Fill in the laptop specifications using the provided input fields.
3. Click the "Predict Price" button to get the predicted price of the configured laptop.
4. The predicted price will be displayed below the button.

## Project Structure

- `app.py`: The main Streamlit application.
- `pipe.pkl`: The pre-trained machine learning model.
- `df.pkl`: The dataset used for the application.
- `requirements.txt`: List of Python dependencies.
- `example_screenshot.png`: Example screenshot of the application (if available).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
