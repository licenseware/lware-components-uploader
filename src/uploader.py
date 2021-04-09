import logging
import os
import requests


class Uploader:

    def __init__(
        self,
        app_id,
        upload_name,
        upload_id,
        description,
        upload_url,
        upload_validation_url,
        status_check_url,
        quota_validation_url,
        history_url,
        status="Idle",
        icon="default.png"
    ):

        self.app_id = app_id
        self.upload_name = upload_name
        self.upload_id = upload_id
        self.description = description
        self.upload_url = upload_url
        self.upload_validation_url = upload_validation_url
        self.quota_validation_url = quota_validation_url
        self.status_check_url = status_check_url
        self.history_url = history_url
        self.root_url = os.getenv("APP_BASE_PATH") + os.getenv("APP_URL_PREFIX") + '/uploads'
        self.status = status
        self.icon = icon


    def register_uploader(self):

        if 'true' not in os.getenv('APP_AUTHENTICATED', 'false'):
            logging.warning('Uploader not registered, no auth token available')
            return False


        payload = {
            'data': [{
                "app_id": self.app_id,
                "upload_name": self.upload_name,
                "upload_id": self.upload_id,
                "description": self.description,
                "upload_url": self.root_url + self.upload_url,
                "upload_validation_url": self.root_url + self.upload_validation_url,
                "quota_validation_url": self.root_url + self.quota_validation_url,
                "status_check_url": self.root_url + self.status_check_url,
                "history_url": self.root_url + self.history_url,
                "status": self.status,
                "icon": self.icon,
            }]
        }

        logging.warning(payload)

        url = f'{os.getenv("REGISTRY_SERVICE_URL")}/uploaders'
        
        headers = {
            "Authorization": os.getenv('AUTH_TOKEN'), 
            "TenantId": os.getenv('AUTH_TENANT_ID'),
            "Accept": "application/json"
        }
        
        registration = requests.post(url, json=payload, headers=headers)

        logging.warning(registration.content)

        if registration.status_code == 200:
            logging.warning("Uploader register successfully!")
            return payload
        else:
            logging.warning("Could not register uploader")
            return False
    