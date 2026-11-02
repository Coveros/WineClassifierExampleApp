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