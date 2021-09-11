import matplotlib.pyplot as plt
import numpy as np 
from appJar import gui

# Create a def to cancel button
def cancel(button):
    if button == "Cancelar":
        app.stop()

# Create a GUI variable called app
app = gui("Geometria Analítica", "400x200")
app.setBg("white")
app.setFont(size=18, family="Bebas Neue")

# Add & configure widgets
app.addLabel("title", "Insira os valores de x1, x2, y1 e y2:")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("x1")
app.addLabelEntry("x2")
app.addLabelEntry("y1")
app.addLabelEntry("y2")

# Create a def to input data into the cartesian plane graphic
def graphic():
    x1 = float(app.getEntry("x1"))
    x2 = float(app.getEntry("x2"))
    y1 = float(app.getEntry("y1"))
    y2 = float(app.getEntry("y2"))
    result = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

    xs = [0, x1, x2]
    ys = [0, y1, y2]
    colors = ['m', 'g', 'r']
    
    # Create the graphic
    # Select length of axes and the space between tick labels
    if x1 <=5 and x2 <=5 and y1 <=5 and y2 <=5:
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        ticks_frequency = 1
    elif (x1 >5 and x1 <10) or (x2 >5 and x2 <10) or (y1 >5 and y1 <10) or (y2 >5 and y2 <10):
        xmin, xmax, ymin, ymax = -10, 10, -10, 10 
        ticks_frequency = 1
    elif (x1 >10 ) or (x2 >10) or (y1 >10) or (y2 >10):
        largest = max(x1,x2,y1,y2)
        xmin, xmax, ymin, ymax = -(largest), (largest), -(largest), (largest)
        ticks_frequency = round((largest)/10)

    # Plot points and window title
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.canvas.set_window_title('Plano Cartesiano')
    ax.scatter(xs, ys, c=colors)

    # Draw lines connecting points to axes
    for x, y, c in zip(xs, ys, colors):
        ax.plot([x, x], [0, y], c=c, ls='--', lw=1.5, alpha=0.5)
        ax.plot([0, x], [y, y], c=c, ls='--', lw=1.5, alpha=0.5)

    # Set identical scales for both axes
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03, family="Bebas Neue")
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0, family="Bebas Neue")

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Create minor ticks placed at each integer to enable drawing of minor grid
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    # Draw a line between two points
    point1 = [x1, y1]
    point2 = [x2, y2]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    resultInput = "A distancia entre ({}, {}) e ({}, {}) é: {:.2f}".format(x1,x2,y1,y2, result)
    plt.title(resultInput, loc ='right', size =15, family="Bebas Neue")
    plt.title("Desenvolvido por: Lucas Zambam", loc='left', size=18, family="Bebas Neue")
    plt.plot(x_values, y_values)

    plt.show()

# Link the buttons to the functions
app.addButtons(["Criar Gráfico"], graphic)
app.addButtons(["Cancelar"], cancel)

# Start the GUI
app.go()
