class PDFReader:
    def open(self):
        return"Opening PDFReader in Reader Mode"

class ImageViewer:
    def open(self):
        return"Opening ImageViewer in Full Resolution"


viewers = [PDFReader(),ImageViewer()]
for v in viewers:
    print(v.open())