# altv-reconnect

# Why?

I'm tired of typing `reconnect` in the alt:V console. This tool is going to do it for me whether it likes it or not.

# Usage

Download the executable from releases and simply run it in the background.

Invoke a HTTP `GET` request for `localhost:5599` to invoke a reconnect. (Example Below)

This will only allow reconnecting from a local Windows Machine that is also running an alt:V Server

**Append to your altv.cfg**

These must be added to your client configuration for this to work:

```
debug: 'true'
useExternalConsole: 'true'
```

**Append to your Game Mode**

Add and call `ReconnectHelper.invoke()` after your game mode loads to invoke a local reconnection.

```ts
import * as alt from 'alt-server';
import * as http from 'http';

const RECONNECTION_ADDRESS = 'http://localhost:5599';
let caughtErrorOnce = false;

export class ReconnectHelper {
    static invoke() {

        if (!ReconnectHelper.isWindows()) {
            return;
        }

        ReconnectHelper.sendRequest();
    }

    private static isWindows() {
        return process.platform.includes('win');
    }

    private static sendRequest() {
        const req = http.get(RECONNECTION_ADDRESS);
        req.on('response', () => {
            alt.log(`~g~[altv-reconnect] Invoked Reconnection Successfully`);
        });

        req.on('error', () => {
            if (caughtErrorOnce) {
                return;
            }

            caughtErrorOnce = true;
            alt.log(`~r~[altv-reconnect] ~y~Not Currently Running`);
            alt.log(`~r~[altv-reconnect] ~y~Download Binaries from https://github.com/Stuyk/altv-reconnect`);
        });
    }
}
```

# Building from Scratch

Requires pyinstaller

```
pyinstaller --clean --name altv-reconnect --onefile --icon=main.ico src/altv-reconnect.py 
```
