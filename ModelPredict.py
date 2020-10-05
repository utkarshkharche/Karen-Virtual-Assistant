import random
import json

import torch
import torch.nn as nn

from model import NeuralNet
from nltk_utils import bag_of_words,tokenize 

device = torch.cuda.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('commands.json',) as json_data:
    commands = json.load(json_data)


FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

device = torch.cuda._device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device=device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Karen"
print("Hi...")
while True:
    query = input("You: ")
    if query == "quit":
        break
    
    query = tokenize(query)
    X = bag_of_words(query, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > .90:
        for command in commands['commands']:
            if tag == command["tag"]:
                print(f"{bot_name}: {random.choice(command['responses'])}")
            
    else:
        print(f"{bot_name}: I did not understand...")




