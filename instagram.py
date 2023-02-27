import json
from pathlib import Path
import pandas as pd
from datetime import datetime

def parse_messages(path):
    path_to_messages = path / "messages/inbox"

    dfs = []
    # iterate through the inbox
    for fpath in path_to_messages.iterdir():
        fdata = json.load(open(fpath / "message_1.json", "r"))
        messages_df = pd.DataFrame(fdata["messages"])
        messages_df["timetamp"] = messages_df["timestamp_ms"].apply(lambda x: str(datetime.fromtimestamp(x/1000)))
        dfs.append(messages_df)

    df = pd.concat(dfs, axis=0).reset_index(drop=True)
    return df
