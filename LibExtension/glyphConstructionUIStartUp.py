from mojo.events import addObserver
from mojo.roboFont import CurrentFont
from mojo.tools import registerFileExtension

from glyphConstructionController import GlyphBuilderController


fileExtension = "glyphConstruction"
registerFileExtension(fileExtension)


class GlyphConstructionFileOpener(object):

    def __init__(self):
        addObserver(self, "applicationOpenFile", "applicationOpenFile")

    def applicationOpenFile(self, notification):
        path = notification["path"]
        ext = notification["ext"]
        fileHandler = notification["fileHandler"]
        if ext == ".%s" % fileExtension:
            controller = GlyphBuilderController(CurrentFont())
            controller.setFile(path)
            fileHandler["opened"] = True


GlyphConstructionFileOpener()
