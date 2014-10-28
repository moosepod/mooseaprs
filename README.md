mooseweather
============

Little web-based weather app for home use.

The basic concept: I run an APRS client at home, and I'd like to pull the weather off several local weather stations to 
display on a web page. 

The architecture:
- A static HTML page pulls down data from a (fixed) Firebase URL and displays it
- A python script runs on the linux box and checks the Xastir log for changes, then pushes them to Firebase.

That's pretty much it!
