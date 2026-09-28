"""
visualization.py

Matplotlib visualization for CAD geometry data.
"""
import matplotlib.pyplot as plt

def plot_3d_features(df):
    """
    Plot CAD feature locations in 3D.
    """

    fig = plt.figure(figsize=(10, 7))

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    scatter = ax.scatter(
        df["x"],
        df["y"],
        df["z"],
        s=df["diameter"]*5,
        alpha=0.8
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title(
        "CAD Feature Distribution"
    )

    plt.tight_layout()
    plt.show()

def plot_feature_volume(df):
    """
    Plot calculated feature volume
    """
    plt.figure(figsize=(10, 6))

    plt.bar(
        df["feature_id"].astype(str),
        df["volume"]
    )

    plt.xlabel("Feature_ID")
    plt.ylabel("Volume")
    plt.title("Calculated CAD Feature Volume")

    plt.tight_layout()
    plt.show()

def plot_aspect_ratio(df):
    """
    Plot feature aspect ratios.
    """

    plt.figure(figsize=(10, 6))

    plt.bar(
        df["feature_id"].astype(str),
        df["aspect_ratio"]
    )

    plt.xlabel("Feature ID")
    plt.ylabel("Aspect Ratio")
    plt.title("CAD Feature Aspect Ratio")

    plt.tight_layout()
    plt.show()

    


