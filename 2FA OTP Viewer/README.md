
You can ditch your 2FA app (Google Authenticator, LastPass etc) with Termux and this script.

# Before using
- Install [Termux:API](https://wiki.termux.com/wiki/Termux:API) and [Termux:Widget](https://wiki.termux.com/wiki/Termux:Widget) app from [Google Play Store](https://play.google.com/store/apps/details?id=com.termux.api&hl=en) or [f-droid](https://f-droid.org/en/packages/com.termux.api/). Termux, Termux:API and Termux-Widget, all the apps should be downloaded from same source (either Google Play Store or f-droid). [Why?](https://wiki.termux.com/wiki/FAQ#Why_does_Termux_not_support_more_special_buttons.3F)
- Give necessary permissions to Termux and Termux:API (i.e. Storage).
- Install package for Termux:API and Python3: `apt install termux-api python`
- Install onetimepass: `pip install onetimepass`
- Create a directory like this: `~/.shortcuts/tasks`
- Copy `main.py` file to the directory.
- Open `main.py` with nano (`nano main.py`) and add directory for files containing 2FA token.
- Make this script executable: `chmod +x main.py`
- Tap and hold on you Homepage (I mean, on the Launcher home page or desktop, whatever you call it), tap on **Widgets**, add widget of Termux:Widget. A new activity will be opened. Navigate to your script.

And your launcher for 2FA OTP Viewer is created. Now tap on the launcher to use it. :-D
