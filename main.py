"""
main.py

Main execution pipeline for the
CAD Geometry Dataset Processor.

Pipeline:

CAD feature data
       ↓
NumPy calculations
       ↓
Feature engineering
       ↓
Pandas analysis
       ↓
Matplotlib visualization
       ↓
CSV output
"""

import os

from src.geometry_data import create_cad_dataset

from src.numpy_analysis import (
    calculate_bounding_box,
    calculate_centroid,
    add_numpy_calculations,
)

from src.feature_engineering import (
    add_derived_features,
)

from src.pandas_analysis import (
    print_dataset_summary,
    print_feature_counts,
    print_geometry_counts,
    print_numeric_statistics,
    group_by_feature_type,
    find_largest_features,
)

from src.visualization import (
    plot_3d_features,
    plot_feature_volume,
    plot_aspect_ratio,
)

def main():

    print("\n")
    print("=====================================")
    print("CAD GEOMETRY DATASET PROCESSOR")
    print("=====================================")

    #--------------------------------------------
    # STEP 1
    # Create raw CAD dataset
    # #------------------------------------------

    df = create_cad_dataset()

    print("\nRaw CAD dataset:")
    print(df)

    #--------------------------------------------
    # STEP 2
    # NumPy calculations
    #--------------------------------------------

    bounding_box = calculate_bounding_box(df)

    centroid = calculate_centroid(df)

    print("\n===================================")
    print("BOUNDING BOX")
    print("=====================================")

    for key, value in bounding_box.items():
        print(f"{key:10s}: {value:.3f}")

    print("\n===================================")
    print("CENTROID")
    print("=====================================")

    print(
        f"x = {centroid['x']:.3f}"
    )

    print(
        f"Y = {centroid['y']:.3f}"
    )

    print(
        f"z = {centroid['z']:.3f}"
    )

    df = add_derived_features(df)
    df = add_numpy_calculations(df)

    #----------------------------------------
    #  STEP 4
    # Pandas analysis
    # ---------------------------------------

    print_dataset_summary(df)

    print_feature_counts(df)

    print_geometry_counts(df)

    print_numeric_statistics(df)

    #---------------------------------------
    # STEP 5
    # Grouped analysis
    # --------------------------------------

    grouped = group_by_feature_type(df)

    print("\n==============================")
    print("FEATURE TYPE ANALYSIS")
    print("================================")

    print(grouped.to_string(index=False))

    #----------------------------------------
    # STEP 6
    # Largest feature
    # ----------------------------------------

    largest = find_largest_features(
        df,
        count=5
    )

    print("\n===============================")
    print("TOP 5 FEATURES BY VOLUME")
    print("=================================")

    print(
        largest[
            [
                "feature_id",
                "feature_type",
                "geometry_type",
                "volume",
                "aspect_ratio",
            ]
        ].to_string(index=False)
    )

#------------------------------------------------
# STEP 7
# Save processed CSV
#-----------------------------------------------

    output_directory = "data/output"

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    output_file = os.path.join(
        output_directory,
        "cad features processed.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print("\n==================================")
    print("CSV  OUTPUT")
    print("====================================")

    print(
        f"Processed data saved to:\n"
        f"{output_file}"
    )

    #-------------------------------------------
    # STEP 8
    # Visualization
    #------------------------------------------

    print("\nOpening 3D CAD feature visualization....")

    plot_3d_features(df)

    print("\nOpening volume visualization...")

    plot_feature_volume(df)

    print("\nOpening aspect-ratio visualization...")

    plot_aspect_ratio(df)

if __name__ == "__main__":
    main()

    






