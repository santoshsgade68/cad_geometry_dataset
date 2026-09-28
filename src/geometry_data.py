"""
geometry_data.py

Contains sample CAD geometry/feature data.

This is synthetic data for Project 2.
Later, this data can be replaced by geometry extracted
from STEP files.
"""
import pandas as pd

def create_cad_dataset():
    """
    Create a sample CAD feature dataset.

    Returns
    -------
    pandas.DataFrame
        CAD feature information.
    """
    data = [
        #feature_id, feature_type, geometry_type,
        #x, y, z, radius, height
        [1, 'hole', 'cylinder', 10.0, 20.0, 5.0, 2.0, 10.0],
        [2, 'hole', 'cylinder', 15.0, 25.0, 5.0, 3.0, 12.0],
        [3, 'hole', 'cylinder', 20.0, 30.0, 5.0, 4.0, 15.0],

        [4, 'pocket', 'cylinder', 5.0, 10.0, 2.0, 6.0, 8.0],
        [5, 'pocket', 'cylinder', 12.0, 18.0, 3.0, 7.0, 9.0],
        [6, 'pocket', 'cylinder', 18.0, 22.0, 4.0, 8.0, 10.0],

        [7, 'boss', 'cylinder', 8.0, 16.0, 5.0, 2.5, 10.0],
        [8, 'boss', 'cylinder', 14.0, 24.0, 6.0, 3.5, 12.0],
        [9, 'boss', 'cylinder', 22.0, 28.0, 7.0, 4.5, 15.0],

        [10, 'Fillet', 'Torus', 6.0, 12.0, 3.0, 1.5, 5.0],
        [11, 'Fillet', 'Torus', 13.0, 21.0, 4.0, 2.0, 6.0],

        [12, 'Chamfer', 'Cone', 9.0, 19.0, 5.0, 2.5, 7.0],

        [13, 'Boss', 'Cylinder', 11.0, 23.0, 6.0, 3.0, 8.0],
        [14, 'Hole', 'Cylinder', 17.0, 27.0, 7.0, 4.0, 9.0],
        [15, 'Pocket', 'Cylinder', 21.0, 31.0, 8.0, 5.0, 10.0],
    ]

    columns = [
        'feature_id', 'feature_type', 'geometry_type',
        'x', 'y', 'z', 'radius', 'height'       
    ]

    df = pd.DataFrame(data, columns=columns)
    
    return df








