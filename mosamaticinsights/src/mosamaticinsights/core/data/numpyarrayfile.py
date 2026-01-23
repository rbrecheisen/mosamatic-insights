import os
import numpy as np
import SimpleITK as sitk
from mosamaticinsights.core.data.file import File


class NumpyArrayFile(File):
    def __init__(self, path):
        super(NumpyArrayFile, self).__init__(path)

    def load(self):
        if self.loaded():
            return True
        try:
            arr = np.load(self.path())
            self.set_object(arr)
            self.set_loaded(True)
            return True
        except ValueError as e:
            print(f'Error reading Numpy array file {self.path()} ({str(e)})')
            return False

    def to_nifti(self, dicom_file):
        if not self.loaded():
            self.load()
        if self.object() is not None:
            arr = self.object()
            arr = arr.astype(np.uint16)
            arr3d = arr[None, ...]
            img_itk = sitk.ReadImage(dicom_file.path())
            seg_itk = sitk.GetImageFromArray(arr3d)
            seg_itk.CopyInformation(img_itk)
            return seg_itk
        return None