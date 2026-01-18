import numpy as np
import trimesh

def trimesh_cylinder (radius = 10.0,
                      height = 20.0,
                      n_theta = 64,
                      n_z = 40,
                      twist_ratio = 0.5
                      ):

    vertices = []
    faces = []

    dtheta = 2 * np.pi / n_theta
    dz = height / n_z

    ### angle betweem (i,j) - (i,j+1) on x-y plane ###
    twist = twist_ratio * dtheta

    ### nodes generator ###
    for j in range(n_z + 1):
        z = j * dz
        theta_offset = j * twist
        for i in range(n_theta):
            theta = i * dtheta + theta_offset
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)
            vertices.append([x, y, z])
    vertices = np.array(vertices)

    ### vertices index ####
    def vid(i, j):
        return j * n_theta + (i % n_theta)

    ### triangle faces generator ###
    for j in range(n_z):
        for i in range(n_theta):
            faces.append ([vid(i, j), 
                           vid(i + 1, j), 
                           vid(i, j + 1)
                         ])
            faces.append ([vid(i + 1, j), 
                           vid(i + 1, j + 1), 
                           vid(i, j + 1)
                         ])

    return trimesh.Trimesh (vertices = vertices,
                            faces = np.array (faces),
                            process = True)

if __name__ == "__main__":
    mesh = trimesh_cylinder (radius = 10,
                             height = 20,
                             n_theta = 72,
                             n_z = 50,
                             twist_ratio = 0.5
                             )

    print("faces:", len(mesh.faces))
    print("watertight:", mesh.is_watertight)

    mesh.export("cylinder.stl")
