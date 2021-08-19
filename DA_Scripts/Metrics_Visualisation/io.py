import matplotlib.pyplot as plt
import numpy as np


labels = ['Half', 'Default','Double']
men_means = [376.7, 328, 461.7]
women_means = [175, 263.5, 316.8]

x = np.arange(len(labels))  # the label locations
width = 0.40  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Input_Rate',color='green')
rects2 = ax.bar(x + width/2, women_means, width, label='Output_Rate')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time in Seconds')
ax.set_title('Network I/O')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
fig.set_size_inches(12, 8)
plt.show()
fig.savefig("io.png")
