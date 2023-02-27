import json
from pathlib import Path
import pandas as pd
from datetime import datetime

def parse_messages(path):
    path_to_messages = path / "messages/inbox"

    # iterate through the inbox
    for fpath in path_to_messages.iterdir():
        fdata = json.load(open(fpath / "message_1.json", "r"))
        messages_df = pd.DataFrame(fdata["messages"])
        messages_df["timetamp"] = messages_df["timestamp_ms"].apply(lambda x: str(datetime.fromtimestamp(x/1000)))
        break
    return messages_df


# if __name__ == "__main__":
path_to_data = Path("../data/Instagram volunteer2 JSON/")

messages_df = parse_messages(path_to_data)

messages_df

messages_df["sender_name"].unique()

messages_df["type"]

print(messages_df[messages_df["type"] == "Share"]["share"][0])
messages_df[messages_df["type"] == "Share"]["share"].apply(lambda x: [v for v in x.values()])

messages_df["is_unsent"]

# only messages of type "Generic" contain content
messages_df[messages_df["type"] == "Generic"]["content"]


