import unittest
from unittest.mock import patch
from tkinter import Tk, PhotoImage
from PIL import Image

import main  # Make sure to replace 'main' with the actual name of your script

class TestImageBackgroundRemovalApp(unittest.TestCase):
    def setUp(self):
        self.app = Tk()
        self.app.withdraw()  # Hide the main window during tests

    def tearDown(self):
        self.app.destroy()

    @patch("main.filedialog.askopenfilename", return_value="path/to/test_image.jpg")
    @patch("main.rembg.remove", return_value=Image.new("RGBA", (100, 100), (255, 0, 0, 0)))
    @patch("main.ImageTk.PhotoImage", return_value=PhotoImage())
    @patch("main.label.config")
    def test_remove_background(self, mock_label_config, mock_photo_image, mock_rembg_remove, mock_askopenfilename):
        main.remove_background()

        mock_askopenfilename.assert_called_once()
        mock_rembg_remove.assert_called_once()
        mock_label_config.assert_called_once()

    @patch("main.remove_background")
    @patch("main.Tk.bind")
    def test_restart_program(self, mock_bind, mock_remove_background):
        main.restart_program(None)

        mock_remove_background.assert_called_once()
        mock_bind.assert_called_once_with("<F5>", main.restart_program)

if __name__ == "__main__":
    unittest.main()
