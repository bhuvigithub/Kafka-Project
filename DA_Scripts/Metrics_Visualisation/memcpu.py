import matplotlib.pyplot as plt
import numpy as np


labels = ['Half', 'Default','Double']
men_means = [0.2, 0.61, 0.46]
women_means = [0.144, 0.155, 0.149]

x = np.arange(len(labels))  # the label locations
width = 0.40  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Memory_Usage',color='cyan')
rects2 = ax.bar(x + width/2, women_means, width, label='CPU_Usage')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time in Seconds')
ax.set_title('Utilisation')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
fig.set_size_inches(12, 8)
plt.show()
fig.savefig("memcpu.png")
