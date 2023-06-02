from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()


class PaymentInfo(BaseModel):
    type: Optional[str]
    data: Optional[str]
    is_subscription_payment: bool = False
    is_first_subscription_payment: bool = False
    tier_name: Optional[str]
    shop_items: Optional[list]
    email: Optional[str]

@app.post("/webhook")
async def webhook(data: str = Form(...)):
    # Parse the 'data' field as a JSON string
    print(type(data))
    print(data)
    try:
        payment_info = PaymentInfo(**json.loads(data))
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON data")

    # Access the payment information
    payment_type = payment_info.type
    is_subscription_payment = payment_info.is_subscription_payment
    is_first_subscription_payment = payment_info.is_first_subscription_payment
    tier_name = payment_info.tier_name
    shop_items = payment_info.shop_items

    # Perform your logic based on the payment information
    # ...
    # Your code here
    print(payment_info.email)
    # Return a 200 status code to indicate successful processing
    return {"message": "Webhook received"}

