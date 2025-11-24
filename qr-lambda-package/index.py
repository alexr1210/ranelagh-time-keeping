import json
import uuid
import base64
import boto3
import os
from io import BytesIO

import qrcode
from qrcode.image.pil import PilImage  # Use Pillow explicitly

# Initialize S3 client
s3 = boto3.client("s3")

# Environment variables
BUCKET_NAME = os.environ.get("BUCKET_NAME", "ranelagh-results-csv2")
UPLOAD_PREFIX = os.environ.get("UPLOAD_PREFIX", "uploads/")

def generate_qr_png(data: str) -> str:
    """
    Generates a QR code PNG using Pillow and returns it as base64 string.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Use Pillow image factory
    img = qr.make_image(image_factory=PilImage, fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer)  # Pillow handles PNG format automatically
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def lambda_handler(event, context):
    """
    Lambda entry point: generates a unique token, a pre-signed S3 PUT URL,
    and a QR code representing the token.
    """
    # Unique token for this upload
    token = str(uuid.uuid4())
    object_key = f"{UPLOAD_PREFIX}{token}.csv"

    # Generate pre-signed URL for S3 PUT
    presigned_url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": object_key,
            "ContentType": "text/csv"
        },
        ExpiresIn=300  # 5 minutes
    )

    # Generate QR code as base64
    qr_png_b64 = generate_qr_png(token)

    # Return response
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "token": token,
            "upload_url": presigned_url,
            "s3_key": object_key,
            "qr_png_base64": qr_png_b64
        })
    }
