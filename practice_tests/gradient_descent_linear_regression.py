import numpy as np
import matplotlib.pyplot as plt

# Initialize training data
X = np.array([1, 2, 3, 4, 5])  
Y = np.array([2, 4, 6, 8, 10])

# Model parameters initialization
m = 0.0  
b = 0.0
L = 0.01  # Learning rate (relative faster convergence)
epochs = 1500  # Number of iterations
n = len(X)  # Number of data points

# Calculating the Gradient Descent
for i in range(epochs):

    # Current predictions
    Y_pred = m * X + b
    
    # Calculate loss (MSE)
    loss = np.mean((Y - Y_pred)**2)
    
    # Compute the partial derivatives of the loss with respect to `m` and `b`
    grad_m = (-2/n) * np.dot(X, (Y - Y_pred))
    grad_b = (-2/n) * np.sum(Y - Y_pred)
    
    # Update `m` and `b` using the learning rate and the computed gradients
    m -= L * grad_m
    b -= L * grad_b   

     # Print progress every 10 epochs(it is just to see how it is converging to the actual)
    # if i % 10 == 0:
    #     print(f'Epoch {i}: m = {m:.4f}, b = {b:.4f}, Loss = {loss:.4f}')   
   

# Final Values
print(f'\nFinal Values: m = {m:.4f}, b = {b:.4f}')

# asking the user for input(X) and predict Y
while True:
    try:
        user_input = input("Enter X value for prediction (or 'q' to quit and see the graph): ")
        if user_input.lower() == 'q':
            break
        x_new = float(user_input)
        y_pred = m * x_new + b
        print(f"Predicted Y for X = {x_new}: {y_pred:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

# Visualization
plt.figure(figsize=(7, 7))
plt.scatter(X, Y, label='Training Data')
plt.plot(X, m*X + b, color='red', label=f'Final Fit: y = {m:.2f}x + {b:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regression Fit')
plt.legend()
plt.tight_layout()
plt.show()




