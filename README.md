# altv-reconnect

# Why?

I'm tired of typing `reconnect` in the alt:V console. This tool is going to do it for me whether it likes it or not.

# Usage

Download the executable from releases and simply run it in the background.

Invoke a HTTP `GET` request for `localhost:5599` to invoke a reconnect.

This will only allow reconnecting from a local Windows Machine that is also running an alt:V Server

# Build from Scratch

Requires pyinstaller

```
pyinstaller --uac-admin --clean --name altv-reconnect --onefile --icon=main.ico main.py 
```