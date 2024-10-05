import logging
import azure.functions as func
import requests
import json
import datetime

from utils.constants.req_bodies import booking, update, cancel 
from utils.constants.urls import base_url
from utils.functions import orchestrator_responder
logging.basicConfig(level=logging.INFO)

app = func.FunctionApp()

@app.function_name(name="mytimer")
@app.schedule(schedule="0 */20 * * * *", arg_name="mytimer", run_on_startup=True) 
def timer_function(mytimer: func.TimerRequest) -> None:
    # utc_timestamp = datetime.datetime.utcnow().replace(
    #     tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')

    # logging.info('Python timer trigger function ran at %s', utc_timestamp)

    try:
        logging.info('Test')
        
        booking_response = requests.post(
            url=base_url,
            data=json.dumps(booking)
        )
        logging.info(orchestrator_responder(booking_response.status_code))
        update_response = requests.post(
            url=base_url,
            data=json.dumps(update)
        )
        logging.info(orchestrator_responder(update_response.status_code))
        cancel_response = requests.post(
            url=base_url,
            data=json.dumps(cancel)
        )
        logging.info(orchestrator_responder(cancel_response.status_code))

    except requests.exceptions.RequestException as e:
        logging.info(f"Error with initialization: {e}")