import math
import numpy as np

def unpack_geometry(geom):
    m_array, coords = [], []
    for coord in geom['coordinates']:
        coords.append(coord[:2])
        m_array.append(coord[2])
    geom['coordinates'] = coords
    geom['type'] = geom['type'].rstrip('M')
    return geom, m_array


def add_m(coords, m_array):
    assert len(coords) == len(m_array)
    m_coords = []
    [m_coords.append(xy + (m,)) for xy, m in zip(coords, m_array)]
    return m_coords


def scale(values):
    old_range = max(values) - min(values)
    results = []
    for value in values:
        results.append(int(((value - min(values)) * 10) / old_range + 1))
    return results


def log_scale(values):
    results = []
    for value in values:
        results.append(math.log(value))
    return results

def normalize(values):
    for value in values:
        value = value / 39499.0
    return values

def as_ndarray(coords,m_array):
    assert len(coords) == len(normalize(m_array))
    return np.insert(np.asarray(coords), 2, m_array, axis=1)


def zip_geometry(geom,m_values):
    coords = []
    for coord, m in zip(geom['coordinates'], m_values):
        coords.append(coord + (m,))
    geom['coordinates'] = coords
    return geom

