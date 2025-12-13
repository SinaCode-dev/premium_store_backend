from celery import shared_task
from kavenegar import KavenegarAPI
from django.conf import settings

@shared_task
def send_sms_task(phone, message):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params = {
            'sender': settings.KAVENEGAR_SENDER,
            'receptor': str(phone),
            'message': message
        }
        response = api.sms_send(params)
        print("SMS sent via Celery:", response)
        return {"status": "success", "response": response}
    except Exception as e:
        print("SMS error in Celery:", str(e))
        return {"status": "error", "message": str(e)}