from operator import itemgetter

import requests
import plotly.express as px


# Makes an API call and checks the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Processes information about each submission.
submission_ids = r.json()
print(len(submission_ids))

article_links, comment_counts, hover_texts = [], [], []
for submission_id in submission_ids[39:50]:
    # Makes a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        title = response_dict['title']
        hn_link = f"https://news.ycombinator.com/item?id={submission_id}"
        comment_count = response_dict['descendants']
        owner = response_dict['by']
    except KeyError:
        print(f"Missing data for id {submission_id}")
    else:
        article_link = f"<a href='{hn_link}'>{title}</a>"
        article_links.append(article_link)
        comment_counts.append(comment_count)
        hover_text = f"By {owner}"
        hover_texts.append(hover_text)

plot_title = "Most Comments in Recent Hacker News Articles"
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=article_links,
             y=comment_counts,
             title=plot_title,
             labels=labels,
             hover_name=hover_texts)

fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()