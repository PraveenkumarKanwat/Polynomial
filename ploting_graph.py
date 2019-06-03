import matplotlib.pyplot as plt


def plot_graph(x, y, title):
    plt.plot(x, y)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid(True, which='both')
    plt.title(title)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
