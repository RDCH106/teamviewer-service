# TeamViewer Service

Service to launch TeamViewer Remote Desktop

---------------------

### Installation

You can install from source with:

``` bash
$ git clone https://github.com/RDCH106/teamviewer-service.git --recursive
$ cd teamviewer-service
$ pip install -r requirements.txt
```

---------------------

### Service start-up

Execute TeamViewer service with:

``` bash
$ cd teamviewer-service/teamviewerservice
$ python gateway_main.py
```

In the first execution default config.json will be created in the working directory:

``` bash
Error loading config.json!

Default config.json generated! Try again.
```

👁️[*Check Configure tv_config.jon*](#configure-tv_configjon)

👁️[*Check Change Linkero adminSecret*](#change-linkero-adminsecret)

Running again the service will start to work:

``` bash
$ python gateway_main.py
```

---------------------

### Configuration

#### Configure tv_config.jon

Create `tv_config.jon` file in `config` with this content:

```
{"tv_path": "C:/path/to/teamviewer/TeamViewer.exe"}
```

where `tv_path` is the path to TeamViewer excutable. You can use **TiemViewer portable version without installation** for this purpose.

#### Change Linkero *adminSecret*

Change Linkero *adminSecret* typing the followings command:

```
python -c 'from linkero.tools.passwordHashGenerator import generatePasswordHash; generatePasswordHash()'
```

Introduce desired password and push enter. The password hash will be print in the following line in blue color. Copy the password hash to `config.json` in `config` folder. Search default *adminSecret*:

`$5$rounds=549561$kWqFvPNTcBsl.Kle$ONikf.BJtqKKFTZbUtVmwZn0nDdwrsHhjyqgxRlUNw4`

And replace it by your generated password hash.

#### Change Linkero user

Execute the following python code with `gateway_main.py` running:

```py
from requests import post

post ('http://localhost:5000/api/users', data={"username":"myuser","password":"mypassword","secret":"myadminSecret"})
```

where "*http://localhost:5000/api/users*" is the local endpoint, "*myuser*" is the username for the new user, "*mypassword*" is the password for the new user and "*myadminSecret*" is the adminSecret introduced in [Change Linkero *adminSecret*](#change-linkero-adminsecret) section.

If everything is correct, the post will return `<Response [201]` where code `201` indicates the correct creation of the user.
