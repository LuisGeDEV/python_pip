import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ['A','B','C']
    values = [20, 34, 113]
    fig, ax = pylot.subplots()
    ax.pie(values, labels = labels)
    # pylot.show()
    pylot.savefig('./charts/pie.png')
    pylot.close()