import json
from pathlib import Path
import pandas as pd
from datetime import datetime

def parse_messages(root_path):
    path_to_messages = root_path / "messages/inbox"

    dfs = []
    # iterate through the inbox
    for fpath in path_to_messages.iterdir():
        fdata = json.load(open(fpath / "message_1.json", "r"))
        messages_df = pd.DataFrame(fdata["messages"])
        messages_df["timetamp"] = messages_df["timestamp_ms"].apply(lambda x: str(datetime.fromtimestamp(x/1000)))
        dfs.append(messages_df)

    df = pd.concat(dfs, axis=0).reset_index(drop=True)
    return df

def get_stories_paths(root_path):
    path_to_stories = root_path / "media/stories"
    paths = []
    for fpath in path_to_stories.iterdir():
        date = fpath.name
        for story_path in fpath.iterdir():
            paths.append(str(story_path))

    paths_df = pd.DataFrame(paths, columns=["fpath"])
    paths_df["date_str"] = paths_df["fpath"].str.split("/").str[-2]
    paths_df["timestamp"] = paths_df["date_str"].apply(lambda x: datetime.strptime(x, "%Y%m").timestamp())
    return paths_df

def get_posts_paths(root_path):
    path_to_stories = root_path / "media/posts"
    paths = []
    for fpath in path_to_stories.iterdir():
        date = fpath.name
        for story_path in fpath.iterdir():
            paths.append(str(story_path))

    paths_df = pd.DataFrame(paths, columns=["fpath"])
    paths_df["date_str"] = paths_df["fpath"].str.split("/").str[-2]
    paths_df["timestamp"] = paths_df["date_str"].apply(lambda x: datetime.strptime(x, "%Y%m").timestamp())
    return paths_df
