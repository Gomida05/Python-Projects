from PIL import Image
from os import system, path, makedirs


class ImageResizer:
    def __init__(self, input_path, output_path):
        """
        Initialize the ImageResizer with input and output paths.
            :param input_path: str - Path to the input image file.
            :param output_path: str - Path to save the resized image.
        """
        self.input_path = input_path
        self.output_path = output_path
    
    def resize_image(self, width= 1024, height = 1024):
        """
        Resize the image to the specified width and height.
            :param width: int the desired width of the image default is 1024
            :param height: int the desired height of the image default is 1024
            :raises Exception: if there is an error in the resizing process
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width and height must be integers")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers")
        self.output_path = self.__isTheDirectoryExits(self.output_path)

        
        with Image.open(self.input_path) as img:
            resized_img = img.resize((width, height))

            resized_img.save(self.output_path, format="PNG")
            print(f"Image saved as {self.output_path}")
            print("Image resized successfully")
        return self
    def show(self):
        """
        Show the resized image.
            :raises Exception: if there is an error in the resized image
        """
        try:
            system(f'start {self.output_path}')
        except Exception as e:
            raise Exception(f"Error showing image: {e}")
        return self
    

        
    def __isTheDirectoryExits(self, file_path):
        """
        Check if the directory exists, if not create it.
            :raises Exception: if there is an error in the directory creation process
        """

        try:
            normalize_path = path.normpath(file_path)

            directory = path.dirname(normalize_path)
            if not path.exists(directory):
                makedirs(directory, exist_ok=True)

            return normalize_path

        except Exception as e:
            raise Exception(f"Error creating file: {e}")
