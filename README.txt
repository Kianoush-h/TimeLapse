# Timelapse Video Generator

This Python script generates a timelapse video from a collection of images. Each image is displayed for 0.3 seconds in the resulting video. The script uses the `imageio` library to create the timelapse video in the MP4 format.

## Requirements

- Python 3.x
- imageio library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Install the required packages:

    ```bash
    pip install imageio
    ```

## Usage

1. Place your images in the designated folder.

2. Modify the `image_folder` variable in the script to point to the folder containing your images.

3. Run the script:

    ```bash
    python timelapse_generator.py
    ```

4. The resulting timelapse video will be saved as `timelapse_output.mp4` in the same directory.

## Customization

- You can adjust the frame duration by modifying the `frame_duration` variable in the script.
- Change the file extension in the script if your images are in a different format.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
