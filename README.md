# To run the dev branch locally

**Note** Assumed that you are inside the `src` folder of the `dev-branch`.

Your pwd should look like this `.../src/`

1. **Install Poetry**

```bash
# Install the poetry package
pip install poetry
```

2. **Install all the dependencies**

```bash
# Poetry installs all the required dependencies
poetry install
```

3. **Run the module**

```bash
# to run the "recommender" module
python -m recommender "Attention mechanism, gpt"

# to run the "user" module
python -m user "Attention mechanism, gpt"
```

4. **Expected Output**

```bash
[(40, 0.07523317245996379), (30, 0.0645704279199833), (68, 0.019730676950393673), (66, 0.01706847010186102), (88, 0.01676402091510068), (9, 0.015864706383126106), (5, 0.012539847098876067), (2, 0.011670485300686375), (84, 0.009874931918079605), (51, 0.009075828413454008)]
```

```bash
(40, 0.07523317245996379)
```

- `Index 0 i.e 40:` Index of the document.
- `Index 1 i.e 0.075:` Similarity score of the `query` wrt to the `document` at that position.
