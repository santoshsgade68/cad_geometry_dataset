"""
feature_engineering.py

Creates derived CAD/geometry features from 
the raw CAD dataset
"""

import numpy as np
import pandas as pd

def add_derived_features(df: pd.DataFrame):
    """
    Add derived geometric parameters.

    Calculations include:

    -diameter
    -circular area
    -cylindrical volume
    -lateral surface area
    -total cylindrical surface area
    -aspect ratio
    """

    result = df.copy()

    #-------------------------------------------------------
    # Diameter
    #-------------------------------------------------------

    result["diameter"] = 2.0 * result["radius"]

    #-----------------------------------------------
    # Cylindrical volume
    # V = pi*r^2*h
    # ----------------------------------------------

    result["volume"] = (
        np.pi 
        * result["radius"] ** 2
        * result["height"]
    )

    #-------------------------------------------------
    # Cylindrical lateral surface area
    # A = 2 * pi * r * h
    # ------------------------------------------------

    result["lateral_area"] = (
        2.0
        * np.pi
        * result["radius"]
        * result["height"]
    )

    #----------------------------------------------
    # Total cylindrical surface area
    # A = 2*pi*r*(r+h)
    #---------------------------------------------

    result["Surface_area"] = (
        2.0
        * np.pi
        * result["radius"]
        *(
            result["radius"] + result["height"]
        )
    )

    #-------------------------------------------
    # Aspect ratio
    # height / diameter
    #------------------------------------------

    result["aspect_ratio"] = np.where(
        result["diameter"] != 0,
        result["height"] / result["diameter"],
        0.0
    )

    return result

