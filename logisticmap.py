import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
"""
    Chaos theory & the Logistic Map
    Key resources: 
        - https://geoffboeing.com/2015/03/chaos-theory-logistic-map/
        - https://github.com/gboeing/pynamical
"""

def logistic_map(x, r):
    return r * x * (1 - x)

def static_lmap(growth, initial_x, iterations_n):
    x = np.zeros(iterations_n)
    x[0] = initial_x
    for i in range(1, iterations_n):
        x[i] = logistic_map(x[i-1], growth)

    plt.plot(range(iterations_n), x, label=f"rate={growth}")
    plt.xlabel("Iteration")
    plt.ylabel("x")
    plt.title("Logistic Map Dynamics")
    plt.legend()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"logistic_map_{timestamp}.png"
    plt.savefig(filename)
    plt.close()

    print(f"Plot saved as {filename}")

"""
    Aside from the standard linear logistic map visualizations achieved above, 
    you can instead have variate the growth rate 
    (ex: 200 generations across 1,000 growth rates within a certain range)
    best form of representation for this is a bifurcation diagram instead
"""
if __name__ == "__main__":
    # Example Parameters
    r = 3.9 
    x0 = 0.5 
    n_iter = 200
    static_lmap(r, x0, n_iter)

