import bz2
import pickle

def decompress_model():
  compressed_model_path = "model1.pkl.bz2"
  decompressed_model_path = "model1.pkl"  # Path for the decompressed model

  with bz2.open(compressed_model_path, 'rb') as compressed_file:
    decompressed_data = compressed_file.read()

  with open(decompressed_model_path, 'wb') as decompressed_file:
    decompressed_file.write(decompressed_data)

  with open(decompressed_model_path, 'rb') as file:
    model = pickle.load(file)

  return model
