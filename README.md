# AgeGenDetect

**Project Description:**

AgeGenDetect is a project designed to predict the age and gender of individuals based on images captured from a camera. This project was developed using TensorFlow and OpenCV. TensorFlow is used to create and train the models for age and gender detection, while OpenCV is used to detect the individual and display the results to the user.

**Technologies Used:**

- **Python**: The primary programming language used to develop the project.
- **TensorFlow**: Used to create and train models for age and gender detection.
- **OpenCV**: Used to process and detect images captured from the camera.
- **Flask**: Used to create the web interface and handle user interactions.
- **Kaggle API**: Used to download the UTKFace dataset.

## Setup and Running:

### Requirements:

1. Python 3.10.0 or above.
2. The following Python packages, which are included in the `requirements.txt` file:
   - Flask
   - TensorFlow
   - OpenCV
   - Numpy

### Steps:

1. Clone the project:

    ```bash
    git clone https://github.com/username/agegendetect.git
    cd agegendetect
    ```
### Additional Step: Creating a Virtual Environment (Recommended)
-  After cloning the project, create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux and MacOS
   venv\Scripts\activate  # For Windows
   ```

2. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download Models and Dataset:**

   The models used in the project are pre-trained and available in the `models` folder. If you want to train your own models, you can use the `building_models.ipynb` notebook.

   To download the UTKFace dataset, follow these steps:

    ```python
    from google.colab import files
    files.upload()

    !mkdir -p ~/.kaggle
    !cp kaggle.json ~/.kaggle/
    !chmod 600 ~/.kaggle/kaggle.json

    !kaggle datasets download -d jangedoo/utkface-new
    !unzip utkface-new.zip -d data/utkface
    ```

4. **Run the Project:**

    To run the Flask server, use the following command:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to [http://localhost:5000](http://localhost:5000) to use the project.

### How to Use the Project:

- **Age and Gender Prediction via Camera:**
    - The project captures video from your camera and predicts the age and gender every 5 seconds.
    - Click the "Start Prediction" button to begin the prediction process.
    - Click the "Stop Prediction" button to stop the camera and the prediction process.
    - The prediction results will be displayed on the screen.

**Training Your Own Models:**

- To retrain the age and gender models, use the `building_models.ipynb` notebook.
- The models will be saved in the `models` folder in `.keras` format.
  
### Contributing:

If you wish to contribute to this project, please review the [CONTRIBUTING.md](CONTRIBUTING.md) file first.

### License:

This project is licensed under the [MIT License](LICENSE).