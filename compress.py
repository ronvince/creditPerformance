import pickle
import bz2

# Load your trained model
with open('model1.pkl', 'rb') as file:
    model = pickle.load(file)

# Compress the model
with bz2.BZ2File('model1.pkl.bz2', 'wb') as file:
    pickle.dump(model, file)
