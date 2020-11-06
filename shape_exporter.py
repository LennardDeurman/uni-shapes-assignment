import uuid
import zipfile

class ShapeExporter:

    def __init__(self, shapes, file_name):
        self.shapes = shapes
        self.file_name = file_name
    
    def write(self):
        zf = zipfile.ZipFile(self.file_name, mode="w", compression=zipfile.ZIP_DEFLATED)
        for shape in self.shapes:
            zf.writestr("{0}-{1}.svg".format(shape.name(), str(uuid.uuid4())), shape.to_xml().encode())
        zf.close()
