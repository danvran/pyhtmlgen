import pyhtml

import numpy as np
import plotly.graph_objects as go

website = pyhtml.start("pyhtml test site")

website += pyhtml.h1("This is a title")

website += pyhtml.para("This is a paragraph")

N = 1000
t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))

website += pyhtml.plotly_figure(fig, 'id_01')

with open('Testwebsite.html', 'w') as f:
    f.write(website)

print("Finished Script")
