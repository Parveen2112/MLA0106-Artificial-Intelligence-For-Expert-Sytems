import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# XOR inputs and outputs
X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[0]])

# Random weights and biases
np.random.seed(1)
W1 = np.random.randn(2,2)
b1 = np.zeros((1,2))
W2 = np.random.randn(2,1)
b2 = np.zeros((1,1))

# Forward propagation
hidden = sigmoid(np.dot(X, W1) + b1)
output = sigmoid(np.dot(hidden, W2) + b2)

print("Input:\n", X)
print("Predicted Output:\n", np.round(output, 3))
