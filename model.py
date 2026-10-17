import numpy as np
from sklearn.linear_model import LinearRegression

def train():
    # Sample data: House Area (sq ft) vs. Price (Lakhs)
    X = np.array([[800], [1000], [1200], [1500], [1800], [2000], [2500]])
    y = np.array([40, 50, 60, 75, 90, 100, 125])
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    return model