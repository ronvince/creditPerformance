import bz2
import pickle

# Path to the compressed model file (assuming it's in the same directory)
compressed_model_path = "model1.pkl.bz2"

# Function to decompress the model
def load_compressed_model():
  with bz2.open(compressed_model_path, 'rb') as compressed_file:
    decompressed_data = compressed_file.read()

  with open("model1.pkl", 'wb') as decompressed_file:
    decompressed_file.write(decompressed_data)

  # Load the decompressed model using pickle
  with open('model1.pkl', 'rb') as file:
    model1 = pickle.load(file)

  # Remove the temporary decompressed file (optional)
  # os.remove("model1.pkl")  # Uncomment if you want to remove the temporary file

  return model1

# Load the model using the decompress function
model1 = load_compressed_model()

# Use the loaded model (model1) in your app.py logic
