# AgeGenDetect

## Project Description

**AgeGenDetect** is a project designed to detect the age and gender of individuals using a camera. This project leverages TensorFlow for creating age and gender detection models, while OpenCV is utilized to process and detect faces from the camera feed and deliver the results to the user in real time.

## Technologies Used

- **Python**: The primary programming language used for this project.
- **TensorFlow**: Employed for creating and training the age and gender detection models.
- **OpenCV**: Utilized for processing images and detecting faces from the camera.
- **Kaggle API**: Used for downloading the UTKFace dataset required for training.

## Dataset

The project uses the UTKFace dataset, obtained from Kaggle, as it provides crucial age and gender information for training. The UTKFace dataset is copyrighted by its original authors. More information can be found [here](https://www.kaggle.com/datasets/jangedoo/utkface-new).

### Setting Up the Dataset

Follow these steps to download the dataset used in this project:

1. Obtain your Kaggle API key and place the `kaggle.json` file in the root directory of the project.
2. Run the following commands to download and set up the dataset:

    ```python
    from google.colab import files
    files.upload()

    !mkdir -p ~/.kaggle
    !cp kaggle.json ~/.kaggle/
    !chmod 600 ~/.kaggle/kaggle.json

    !kaggle datasets download -d jangedoo/utkface-new
    !unzip utkface-new.zip -d data/utkface
    ```

## Model Training and Usage

The models required for this project are pre-trained and available in the `models` folder. If you wish to modify the models or retrain them, you can use the `building_models.ipynb` notebook located in the `notebooks` folder. These TensorFlow models are employed to detect the age and gender of individuals based on images captured from the camera.

## Running the Project

You can run this project using Docker for a streamlined setup and environment consistency.

### Docker Setup

1. **Build the Docker Image:**

   ```bash
   docker build -t age-gender-prediction-app .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run -p 5000:5000 age-gender-prediction-app
   ```

   After running the above command, the application will be accessible at `http://localhost:5000`.

### Testing the Application

Once the Docker container is running, open your web browser and navigate to:

```
http://localhost:5000
```

The application will use your camera to detect faces and predict the age and gender of the detected individuals in real-time.

## Project Web Version

You can also explore the project directly on my website, where the live version is hosted. Visit [this link](http://www.mesutby-ai.com/) to view and test the project online.

## Contributing

If you would like to contribute to the project, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

---

This README file is now concise, focusing on the project's purpose, how to set it up, and how to run it using Docker. It also directs users to your website for further exploration and testing.