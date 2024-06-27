# Brain Tumor Detection Application

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Welcome to the Brain Tumor Detection Application! This project leverages the power of machine learning to assist in the early detection of brain tumors using MRI images. Built with Python and Flask, this application provides an intuitive web interface for users to upload MRI scans and receive immediate feedback on the presence of tumors.

## Features
👉  **MRI Image Upload**: Easily upload MRI images for analysis.
<br/>
👉  **Tumor Detection**: Utilizes a trained machine learning model,VGG16 to detect brain tumors with high accuracy of 97%. <br/>
👉  **Result Visualization**: Visualize the detection results directly on the MRI images with type of tumour(Glioma,Meningioma,Pituary or if no tumour is present then the model prints no_tumour). <br/>
👉  **User-Friendly Interface**: Simple and intuitive web interface powered by Flask.<br/>
👉  **Scalable**: Easily deployable on any server or cloud platform.<br/>

## Demo
<br/>
##Model detecting GLIOMA:

<p align="center">
    <img src="Images/glioma (2).png"alt="glioma"width="80%"/>
</p>
<br/>

## Installation
To get started with the Brain Tumor Detection Application, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SahiLmb/Tumor_Detection_App.git
    cd Tumor_Detection_App
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory.
    - Add your environment variables following the format in `.env.example`.

5. **Run the application**:
    ```bash
    flask run
    ```
## Usage

Once the application is running, users need to:
1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Upload an MRI image using the provided interface.
3. Click "Submit" to analyze the image.
4. View the results to see if a brain tumor along with it's type has been detected.

## Contributing

Contributions to this project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Create a new pull request.

Please ensure your contributions adhere to the [code of conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance [Sahil Bodke](https://www.linkedin.com/in/sahilbodke/). Happy coding!
