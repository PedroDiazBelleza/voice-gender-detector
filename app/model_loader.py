from utils import create_model

def load_model(weights_path="results/model.h5"):
    model = create_model()
    model.load_weights(weights_path)
    return model
