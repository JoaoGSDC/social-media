import win32com.client
# import os
# from pathvalidate import sanitize_filename


class PhotoshopPy:
    app = None
    psd_file = None

    doc = None

    img = r"C:\Users\JoaoGSDC\Pictures\covers gkn\png\cbolao-segundo-split-2021.png"

    def __init__(self):
        self.app = None

    def openApp(self):
        import pythoncom
        pythoncom.CoInitialize()

        self.openPSD()

        self.doc = self.app.Application.ActiveDocument

        self.changeTitle()
        self.changeCover()

        self.exportInPng()

        self.closePsd()
        self.closePhotoshop()

    def openPSD(self):
        psdPath = r"C:\Users\JoaoGSDC\Pictures\feed instagram gkn\instagram_post_gkn.psd"

        self.app = win32com.client.Dispatch("Photoshop.Application")
        self.app.Open(psdPath)

    def changeTitle(self):
        layerTitle = self.doc.ArtLayers["Title"]
        textOfLayer = layerTitle.TextItem
        textOfLayer.contents = "CBOLÃO: Confira como foram as semifinais do CBOLÃO Open Qualify"

    def changeCover(self):
        self.app.Load(self.img)
        self.app.ActiveDocument.Selection.SelectAll()
        self.app.ActiveDocument.Selection.Copy()
        self.app.ActiveDocument.Close()
        self.app.ActiveDocument.Paste()

        self.doc.layers[0].Move(self.doc, 2)

    def exportInPng(self):
        options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
        options.Format = 13
        options.PNG8 = False

        pngfile = r"C:\Users\JoaoGSDC\Documents\Dev\Pessoal\social-media\img\instagram_feed.png"

        self.doc.Export(ExportIn=pngfile, ExportAs=2, Options=options)

    def closePsd(self):
        self.doc.Close(2)

    def closePhotoshop(self):
        self.app.Quit()
