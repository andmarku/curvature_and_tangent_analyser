import knutsson
import dw_dt_approximator as dm
import curvatureCalculator

def curvatures(tensor_tangents):
    tensor_knutVecs = knutsson.knutssonMapping(tensor_tangents)
    tensor_dmAlongTangent = dmDotTangents(tensor_knutVecs,tensor_tangents)
    tensor_curvatures = curvatureCalcForAllVoxels(tensor_dmAlongTangent)
    return tensor_curvatures
