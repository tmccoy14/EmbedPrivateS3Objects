from flask import Flask, render_template
import boto3
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        "Navigate to /<resource> to see embedded image pulled from private s3 bucket!"
    )


@app.route("/<resource>")
def download_image(resource):
    """ resource: name of the file to download"""
    s3Client = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )
    url = s3Client.generate_presigned_url(
        "get_object",
        Params={"Bucket": "object-storage-auth", "Key": resource},
        ExpiresIn=100,
    )
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
