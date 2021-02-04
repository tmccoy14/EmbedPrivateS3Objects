# Embed Private S3 Objects

## Embed Private S3 Objects is a Python Flask application that allows you to fetch an image or video that is stored within a private S3 bucket and embeds it into your web application.

### Prerequisites

- Create a private S3 bucket within your AWS Account
- Upload an image or video to the newly created S3 bucket
- Configure environment variables for you AWS Account credentials
- Update the newly created S3 bucket name in the `app.py` file

### Run Application

```sh
$ python3 -m venv env

$ source env/bin/activate

$ pip install -r requirements.txt

$ python app.py
```
