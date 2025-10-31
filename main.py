import imageio.v3 as iio
import os


folder_path = 'Python-gif/img'
images = []

for filename in os.listdir(folder_path):
    images.append(iio.imread(f'{folder_path}/{filename}'))


iio.imwrite(f'Python-gif/team.gif', images, duration = 500, loop = 0)