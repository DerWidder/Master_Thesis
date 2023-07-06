'''fucntion to get the Eulerian path'''
'''reference: https://towardsdatascience.com/how-to-create-a-gif-from-matplotlib-plots-in-python-6bec6c0c952c'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imageio

# points of planet pattern
# point_set = pd.read_csv('../new_nodes.txt', sep='\s+')
# points of ring pattern
point_set = pd.read_csv('../Ring/ring_new_nodes.txt', sep='\s+')

x = point_set['x']
y = point_set['y']

'''ordering of planet gear mesh nodes'''
# order = [1 , 0 , 5 , 6 , 1 , 2 , 3 , 2 , 7 , 6 , 11 , 10 , 5 , 10 , 15 , 16 , 11 , 12 , 7 , 8 , 3 , 4 , 9 , 8 ,
#          13 , 12 , 17 , 16 , 21 , 20 , 15 , 20 , 25 , 26 , 21 , 22 , 17 , 18 , 13 , 14 , 9 , 14 , 19 , 18 , 23 ,
#          22 , 27 , 26 , 31 , 30 , 25 , 30 , 35 , 36 , 31 , 32 , 27 , 28 , 23 , 24 , 19 , 24 , 29 , 28 , 33 , 32 ,
#          37 , 36 , 41 , 40 , 35 , 51 , 40 , 45 , 46 , 41 , 42 , 37 , 38 , 33 , 34 , 29 , 34 , 39 , 38 , 43 , 42 ,
#          47 , 45 , 52 , 51 , 60 , 61 , 52 , 53 , 46 , 47 , 54 , 53 , 62 , 61 , 71 , 70 , 60 , 70 , 80 , 81 , 71 ,
#          72 , 62 , 63 , 54 , 55 , 42 , 48 , 49 , 43 , 44 , 39 , 59 , 44 , 50 , 48 , 56 , 55 , 64 , 63 , 73 , 72 ,
#          82 , 81 , 82 , 83 , 73 , 74 , 64 , 92 , 91 , 74 , 84 , 83 , 84 , 90 , 91 , 98 , 97 , 90 , 97 , 104 , 105 ,
#          98 , 99 , 92 , 93 , 55 , 65 , 66 , 56 , 57 , 49 , 50 , 58 , 57 , 67 , 66 , 76 , 75 , 65 , 94 , 93 , 100 ,
#          99 , 106 , 105 , 112 , 111 , 104 , 111 , 118 , 119 , 112 , 113 , 106 , 107 , 100 , 101 , 94 , 95 , 75 , 85 ,
#          86 , 76 , 77 , 67 , 68 , 58 , 59 , 69 , 68 , 78 , 79 , 69, 79,  89 , 88 , 87,88, 78, 77 , 87 , 86 , 85 , 96 ,
#          95 , 102 , 101 , 108 , 107 , 114 , 113 , 120 , 119 , 126 , 125 , 118 , 125 , 132 , 133 , 126 , 127 , 120 , 121 ,
#          114 , 115 , 108 , 109 , 102 , 103 , 96 , 103 , 110 , 109 , 116 , 115 , 122 , 121 , 128 , 127 , 134 , 133 , 140 ,
#          139 , 132 , 139 , 146 , 147 , 140 , 141 , 134 , 135 , 128 , 129 , 122 , 123 , 116 , 117 , 110 , 117 , 124 , 123 ,
#          130 , 129 , 136 , 135 , 142 , 141 , 148 , 147 , 154 , 153 , 146 , 153 , 160 , 161 , 154 , 155 , 148 , 149 , 142 ,
#          143 , 136 , 137 , 130 , 131 , 124 , 131 , 138 , 137 , 144 , 143 , 150 , 149 , 156 , 155 , 162 , 161 , 168 , 167 ,
#          160 , 167 , 174 , 175 , 168 , 169 , 162 , 163 , 156 , 157 , 150 , 151 , 144 , 145 , 138 , 145 , 152 , 151 , 158 ,
#          157 , 164 , 163 , 170 , 169 , 176 , 175 , 182 , 174 , 181 , 182 , 183 , 176 , 177 , 170 , 171 , 164 , 165 , 158 ,
#          159 , 152 , 159 , 166 , 165 , 172 , 171 , 178 , 177 , 184 , 183 , 184 , 185 , 178 , 179 , 172 , 173 , 166 , 173 ,
#          180 , 179 , 186 , 180 , 187 , 186 , 185]

'''ordering of ring gear mesh nodes'''
order_ring = [153 , 146 , 139 , 132 , 124 , 120 , 114 , 106 , 99 , 86 ,
            73 , 65 , 56 , 47 , 38 , 29 , 20 , 11 , 2 , 1 , 0 , 9 , 10 ,
            1 , 2 , 3 , 4 , 3 , 12 , 11 , 10 , 19 , 18 , 9 , 18 , 27 , 28 , 19 ,
            20 , 21 , 12 , 13 , 4 , 5 , 6 , 5 , 14 , 13 , 22 , 21 , 30 , 29 , 28 ,
            37 , 36 , 27 , 36 , 45 , 46 , 37 , 38 , 39 , 30 , 31 , 22 , 23 , 14 , 15 ,
            6 , 7 , 8 , 17 , 7 , 16 , 15 , 24 , 23 , 32 , 31 , 40 , 39 , 48 , 47 , 46 ,
            55 , 54 , 45 , 54 , 63 , 64 , 55 , 56 , 57 , 48 , 49 , 40 , 41 , 32 , 33 , 24 ,
            25 , 16 , 17 , 26 , 25 , 34 , 33 , 42 , 41 , 50 , 49 , 58 , 57 , 66 , 65 , 64 ,
            65 , 75 , 74 , 72 , 64 , 84 , 83 , 63 , 83 , 104 , 105 , 84 , 85 , 72 , 73 , 74 ,
            87 , 86 , 85 , 98 , 99 , 100 , 87 , 88 , 75 , 76 , 66 , 67 , 58 , 59 , 50 , 51 , 42 ,
            43 , 34 , 35 , 26 , 35 , 44 , 43 , 52 , 51 , 60 , 59 , 68 , 67 , 77 , 76 , 89 , 88 ,
            107 , 100 , 98 , 105 , 106 , 105 , 113 , 112 , 104 , 112 , 118 , 119, 120, 119 , 113 , 114 , 125 ,
            124 , 132 , 133 , 125 , 126 , 106 , 107 , 127 , 89 , 90 , 77 , 78 , 68 , 69 , 60 , 61 , 52 ,
            53 , 44 , 53 , 62 , 61 , 70 , 69 , 70 , 71 , 62 , 71 , 97 , 96 , 70 , 82 , 80 , 79 , 69 , 81 ,
            80 , 93 , 92 , 79 , 78 , 91 , 90 , 135 , 127 , 126 , 134 , 133 , 140 , 139 , 146 , 147 , 140 ,
            141 , 134 , 135 , 128 , 91 , 92 , 108 , 101 , 93 , 94 , 81 , 82 , 95 , 94 , 102 , 101 , 103 , 95 ,
            96 , 110 , 103 , 102 , 109 , 108 , 128 , 129 , 109 , 110 , 109 , 115 , 116 , 110 , 111 , 97 , 111 ,
            117 , 116 , 122 , 117 , 123 , 122 , 121 , 115 , 130 , 129 , 136 , 135 , 142 , 141 , 148 , 147 , 154 ,
            153 , 160 , 161 , 154 , 155 , 148 , 149 , 142 , 143 , 136 , 137 , 130 , 131 , 121 , 131 , 138 , 137 ,
            144 , 143 , 150 , 149 , 156 , 155 , 162 , 161 , 162 , 163 , 156 , 157 , 150 , 151 , 144 , 145 , 138 ,
            145 , 152 , 151 , 158 , 157 , 164 , 163 , 164 , 165 , 152 , 159 , 158 , 165 , 166 , 159]

'''create animation of the planet gear Eulerian path'''
# x_whole = [x[i] for i in order]
# y_whole = [y[i] for i in order]
#
# time = [i for i in range(len(order))]
# def create_frame(t):
#     fig = plt.figure()
#     plt.plot(x_whole[:(t+1)], y_whole[:(t+1)], color = 'grey' )
#     plt.plot(x_whole[t], y_whole[t], color='black', marker = 'o' )
#     plt.xlim([-7.5, 7.5])
#     plt.xlabel('x', fontsize = 14)
#     plt.ylim([10, 60])
#     plt.ylabel('y', fontsize = 14)
#     # plt.title(f'Relationship between x and y at step {t}',
#     #           fontsize=14)
#     plt.savefig(f'D:/Daten/TUD SS2020/Masterarbeit/Lasergravur/animation/img/img_{t}.png',
#                 transparent = False,
#                 facecolor = 'white'
#                )
#     plt.close()

'''create animation of the ring gear Eulerian path'''
x_whole = [x[i] for i in order_ring]
y_whole = [y[i] for i in order_ring]

time = [i for i in range(len(order_ring))]

def create_frame(t):
     fig = plt.figure()
     plt.plot(x_whole[:(t + 1)], y_whole[:(t + 1)], color='grey')
     plt.plot(x_whole[t], y_whole[t], color='black', marker='o')
     plt.xlim([-10, 10])
     plt.xlabel('x', fontsize=14)
     plt.ylim([160, 200])
     plt.ylabel('y', fontsize=14)
     # plt.title(f'Relationship between x and y at step {t}',
     #           fontsize=14)
     plt.savefig(f'D:/Daten/TUD SS2020/Masterarbeit/Lasergravur/animation/img_ring/img_{t}.png',
                transparent=False,
                facecolor='white'
                )
     plt.close()

if __name__ == '__main__':

    for t in time:
        create_frame(t)

    frames = []
    for t in time:
        image = imageio.imread(f'D:/Daten/TUD SS2020/Masterarbeit/Lasergravur/animation/img_ring/img_{t}.png')
        frames.append(image)

    imageio.mimsave('ring.gif', # output gif
                    frames,          # array of input frames
                    fps=10)         # optional: frames per second