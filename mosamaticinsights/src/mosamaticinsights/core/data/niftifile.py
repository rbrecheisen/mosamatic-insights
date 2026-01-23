import numpy as np
import SimpleITK as sitk
from mosamaticinsights.core.data.file import File


class NiftiFile(File):
    def __init__(self, path):
        super(NiftiFile, self).__init__(path)

    def load(self):
        if self.loaded():
            return True
        try:
            img = sitk.ReadImage(self.path())
            self.set_object(img)
            self.set_loaded(True)
            return True
        except RuntimeError as err:
            print(f'Error reading NIFTI file {self.path()} ({str(err)})')
            return False
        
    def to_numpy(self, rot90=False):
        if not self.loaded():
            self.load()
        if self.object() is not None:
            img = self.object()
            arr = sitk.GetArrayFromImage(img)
            arr = arr[..., 0]
            if rot90:
                arr = np.rot90(arr, k=3, axes=(0, 1))
            return arr
        return None