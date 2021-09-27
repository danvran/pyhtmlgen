# import the html library
from pyhtmlgen import generators as htmlgen
# import other libraries
import numpy as np
import pandas as pd
import plotly.express as px

# create a variable to store the content of the website
# always start the website with the start function
website = htmlgen.start_styled_html("pyhtml test site")

website += htmlgen.h1("pyhtmlgen example")

website += htmlgen.h3("Importing many words from a file is easy and keeps your code clean")

with open("C:/Users/Daniel/Documents/GitHub/pyhtmlgen/examples/intro.txt", 'r') as f:
    data = f.read()
website += htmlgen.para(data)

website += htmlgen.h3("Using MathJax we can insert beautiful formulas")

with open("C:/Users/Daniel/Documents/GitHub/pyhtmlgen/examples/formula.txt", 'r') as f:
    data = f.read()
website += htmlgen.para(data)

website += htmlgen.h3('Plotly objects can be integrated natively')
website += htmlgen.para('You can use the interactive functions of the plot')

# now let's add some data and plot it
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color='petal_length')
fig.update_layout(width=900, height=500)
# when adding a figure to your website, make sure to give it a unique id of type 'id_number'
website += htmlgen.plotly_figure(fig, 'id_01')

# put in a line break
website += htmlgen.line_break()

website += htmlgen.h3("If you want to dislpay some tabular data, that's possible too")

# using pandas
website += htmlgen.para("We can use pandas dataframes...")
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
website += htmlgen.df_as_table(df, size='30')

# put in a line break
website += htmlgen.line_break()

# we can also plot a numpy table with some added colums and rows as headers
website += htmlgen.para("as well as numpy arrays and additional lists for headers and indices")
data = np.array(((1 , 2), (3, 4)))
header = ['A', 'B']
side = ['C', 'D']
website += htmlgen.np_matrix_as_table(data, headers=header, sides=side, size='30')

# put in a line break
website += htmlgen.line_break()


website += htmlgen.h3("Inserting an image can be done using a local or web reference")
# import picture
website += htmlgen.add_link("https://unsplash.com/@alinnnaaaa", "Photo by Alina Grubnyak on Unsplash")
website += htmlgen.line_break()
website += htmlgen.add_image_by_ref("https://images.unsplash.com/photo-1545987796-200677ee1011", "network", "300", "550")

# always close the website with the end function
website += htmlgen.end_styled_html()

# don't forget to save your website to a file
with open('c:/Users/Daniel/OneDrive - Helmut-Schmidt-Universität/Desktop/Testwebsite.html', 'w') as f:
    f.write(website)

print("Finished Script")
