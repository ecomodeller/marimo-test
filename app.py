import marimo

__generated_with = "0.8.15"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""# Kmeans demo""")
    return


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    return mo, plt


@app.cell
def __():
    from sklearn.datasets import make_blobs
    return make_blobs,


@app.cell
def __(mo):
    std = mo.ui.slider(0.1, 2.0,step=0.1)
    mo.md(f"Std: {std}")
    return std,


@app.cell
def __(make_blobs, std):
    X,y = make_blobs(centers=[(0,0), (9,7), (-5,-5)], cluster_std=std.value)
    return X, y


@app.cell
def __(mo):
    nc = mo.ui.slider(2,5)
    mo.md(f"n clusters: {nc}")
    return nc,


@app.cell
def __(X, nc):
    from sklearn.cluster import KMeans

    km = KMeans(nc.value)

    ypred = km.fit_predict(X)
    return KMeans, km, ypred


@app.cell
def __(X, nc, plt, ypred):
    plt.scatter(X[:,0],X[:,1],c=ypred)
    plt.title(f"Kmeans (k={nc.value})")
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.gca()
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
