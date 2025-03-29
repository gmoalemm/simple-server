from Server import Server
from MenuGenerator import MenuGenerator
import torch

MODEL_PATH = "model_weights.pth"

if __name__ == "__main__":
    # Load the model
    print("Loading model...")
    model = MenuGenerator()
    model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()

    # Create the server instance with the model
    server = Server(model)

    # Run the server
    print("Starting server...")
    server.run()
