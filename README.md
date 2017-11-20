# TeamViewer Service

![logo](http://ingran.es:8081/uploads/project/avatar/37/teamviewer-icon.png)

Service to launch TeamViewer Remote Desktop

### Installation

You can install from source with:

``` bash
$ git clone http://ingran.es:8081/rdcelis/teamviewer-service.git --recursive
$ cd teamviewer-service
$ pip install -r requirements.txt
```

### Service start-up

Execute UDP Commander with:

``` bash
$ cd teamviewer-service/tieamviewerservice
$ python gateway_main.py
```

In the first execution default config.json will be created in the working directory:

``` bash
Error loading config.json!

Default config.json generated! Try again.
```

Running again the service will start to work:

``` bash
$ python gateway_main.py
```