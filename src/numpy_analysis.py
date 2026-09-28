"""
numpy_analysis.py

NumPy-based geometric calculations.
"""
import numpy as np
import pandas as pd

def calculate_bounding_box(df: pd.DataFrame):
     """
    Calculate the bounding box of all CAD feature locations.

    Returns
    -------
    dict
        Minimum coordinates, maximum coordinates,
        and bounding-box dimensions.
    """
     points = df[["x", "y", "z"]].to_numpy(dtype=float)

     min_coordinates = np.min(points, axis=0)
     max_coordinates = np.max(points, axis=0)

     dimensions = max_coordinates - min_coordinates

     return {
          "min_x": min_coordinates[0],
          "min_y": min_coordinates[1],
          "min_z": min_coordinates[2],

          "max_x": max_coordinates[0],
          "max_y": max_coordinates[1],
          "max_z": max_coordinates[2],

          "size_x": dimensions[0],
          "size_y": dimensions[1],
          "size_z": dimensions[2],
     }

def calculate_centroid(df: pd.DataFrame):
     """
     calculate centroid of all feature location
     """
     points = df[["x", "y", "z"]].to_numpy(dtype=float)

     centroid = np.mean(points, axis=0)

     return {
          "x": centroid[0],
          "y": centroid[1],
          "z": centroid[2],
     }

def calculate_distance(point1, point2):
     """
     Calculate Euclidean distance between two 3D points
     """

     p1 = np.asarray(point1, dtype=float)
     p2 = np.asarray(point2, dtype=float)

     return np.linalg.norm(p2 - p1)

def calculate_distances_from_centroid(df: pd.DataFrame):
     """
     Calculate distance of every CAD feature
     from the overall feature centroid
     """
     points = df[["x", "y", "z"]].to_numpy(dtype=float)

     centroid = np.mean(points, axis=0)

     distances = np.linalg.norm(points - centroid, axis=1)

     return distances

def add_numpy_calculations(df: pd.DataFrame):
     """
     Add Numpy-derived geometric information to DataFrame
     """

     result = df.copy()

     result["distance_from_origin"] = np.linalg.norm(
          result[["x", "y", "z"]].to_numpy(dtype=float),
          axis=1)

     result["distance_from_centroid"] = calculate_distances_from_centroid(result)

     return result
    




