"""import os

path="notebooks/research.ipynb"

dir,file=os.path.split(path)

os.makedirs(dir)

with open(file,'w') as f:
    pass
"""


from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

customdataobj = CustomData(1.52,62.2,58.0,7.27,7.33,4.55,"Premium","F","VS2")

data = customdataobj.get_data_as_dataframe()
print(data)