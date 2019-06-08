# CALDERA plugin: Proxy

This plugin contains:

* Reverse proxy rendering for the Caldera App
* Launching reverse proxy service on the local system

The Proxy plugin provides TLS/SSL termination and reverse proxying service for the Sandcat agents/web services. The 
proxying service will ensure that sandcat agents render correctly to the reverse proxy external IP and port.

## Usage

Load the UI and fill out the required input values:
* **Proxy type:** Available proxy configuration templates built into caldera
* **Path to certificate:** Provide an absolute path to a PEM file that contains the server public certificate and key
* **HTTP Port:** Provide an HTTP port that the proxy should listen on
* **HTTPS Port:** Provide an HTTPS port that the proxy should listen on
* **Caldera IP:** Provide the redirect IP address of the caldera server
* **Caldera Port:** Provide the redirect port that the caldera server is listening on 
* **Launch Proxy:** Choose to either just render the Reverse Proxy configuration or render the configuration, then launch an
instance of the desired proxy on the local system 