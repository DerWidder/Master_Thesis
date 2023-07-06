'''function to get transformed coordinates of each mesh by rotating a certain angle'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# point_set = pd.read_csv('planet_top_small_nodes.txt', sep='\s+')
point_set = pd.read_csv('nodes_planetgear_Element10_Toothnew.txt', sep='\s+')
# point_set = pd.read_csv('./Ring/Ring_small_nodes.txt', sep='\s+')
# point_set = pd.read_csv('./Sun/Sun_node_new_small.txt', sep='\s+')
order_planetgear_Element10_Toothnew = [1, 0, 3, 4, 1, 2, 5, 4, 7, 6, 3, 10, 11, 6, 11, 12, 7, 12, 13, 4, 8, 9, 5, 16,
                                       15, 9, 15, 14, 8, 14, 13, 20, 19, 12, 19, 18, 11, 18, 17, 10, 17, 24, 25, 18,
                                       25, 26, 19, 26, 27, 20, 21, 14, 21, 22, 15, 22, 23, 16, 23, 31, 30, 22, 30, 29,
                                       21, 29, 28, 20, 42, 41, 27, 35, 34, 26, 34, 33, 25, 33, 32, 24, 32, 33, 34, 35,
                                       40, 41, 46, 45, 40, 45, 50, 51, 46, 47, 42, 43, 28, 36, 37, 29, 37, 38, 30, 38,
                                       39, 31, 39, 38, 37, 36, 44, 43, 48, 47, 52, 51, 56, 55, 50, 55, 60, 61, 56, 57,
                                       52, 53, 48, 49, 44, 49, 54, 53, 58, 57, 62, 61, 66, 65, 60, 65, 70, 71, 66, 67,
                                       62, 63, 58, 59, 54, 59, 64, 63, 68, 67, 72, 71, 76, 75, 70, 75, 80, 81, 76, 77,
                                       72, 73, 68, 69, 64, 69, 74, 73, 78, 77, 82, 81, 86, 85, 80, 85, 90, 91, 86, 87,
                                       82, 83, 78, 79, 74, 79, 84, 83, 88, 87, 92, 91, 96, 95, 90, 95, 100, 101, 96, 97,
                                       92, 93, 88, 89, 84, 89, 94, 93, 98, 97, 102, 101, 102, 103, 98, 99, 94, 99, 104, 103]

order_ring_small_corr = [1 , 0 , 7 , 8 , 1 , 2 , 3 , 2 , 9 , 8 , 15 , 14 , 7 , 14 , 21 , 22 , 15 ,
                    16 , 9 , 10 , 3 , 4 , 5 , 4 , 11 , 10 , 17 , 16 , 23 , 22 , 29 , 28 , 21 ,
                    28 , 35 , 36 , 29 , 30 , 23 , 24 , 17 , 18 , 11 , 12 , 5 , 6 , 13 , 12 , 19 ,
                    18 , 25 , 24 , 31 , 30 , 37 , 36 , 43 , 36, 35 , 42 , 43 , 44 , 37 , 38 , 31 , 32 ,
                    25 , 26 , 19 , 20 , 13 , 20 , 27 , 26 , 33 , 32 , 39 , 38 , 45 , 44 , 53 , 52 ,
                    43 , 50 , 49 , 42 , 60 , 61 , 49 , 50,  51 , 50 , 62 , 61 , 73 , 74 , 62 , 63 , 51 ,
                    52 , 64 , 63 , 75 , 74, 73 , 79 , 60 , 79, 80 , 74 , 75 , 81 , 64 , 65 , 53 , 54 , 45 ,
                    46 , 39 , 40 , 33 , 34 , 27 , 34 , 41 , 40 , 47 , 48,  41 , 48 , 47 , 46 , 55 , 54 ,
                    66 , 65 , 96 , 81 , 80 , 79 , 85 , 86 , 87 , 86,  85 , 88 , 80 , 95 , 94 , 88 , 87 ,
                    93 , 94 , 102 , 101 , 93 , 101 , 108 , 109 , 102 , 103 , 95 , 96 , 104 , 66 , 67 ,
                    55 , 56 , 47 , 58 , 57 , 56 , 68 , 67 , 97 , 82 , 68 , 69 , 57 , 58,  59 , 48 , 72 ,
                    71 , 59 , 58 , 70 , 69 , 76 , 77 , 70 , 71 , 78 , 77,  76 , 82 , 83 ,84,  72 , 84 , 78 ,
                    77 , 83 , 84 , 89 , 90 , 91 , 90, 89 , 92 , 83 , 98 , 97 , 104 , 103 , 110 , 109 ,
                    116 , 115 , 108 , 115 , 122 , 123 , 116 , 117 , 110 , 111 , 104 , 105 , 98 , 99 ,
                    92 , 91 , 100 , 99 , 106 , 105 , 112 , 111 , 118 , 117 , 124 , 123 , 124 , 125 ,
                    118 , 119 , 112 , 113 , 106 , 107 , 100 , 107 , 114 , 113 , 120 , 119 , 126 , 125 ,
                    126 , 127 , 120 , 121 , 114 , 121 , 128 , 127]

order_sun_small_corr = [1 , 0 , 3 , 4 , 1 , 2 , 5 , 4 , 7 , 6 , 3 , 6 , 9 , 10 , 7 , 8 , 5 , 8 , 11 , 10 , 13 , 12 ,
                   9 , 12 , 15 , 16 , 13 , 14 , 11 , 14 , 17 , 16 , 26 , 18 , 15 , 18 , 19 , 20 , 24 , 20, 19 , 25 ,
                   24 , 29 , 30 , 25 , 26 , 21 , 17 , 21 , 22 , 23 , 28 , 23, 22 , 27 , 26 , 31 , 30 , 35 , 34 , 29 ,
                   34 , 39 , 40 , 35 , 36 , 31 , 32 , 27 , 28 , 33 , 32 , 37 , 36 , 41 , 40 , 41 , 42 , 37 , 38 ,
                   33 , 38 , 43 , 42]

coor = point_set[['x', 'y', 'z']]
'''
change the value in column Z to be 10.0
coor['z'] = 10.0
'''
coor_new = coor.copy()
coor_new['z'] = 10.0  # front surface
# coor_new['z'] = -10.0  # back surface
# print(coor)


theta_planet = [i * 2 * np.pi / 21 for i in range(21)]  # from 0 to 20, the first will be initial state
theta_sun = [i * 2 * np.pi / 24 for i in range(24)]  # from 0 to 23, the first will be initial state
theta_ring = [i * 2 * np.pi / 66 for i in range(66)]  # from 0 to 65, the fist will be initial state

# print(theta_planet[0])

'''Planet'''
# T = np.array([[np.cos(theta_planet[0]), -np.sin(theta_planet[0]), 0],
#               [np.sin(theta_planet[0]), np.cos(theta_planet[0]), 0],
#               [0, 0, 1]])

for i in range(21):
    T = np.array([[np.cos(theta_planet[i]), -np.sin(theta_planet[i]), 0],
                  [np.sin(theta_planet[i]), np.cos(theta_planet[i]), 0],
                  [0, 0, 1]])

    coor_rotate = (np.matmul(T, coor_new.T)).T
    # print(coor_rotate_1)

    x = coor_rotate['x']
    y = coor_rotate['y']
    # x_top = [x[i] for i in order_top_small]
    # y_top = [y[i] for i in order_top_small]
    x_top = [x[i] for i in order_planetgear_Element10_Toothnew]
    y_top = [y[i] for i in order_planetgear_Element10_Toothnew]
    fig = plt.figure()
    plt.plot(x_top, y_top)
    plt.axis('scaled')
    plt.show()
    coor_rotate.to_csv(f'./Transform/Planet_new/Planet_coor_rotate_{i}.txt', sep=' ', index=0, header="x, y, z")


'''Ring'''
# theta_ring_offset = np.pi / 66
# T_ring_offset = np.array([[np.cos(theta_ring_offset), -np.sin(theta_ring_offset), 0],
#               [np.sin(theta_ring_offset), np.cos(theta_ring_offset), 0],
#               [0, 0, 1]])
# coor_new = (np.matmul(T_ring_offset, coor_new.T)).T  # first compensate the offset of the ring gear pattern
# for i in range(66):
#     T = np.array([[np.cos(theta_ring[i]), -np.sin(theta_ring[i]), 0],
#                   [np.sin(theta_ring[i]), np.cos(theta_ring[i]), 0],
#                   [0, 0, 1]])
#
#     coor_rotate = (np.matmul(T, coor_new.T)).T
#     # print(coor_rotate_1)
#
#     x = coor_rotate['x']
#     y = coor_rotate['y']
#     x_top = [x[i] for i in order_ring_small_corr]
#     y_top = [y[i] for i in order_ring_small_corr]
#     fig = plt.figure()
#     plt.plot(x_top, y_top)
#     plt.axis('scaled')
#     plt.show()
#     coor_rotate.to_csv(f'./Transform/Ring/Ring_coor_rotate_{i}.txt', sep=' ', index=0, header="x, y, z")


'''Sun'''
# for i in range(24):
#     T = np.array([[np.cos(theta_sun[i]), -np.sin(theta_sun[i]), 0],
#                   [np.sin(theta_sun[i]), np.cos(theta_sun[i]), 0],
#                   [0, 0, 1]])
#
#     coor_rotate = (np.matmul(T, coor_new.T)).T
#     # print(coor_rotate_1)
#
#     x = coor_rotate['x']
#     y = coor_rotate['y']
#     x_top = [x[i] for i in order_sun_small_corr]
#     y_top = [y[i] for i in order_sun_small_corr]
#     fig = plt.figure()
#     plt.plot(x_top, y_top)
#     plt.axis('scaled')
#     plt.show()
#     coor_rotate.to_csv(f'./Transform/Sun/Back/Sun_coor_rotate_{i}.txt', sep=' ', index=0, header="x, y, z")