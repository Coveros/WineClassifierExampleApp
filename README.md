# Wine Classifier Example App

This repository includes a Flask web app, a pre-trained wine classifier, and test automation with SeleniumBase.

## Dependencies

`requirements.txt` is shared by local development, Codespaces, and other VMs. It includes Flask and scikit-learn for the app, and pytest and SeleniumBase for tests. NumPy is installed transitively by scikit-learn. No notebook or kernel packages are required.

The saved model was trained with scikit-learn 1.4.0. Loading it with a different version can produce compatibility warnings; prediction results should be validated before upgrading or deploying with a different version.

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