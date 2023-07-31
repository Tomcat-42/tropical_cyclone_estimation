import gdown
import os

# Modelo pre treinado
url = 'https://drive.google.com/file/d/1Csj_YFAXHtnGpOutxZ9A6CBrGAsZkpXu/view?usp=sharing'
output = 'model.h5'
gdown.download(url, output, quiet=False, proxy=None, fuzzy=True)

## Dataset
url = 'https://drive.google.com/file/d/1-GaxHdsFv_gNmFqSxz1wRhc3a9uwMgsZ/view?usp=sharing'
output = 'dataset.zip'
gdown.cached_download(url,
                      output,
                      quiet=False,
                      proxy=None,
                      fuzzy=True,
                      postprocess=gdown.extractall)
