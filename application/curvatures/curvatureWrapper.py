from knutsson import knutssonMapper
from dw_dt_approximator import dmDotTangents
from curvatureCalculator import calcCurvatureForAllVoxels

def curvatures(tensor_tangents):
    tensor_knutVecs = knutssonMapper(tensor_tangents)

    tensor_dmAlongTangent = dmDotTangents(tensor_knutVecs,tensor_tangents)

    tensor_curvatures = calcCurvatureForAllVoxels(tensor_dmAlongTangent)
    
    return tensor_curvatures
