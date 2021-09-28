import matplotlib.pyplot as plt


# Colored boxplot ability taken from link below
# https://stackoverflow.com/questions/41997493/python-matplotlib-boxplot-color


def box_plot(data, edge_color, fill_color):
    bp = ax.boxplot(data, patch_artist=True)

    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color=edge_color)

    for patch in bp['boxes']:
        patch.set(facecolor=fill_color)

    return bp


example_data1 = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 24]

fig, ax = plt.subplots()
bp1 = box_plot(example_data1, 'blue', 'cyan')
# ax.legend([bp1["boxes"][0]], ['Data 1'])
# plt.savefig("boxplot_image")
plt.show()

exit(0)
