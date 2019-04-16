# MyGreenCar Server

#### Quick Start Guide

MyGreenCar requires Flask, which can be installed with pip
```sh
$ pip install Flask
```
To start the server on your computer, run
```sh
$ python wallflower_pico_server.py
```
Open a web browser and navigate to http://127.0.0.1:5000/ to view the interactive dashboard. By default, the server will also be publically available on your network and accessible via the IP address of your computer (i.e. http://IP_ADDRESS:5000/).



#### License

The source code is licensed under the [AGPL v3][agpl]. You can find a reference to this license at the top of each source code file.

Components which connect to the server via the API are not affected by the AGPL. This extends to the Python example code and the HTML, JS, and CSS code of the web interface, which are licensed under the [MIT license][mit].

In summary, any modifications to the source code must be distributed according to the terms of the AGPL v3. Any code that connects to the server via an API is recognized as a seperate work (not a derivative work) irrespective of where it runs. Lastly, you are free to modify the HTML, JS, and CSS code of the web interface without restrictions, though we would appreciate you sharing what you have created.

[mit]: <https://opensource.org/licenses/MIT>
[agpl]: <https://opensource.org/licenses/AGPL-3.0>

#### Reference & Credit:
CE 186 taught by Scott Moura, UC berkeley
