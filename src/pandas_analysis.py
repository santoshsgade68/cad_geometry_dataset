"""
pandas_analysis.py

Pandas-based analysis of the CAD dataset
"""
import pandas as pd

def print_dataset_summary(df: pd.DataFrame):
    """
    Print basic dataset information
    """

    print("\n======================================")
    print("CAD DATASET SUMMARY")
    print("========================================")

    print(f"Number of features : {len(df)}")
    print(f"Number of columns : {len(df.columns)}")

    print("\nColumns:")
    print(list(df.columns))

def print_feature_counts(df: pd.DataFrame):
    """
    Count CAD features by feature type
    """
    print("\n=====================================")
    print("FEATURE TYPE COUNTS")
    print("=======================================")

    counts = df["feature_type"].value_counts()

    print(counts)

def print_geometry_counts(df : pd.DataFrame):
    """"
    Count CAD features by geometry types
    """
    print("\n=====================================")
    print("GEOMETRY TYPE COUNTS")
    print("=======================================")

    counts = df["geometry_type"].value_counts()

    print(counts)

def print_numeric_statistics(df: pd.DataFrame):
    """
    Display statistical information for numeric columns.
    """
    print("\n=====================================")
    print("NUMERIC STATISTICS")
    print("=======================================")

    numeric_columns = [
        "radius",
        "diameter",
        "height",
        "volume",
        "surface_area",
        "aspect_ratio",
        "distance_from_origin",
        "distance_from_centroid",
    ]

    available_columns = [column for column in numeric_columns if column in df.columns]
    missing_columns = [column for column in numeric_columns if column not in df.columns]

    if missing_columns:
        print(f"Columns not found: {missing_columns}")

    if available_columns:
        print(df[available_columns].describe())
    else:
        print("No requested numeric columns are available.")

    #print(df[numeric_columns].describe())

def group_by_feature_type(df: pd.DataFrame):
    """
    Calculate statistics grouped by feature type.
    """

    result = (
        df.groupby("feature_type")
        .agg(
            feature_count = ("feature_id", "count"),
            average_radius = ("radius", "mean"),
            average_height = ("height", "mean"),
            total_volume = ("volume", "sum"),
            average_aspect_ratio = ("aspect_ratio", "mean"),
        )
        .reset_index()
    )

    return result

def find_largest_features(df: pd.DataFrame, count=5):
    """
    Return features with the largest calculated volume
    """
    return (
        df.sort_values(
            by = "volume",
            ascending=False
        )
        .head(count)
    )

