# README

This is a barebones WMTS tile server.  It can serve tiled maps, and has a lightweight web preview of all layers.

## Endpoints

* `hostname`: This is the lightweight Leaftlet viewer for previews and testing tile availability
* `hostname/capabilities`: This should display all tile endpoints available
* `hostname/tiles/mapType/z/x/y`: this is how individual tiles are accessed.  You can get this from `/capabilities`

## Build, configuration and setup

* Building is simple: `docker-compose build`
* There are two small configuration steps in `docker-compose.yml`:
    * Point `volumes` to the location of your tiles directory.
    * Optionally change the number of processes to run (more processes means higher throughput and more simultaneous clients)
    * You may want to change the port the server runs on, depending on what else is running on the host
* `docker-compose up` will run the server, and you can test it by opening up `localhost` on the host machine.  You should see a web-viewer
