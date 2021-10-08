# Import the Necessary Libraries
import matplotlib.pyplot as plt

circles = []
red_points = [(5, 5), (4.5, 5), (4.5, 4.5), (5.5, 5), (5.5, 5.5), (5, 4.5)]
orange_points = [(6.1, 6.1), (4, 4)]
blue_points = [(8, 8), (8, 2), (3, 3), (1, 4), (2, 8)]

for point in red_points:
    circles.append(plt.Circle(point, 1, color="red", fill=False))
for point in orange_points:
    circles.append(plt.Circle(point, 1, color="orange", fill=False))
for point in blue_points:
    circles.append(plt.Circle(point, 1, color="blue", fill=False))

ax = plt.gca()
ax.cla()  # clear things for fresh plot

# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))
# some data
# ax.plot(range(11), 'o', color='black')
# # key data point that we are encircling
# ax.plot((5), (5), 'o', color='y')
x_red = []
y_red = []
for point in red_points:
    x_red.append(point[0])
    y_red.append(point[1])

x_orange = []
y_orange = []
for point in orange_points:
    x_orange.append(point[0])
    y_orange.append(point[1])

x_blue = []
y_blue = []
for point in blue_points:
    x_blue.append(point[0])
    y_blue.append(point[1])

ax.scatter(x_red, y_red, color="red", label="Core Point")
ax.scatter(x_orange, y_orange, color="orange", label="Border Point")
ax.scatter(x_blue, y_blue, color="blue", label="Outlier")

for circle in circles:
    ax.add_patch(circle)

plt.legend()
plt.title("DBSCAN Cluster Creation Process")
plt.xlabel("Data X Value")
plt.ylabel("Data Y Value")
plt.savefig("./paper_images/DBSCAN_clustering_process.png", dpi=500)
plt.show()

exit(0)
