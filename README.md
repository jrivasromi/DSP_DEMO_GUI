# DSP_DEMO_GUI
A GUI used to teach basic concepts of DSP and PCM. This application was made using the PySide6 framework and runs on **Linux and Windows**.

Currently the GUI is SPANISH only as this was a University project.

The comments are in spanglish, sorry for the inconsistency! 

![image](https://github.com/user-attachments/assets/f9aea6b3-975c-428f-bf0e-fbcf0e392c59)

## Running

[uv](https://docs.astral.sh/uv/) is recommended. With uv installed, a single command is all you need — it will set up a virtual environment and install dependencies automatically:

```bash
uv run widget.py
```

Alternatively, using pip:

```bash
pip install PySide6 numpy scipy matplotlib
python widget.py
```

## Building a standalone executable

The project can be compiled into a portable executable using [PyInstaller](https://pyinstaller.org/). Run the following from the project directory on the target platform:

```bash
pyinstaller DSP_SIM.spec
```

> **Note:** PyInstaller cannot cross-compile. You must run this command on each platform (Linux, Windows) to produce its respective executable. The `DSP_SIM.spec` file handles platform differences automatically.
