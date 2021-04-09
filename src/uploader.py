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
        icon="default.png",
        registration_url=None,
        auth_token=None,
        auth_tenant_id=None
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
    
        self.registration_url = registration_url or f'{os.getenv("REGISTRY_SERVICE_URL")}/uploaders'
        self.auth_token = auth_token or os.getenv('AUTH_TOKEN')
        self.auth_tenant_id = auth_tenant_id or os.getenv('AUTH_TENANT_ID')


    def register_uploader(self):

        if 'true' != os.getenv('APP_AUTHENTICATED'):
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
        

        headers = {
            "Authorization": self.auth_token, 
            "TenantId": self.auth_tenant_id
        }
        
        registration = requests.post(url=self.registration_url, json=payload, headers=headers)

        logging.warning(registration.content)

        if registration.status_code == 200:
            logging.warning("Uploader register successfully!")
            return payload
        else:
            logging.warning("Could not register uploader")
            return False
    