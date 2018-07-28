# FacebookGraphApi
A small project where I play around with Facebook's graph api.

## Connect.py
This script contains functions to get FB token or graph.

## Group.py
This script contains a function called 
`get_group_post_attachments` that looks into a facebook group
specified by the ID in the config.py file and it returns a 
list containing all the posts with a video. This function can 
be used to check whether in a group a video has been posted in
a given period. This is a functionality currently missing in 
Facebook.

## Whatsapp.py
This script contains a function to send a message on Whatsapp.
Specifically, it is used to send a message to the FB Group owner
whenever a video is posted in a group.
