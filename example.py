from pyhtmlgen import generators as htmlgen

import numpy as np
import plotly.graph_objects as go

website = htmlgen.start("pyhtml test site")

website += htmlgen.h1("This is a title")

website += htmlgen.para("This is a paragraph")

N = 1000
t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))

website += htmlgen.plotly_figure(fig, 'id_01')

with open('Testwebsite.html', 'w') as f:
    f.write(website)

print("Finished Script")
