"""
Check rate limit: https://api.github.com/rate_limit
"""

import requests
import plotly.express as px

# Change this value to other appropriate programming languages!
prog_language = 'Python'

# Makes an API call and checks the response.
url = "https://api.github.com/search/repositories" 
url += f"?q=language:{prog_language.lower()}+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Processes overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Processes repository information.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turns repo names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Builds hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Makes visualization.
title = f"Most Starred {prog_language.title()} Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, 
             y=stars, 
             title=title, 
             labels=labels, 
             hover_name=hover_texts)

fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()