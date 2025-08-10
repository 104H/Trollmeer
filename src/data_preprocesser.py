import os
import re
import json
import yaml

preprocessed_data = {
    "day" : [],
    "month" : [],
    "year" : [],
    "hour" : [],
    "minute" : [],
    "message" : [],
}

# obtain data source and friend's name from config
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

    data_src = config["DATA_SRC"]
    friends_name = config["FRIEND"]

# traverse file by line
with open(data_src) as data:
    # read a line
    for line in data:
        # if this message was sent by the friend we want to train on
        # filter by `in` because it is faster than regex
        if friends_name in line:
            # extract date and message using regex
            
            # whatsapp format
            # [DD.MM.YY, HH:MM:SS] ~ SENDER_NAME: MSG
            pattern = r"(\d{2})\.(\d{2})\.(\d{2}), (\d{2}):(\d{2}).+\: (.+)"
            matched_data = re.search(pattern, line)

            try:
                preprocessed_data["day"].append( matched_data.group(1) )
                preprocessed_data["month"].append( matched_data.group(2) )
                preprocessed_data["year"].append( matched_data.group(3) )
                preprocessed_data["hour"].append( matched_data.group(4) )
                preprocessed_data["minute"].append( matched_data.group(5) )
                preprocessed_data["message"].append( matched_data.group(6) )
            except:
                pass

with open(config["PREPROCESSED_DATA_DEST"], "w") as file:
    json.dump(preprocessed_data, file, indent=4)