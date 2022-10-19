**macOS Monterey version 12.4**<br>
**Python 3.11.0rc2**


1. Download Python (version 3.11) from official site:
[https://www.python.org/downloads/release/python-3110rc2/](https://www.python.org/downloads/release/python-3110rc2/).<br>
Install Python 3.11.

2. In terminal run command:<br>
```
/Applications/Python\ 3.11/Install\ Certificates.command
```

3. In the directory containing files *ultraviolence.py* and *requirements.txt*, create python3.11 virtual environment:<br>
```
python3.11 -m venv .venv
```

4. Activate python3.11 virtual environment *.venv*:<br>
```
source ./.venv/bin/activate
```

5. Install all required packages:<br>
```
pip install -r requirements.txt
```

6. Using any text editor, edit file *.venv_test/lib/python3.11/site-packages/pandas/core/frame.py*<br>

    Find the following lines and comment them (add '#' in the beginning):<br>

>\# GH47215<br>
>\#if index is not None and isinstance(index, set):<br>
>\#    raise ValueError("index cannot be a set")<br>


7. Run script:<br>
```
python ultraviolence.py
```

8. In the end, deactivate virtual environment *.venv*:<br>
```
deactivate
```
