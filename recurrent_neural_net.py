import matplotlib.pyplot as plt

high = 1
medium = 0.5
low = 0

times = [0, 1]
observations = [low, medium]

def stock_market_figure(observations):
    fig = plt.figure(figsize=(10,10))
    
    plt.scatter(
        x=times, 
        y=observations,
        c="blue"
        )
    
    plt.show()