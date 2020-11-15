import matplotlib.pyplot as plt


def buildPlot(x: list, y: list, table_name: str, x_lbl: str, y_lbl: str, label: str):
    fig, ax = plt.subplots()
    plt.title(table_name)

    plt.xlabel(f'{x_lbl}')
    plt.ylabel(f'{y_lbl}')
    plt.grid()
    plt.plot(x, y, linestyle='-', marker='o', markerfacecolor='yellow', markersize=4, color='blue', label=label)
    plt.legend()
    ax
    plt.show()
    fig.savefig(f'./Графики/{table_name}.')
