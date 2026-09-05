from celery import shared_task
import time

@shared_task
def send_otp_code(phone,otp_code):
    # connect to sms panel api
    print(f'Phone : {phone} | OTP code : {otp_code}')
    time.sleep(2)
    return f'OTP Code {otp_code} sent to {phone}'