# Wine Classifier Example App

This repository includes a Flask web app, a pre-trained wine classifier, and test automation with SeleniumBase.

## Wine Classes

Predictions identify wine types from Piedmont, Italy, not three different regions:

- `0`: Barolo
- `1`: Grignolino
- `2`: Barbera

This mapping was verified by matching all 178 samples across all 13 measurements between [scikit-learn's wine dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset) and the [named ContaminatedMixt dataset](https://cran.r-universe.dev/ContaminatedMixt/data/wine/json). See the [CRAN dataset documentation](https://search.r-project.org/CRAN/refmans/ContaminatedMixt/html/wine.html) for provenance.

## Dependencies

`requirements.txt` is shared by local development, Codespaces, and other VMs. It includes Flask and scikit-learn for the app, and pytest and SeleniumBase for tests. NumPy is installed transitively by scikit-learn. No notebook or kernel packages are required.

The saved model was trained with scikit-learn 1.4.0. Loading it with a different version can produce compatibility warnings; prediction results should be validated before upgrading or deploying with a different version.

## Run On A Local Machine

### Prerequisites

- Install 64-bit [Python](https://www.python.org/downloads/). Python 3.12 is a recommended starting point for this course app; newer versions may have different dependency compatibility. On Windows, enable **Add Python to PATH** if offered, then reopen your terminal and VS Code.
- If using VS Code, install the **Python** extension from Microsoft.
- Download and **extract** the repository ZIP, or clone the repository. Open the project folder containing `wine.py` and `requirements.txt`, not its parent folder. In VS Code, select **Terminal > New Terminal**.

### Windows

Verify python is already installed on your computer:
python --version

If it is not installed, see Prerequisites above for where to go to download python.

After python is installed, type these commands one by one at a terminal command prompt:
python -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe wine.py

If you installed a different Python version, adjust `-3.12` accordingly. If `py` is unavailable but `python --version` reports your installed Python, use `python -m venv .venv` for the first command instead.

### macOS / Linux

Verify python is already installed on your computer:
python3 --version

If it is not installed, see Prerequisites above for where to go to download python.

Run these commands one at a time from the project folder:
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python wine.py

Check that `python3 --version` reports the Python you intend to use. On Ubuntu/Debian, if environment creation reports that `ensurepip` is unavailable, install the matching venv package (usually `sudo apt install python3-venv`), then retry.

### Open And Restart The App

Open http://127.0.0.1:5000 in your browser. Select **Register** to create an account, then log in. The model and SQLite database are included; no external database service is required. Keep `model.pkl` and `wineusers.db` in the project folder, and use a writable local folder.

Stop the server with **Ctrl+C**. For later sessions, open a terminal in the project folder and run only the last command for your operating system. There is no need to recreate the environment or reinstall dependencies each time. Check http://127.0.0.1:5000/health to confirm the server is running.

These commands use the virtual environment directly, so you do not need to activate it or change PowerShell execution policies. Each machine creates its own `.venv`; do not commit, upload, or copy that folder into GitHub, Codespaces, or a VM. Transfer the repository files and install dependencies in the destination environment instead.

### Select The Interpreter In VS Code

After creating `.venv`, open the Command Palette (**Ctrl+Shift+P** on Windows/Linux, **Cmd+Shift+P** on macOS), run **Python: Select Interpreter**, and choose the interpreter inside this project's `.venv`.

If it is not listed, choose **Enter interpreter path** and browse to:

- Windows: `.venv\Scripts\python.exe`
- macOS/Linux: `.venv/bin/python`

The repository's current workspace setting points to a Windows `.venv` interpreter that does not exist until you create it. If VS Code reports an invalid interpreter, explicitly selecting the correct interpreter replaces that selection for your workspace. On macOS/Linux or in Codespaces, do not select the Windows executable path.

## Run With GitHub Codespaces

The repository includes a dev container in `.devcontainer/`.

1. In GitHub, open the repository.
2. Select **Code** > **Codespaces** > **Create codespace on main**.
3. Wait for the container build to complete.

The setup will automatically:

- Install Python dependencies from `requirements.txt`
- Forward the Flask app port (`5000`)

If you already had a Codespace open before this setup changed, rebuild the container so the browser packages are refreshed.

## Start The Flask App

```bash
python wine.py
```

Open the forwarded port `5000` when prompted.

## Run UI Tests

Run tests in headless mode (recommended in Codespaces):

```bash
python -m pytest tests/ -v --browser=chrome --headless --no-sandbox --disable-gpu
```
