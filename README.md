# Mosamatic Insights

## What can you do with Mosamatic Insights?

First of all, what many clinical researchers struggle with is handling DICOM data. It needs to be exported
from the PACS and then copied to a file structure that supports their clinical question. 

### 1. Scan selection

The first step would be scan selection. From the multitude of scans that are exported for each patient, 
which ones does the researcher actually need? And how is that decided? Let's say the researchers needs all
CT scans with PVP contrast. This is not always obvious just by looking at the images (if you could) but is
often described somewhere in the series description of the DICOM headers. 

This can be done by filtering. You can filter (and select) at the following levels:

1. Patient (default)
2. Study
3. Series
4. Image

