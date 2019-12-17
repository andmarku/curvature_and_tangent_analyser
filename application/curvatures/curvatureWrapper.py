from knutsson import knutssonMapper
from dw_dt_approximator import dmDotTangents
from curvatureCalculator import calcCurvatureForAllVoxels

def curvatures(tensor_tangents):
    print("knutsson")
    tensor_knutVecs = knutssonMapper(tensor_tangents)
    print("dm dot tangent")
    tensor_dmAlongTangent = dmDotTangents(tensor_knutVecs,tensor_tangents)
    print("calculate curvature final step")
    tensor_curvatures = calcCurvatureForAllVoxels(tensor_dmAlongTangent)
    return tensor_curvatures
