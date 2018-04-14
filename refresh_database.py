#!/usr/bin/env python3
import pickle
from neural_network import prepare_database, triplet_loss, who_is_it, DATABASE_PATH

create_notification = False
try:   # only create notification if module present
    from plyer import notification
    create_notification = True
except ModuleNotFoundError:
    pass

"""
Scan the images directory for folders represnting identities.
For each identity folder found load images within the folder and get their encodings (1x128 tensors produced from the inception model)
This creates and in-memory database like: {"name": [tensor1...tensor_n], ...}
The dictionary is then saved as a pickle file to the database directory
"""

if __name__ == "__main__":
    database = prepare_database(use_avg=False)
    with open(DATABASE_PATH, "wb") as f:
        pickle.dump(database, f)
    if create_notification:
        notification.notify(
            title="Database updated",
            message=f"Facial recognition database updated with {len(database)} {'entry' if len(database) == 1 else 'entries'}",
            app_name="Facial Recognition",
            # app_icon='path/to/the/icon.png'
        )
