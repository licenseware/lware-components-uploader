# Uploader (Beta)

Files uploader registration.
This library is used to register/store information about files that will be uploaded and processed.


## Quickstart

Install this package using the following pip command:
```bash

pip3 install git+https://git@github.com/licenseware/lware-components-uploader.git

```

You can use `git+ssh` if you have ssh keys configured.

Use case:
```py

from uploader import Uploader

UniqueName = Uploader(
    app_id="name-service",
    upload_name="Short description",
    upload_id="UniqueName",
    description="Long description",
    upload_url="/UniqueName/files",
    upload_validation_url='/UniqueName/validation',
    quota_validation_url='/quota/UniqueName',
    status_check_url='/UniqueName/status',
    history_url='/UniqueName/history'
)

response, status_code = UniqueName.register_uploader()

if status_code == 200:
    # uploader registration succeeded

```

The response from `register_uploader` will be a json, status_code tuple.


The following environment variables are expected:
- `APP_BASE_PATH`, `APP_URL_PREFIX`  or `uploads_base_url` parameter filled;     
- `REGISTRY_SERVICE_URL` or `registration_url` parameter filled;
- `AUTH_TOKEN` or `auth_token` parameter filled.


