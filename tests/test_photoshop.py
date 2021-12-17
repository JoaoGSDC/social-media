from photoshop import PhotoshopPy
import os
import sys
import unittest
sys.path.insert(0, '../venv/src')


class TestPhotoshop(unittest.TestCase):
    def setUp(self):
        self.psd_origin = os.path.abspath('./resources/instagram_post_gkn.psd')
        self.jpeg_path = os.path.abspath('./resources/temp')
        self.jpeg_name = "instagram_feed.png"
        self.jpeg_full_path = os.path.join(self.jpeg_path, self.jpeg_name)

        if not os.path.exists(self.jpeg_path):
            os.mkdir(self.jpeg_path)

        self.app = PhotoshopPy()

    def tearDown(self):
        self.app.closePhotoshop()

        if os.path.exists(self.jpeg_full_path):
            os.remove(self.jpeg_full_path)

        if os.path.exists(self.jpeg_path):
            os.rmdir(self.jpeg_path)

    def test_openPSD(self):
        opened = self.app.openPSD(self.psd_origin)
        if opened:
            self.app.closePSD()
        self.assertTrue(opened)

    def updateLayerText(self, layer_name, text):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)

        layer = self.psd_file.ArtLayers[layer_name]
        layer_text = layer.TextItem
        layer_text.contents = text

    def test_updateLayerText(self):
        updateTitle = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            updateTitle = self.app.updateLayerText("Title", "Testando")
            self.app.closePSD()

        self.assertTrue(updateTitle)


if __name__ == '__main__':
    unittest.main()
