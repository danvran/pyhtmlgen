# import the html library
from pyhtmlgen import generators as htmlgen
# import other libraries
import numpy as np
import plotly.express as px

# create a variable to store the content of the website
# always start the website with the start function
website = htmlgen.start_styled_html("pyhtml test site")

website += htmlgen.h1("pyhtmlgen example")

website += htmlgen.h3("Importing many words from a file is easy and keeps your code clean")

with open("C:/Users/Daniel/Documents/GitHub/pyhtmlgen/examples/lorem.txt", 'r') as f:
    data = f.read()
website += htmlgen.para(data)

website += htmlgen.h3("With MathJax we can insert beautiful formulas")

with open("C:/Users/Daniel/Documents/GitHub/pyhtmlgen/examples/formula.txt", 'r') as f:
    data = f.read()
website += htmlgen.para(data)

website += htmlgen.h3("Look at this cool interactive plot below")

# now let's add some data and plot it
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color='petal_length')
fig.update_layout(width=900, height=500)
# when adding a figure to your website, make sure to give it a unique id of type 'id_number'
website += htmlgen.plotly_figure(fig, 'id_01')

# put in a line break
website += htmlgen.line_break()

website += htmlgen.h3("If you want to dislpay some tabular data, that's possible too")

# we can also plot a table
data = np.array(((1 , 2), (3, 4)))
header = ['A', 'B']
side = ['C', 'D']
website += htmlgen.np_matrix_as_table(data, headers=header, sides=side, size='30')

# put in a line break
website += htmlgen.line_break()


website += htmlgen.h3("Inserting an image can be done using a local or web reference")
# import picture
website += htmlgen.add_image_by_ref("https://i.redd.it/11lfx3pm4jv41.jpg", "potato", "300", "600")

# always close the website with the end function
website += htmlgen.end_styled_html()

# don't forget to save your website to a file
with open('c:/Users/Daniel/OneDrive - Helmut-Schmidt-Universität/Desktop/Testwebsite.html', 'w') as f:
    f.write(website)

print("Finished Script")
