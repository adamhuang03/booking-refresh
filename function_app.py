import logging
import azure.functions as func
import requests
import json

from utils.constants.req_bodies import booking, update, cancel 
from utils.constants.urls import base_url
from utils.functions import orchestrator_responder

app = func.FunctionApp()

@app.schedule(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    try:
        
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