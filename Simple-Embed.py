def getDependencies():
  !pip install git+https://github.com/UKPLab/sentence-transformers
  !pip install embedding_as_service
  !pip install laserembeddings
  !python -m laserembeddings download-models