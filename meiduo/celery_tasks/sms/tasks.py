from libs.yuntongxun.sms import CCP
from celery_tasks.main import app

@app.task
def celery_send_sms_code(moblie,code):

    CCP().send_template_sms(moblie,[code,5],1)