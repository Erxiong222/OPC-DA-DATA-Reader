# Simple OPC DA Datalogger <span style="color:red">(alfa)</span>
Simply desktop application to collect and record sensor values from an [OPC DA](https://en.wikipedia.org/wiki/OPC_Data_Access) server.

## 1) How to use
- Run gui.py
- Choose and connect to an OPC DA server
- Choose which tags you want to record
- Click o Start Logging

## 2) Installation
#### 2.1) Python depedencies
- **[Python 2.7.](https://github.com/python/cpython/tree/2.7)** - I prefer using Python 3, however the OpenOPC library requires Python 2. I installed using conda
- **[Pywin32](https://github.com/mhammond/pywin32)** - I installed using conda
- **[OpenOPC](http://openopc.sourceforge.net/)** - Theoretically it is avaiable o [PyPi](https://pypi.org/project/OpenOPC/), but the installation using 'pip install OpenOPC' didn't worked for me. I had to cloning the repository and install it using 'pip install .'
- **Pyside** and **Qt4** - I installed using conda.

**Note:** For personal use I usually choose pyqt5, however for this little project I wanted to more permissive license.
