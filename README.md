# EarthBack (Earth Landscape Backgrounds)
System to load new images to be set as the desktop background, selecting based on machine learning (Windows support only).

## Goals for this Project
* extract images from subreddit [DONE]
* ML model to detect which images are preferable (trained supervised)
* ML model to extract the name/description of the image
* ML model to regress a better fitting box around the image (most images from r/EarthPorn are in portrait orientation for some reason)

These 3 models can likely be combined into a single model trained with a multi-task loss.
