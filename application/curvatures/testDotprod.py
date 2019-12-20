import numpy as np
from dw_dt_approximator import approximateAlong_XYZ
from dw_dt_approximator import dmDotTangents

def dmDotTangents(tensor_knutVecs, tensor_tangents):

    tensor_DM = approximateAlong_XYZ(tensor_knutVecs)

    dim = tensor_knutVecs.shape
    dmAlongTangent = np.zeros((dim[0],dim[1],dim[2],9))

    # for each DM take the dot product between the 3 derivatives and the tangent
    for x in range(dim[0]):
        for y in range(dim[1]):
            for z in range(dim[2]):
                for i in range(9):
                    dmAlongTangent[x,y,z,i] = tensor_DM[x,y,z,:,i].dot(tensor_tangents[x,y,z])

    return dmAlongTangent

def newdmDotTangents(tensor_knutVecs, tensor_tangents):
    tensor_DM = approximateAlong_XYZ(tensor_knutVecs)

    dim = tensor_knutVecs.shape
    dmAlongTangent = np.zeros((dim[0],dim[1],dim[2],9))

    for idx, _ in np.ndenumerate(tensor_DM[:,:,:,0,0]):
        voxelDM = tensor_DM[idx[0], idx[1], idx[2], :, :]
        voxelTangent = tensor_tangents[idx[0], idx[1], idx[2],:]
        dmAlongTangent[idx[0], idx[1], idx[2],:] = voxelTangent@voxelDM

    return dmAlongTangent

if __name__ == '__main__':
    tensor_knutVecs = np.random.rand(200,200,200,9)
    tensor_tangents = np.random.rand(200,200,200,3)
    dim = tensor_knutVecs.shape

    print(dmDotTangents(tensor_knutVecs,tensor_tangents).shape)
    # markus = dmDotTangents(tensor_knutVecs, tensor_tangents)
    # mikael = newdmDotTangents(tensor_knutVecs, tensor_tangents)
    # tensor_DM = approximateAlong_XYZ(tensor_knutVecs)
    # print(tensor_DM.shape)
    # newScalarProd = np.outer(tensor_DM, tensor_tangents)
    # print(markus.shape)
    # print(newScalarProd.shape)
    # dmAlongTangent = np.zeros((dim[0],dim[1],dim[2],9))
    # i = 0

        # print(idx, value)
    #     # print(tensor_tangents[idx[0], idx[1], idx[2],:])
    # print('old shape: ', markus.shape)
    # print('new shape: ', mikael.shape)
    # print(markus[1,1,1,:])
    # print(mikael[1,1,1,:])
