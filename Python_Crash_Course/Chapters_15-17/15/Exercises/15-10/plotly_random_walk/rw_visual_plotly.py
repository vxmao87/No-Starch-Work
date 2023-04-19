import plotly.express as px

from random_walk import RandomWalk


rw = RandomWalk(50_000)
rw.fill_walk()

fig = px.scatter(rw.x_values, rw.y_values)
fig.update_layout(xaxis_visible=False,
                  xaxis_showticklabels=False,
                  yaxis_visible=False,
                  yaxis_showticklabels=False)
fig.show()