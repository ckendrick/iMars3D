import os
import numpy as np
import matplotlib.pyplot as plt

from iVenus import config, io
from iVenus import detector_correction


file = '/Users/j35/Dropbox (ORNL)/iVenus_data_set/Low_res_Gdmask_r0000.fits'
#print('Does file exist: %s' %os.path.isfile(file))

# retrieve image
image_data = io.ImageFile(file).getData()

#plt.figure()
#plt.imshow(image_data, cmap='gray')
#plt.colorbar()
#plt.show()

(detector_width, detector_height) = image_data.shape
chip_width = detector_width/2
chip_height = detector_height/2

# isolate chips data
chip1 = image_data[0:chip_height, 0:chip_width]
chip2 = image_data[0:chip_height, chip_width:detector_width]
chip3 = image_data[chip_height:detector_height, 0:chip_width]
chip4 = image_data[chip_height:detector_height, chip_width:detector_width]

# init final image
detector_config = '../config/detector_offset.yml'

# retrieve offset values
chips_offset = detector_correction.retrieve_mcp_chips_offset.RetrieveMCPChipsOffset(detector_config)

## calculate max x and y offset (to determine size of new image)
new_detector_width_offset = chips_offset.get_detector_new_width_offset()
print('new_detector_width_offset: %d' %new_detector_width_offset)
new_detector_height_offset = chips_offset.get_detector_new_height_offset()
print('new_detector_width_offset: %d' %new_detector_height_offset)


#[xmax, ymax] = chips_offset.get_max_offset()
#print("xmax = %d" %xmax)
#print("ymax = %d" %ymax)

#new_detector_width = detector_width + xmax
#new_detector_height = detector_height + ymax
#new_image_data = np.zeros(())