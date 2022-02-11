from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import os
import numpy as np

import scipy.misc

import imageio



from PIL import Image
from numpy import asarray

class OilSpill:
    TAG = "oillspill.class"
    imagePath_b5 = ""
    image_b5 = None

    imagePath_b4 = ""
    image_b4 = None

    luastumpahanLight = None
    luastumpahanMedium = None
    luastumpahanHeavy = None
    luastumpahanTotal = None

    imagePath_b3 = ""
    image_b3 = None

    def openImage_b5(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath_b5 = path
            self.image_b5 = openImage
            return True

    def openImage_b4(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath_b4 = path
            self.image_b4 = openImage
            return True

    def openImage_b3(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath_b3 = path
            self.image_b3 = openImage
            return True

    def scaleMinMax(x):
        return((x - np.nanmin(x))/(np.nanmax(x) - np.nanmin(x)))
    def scaleCCC(x):
        return((x - np.nanpercentile(x, 2))/(np.nanpercentile(x, 98) - np.nanpercentile(x,2)))
    def scaleStd(x):
        return((x - (np.nanmean(x)-np.nanstd(x)*1))/((np.nanmean(x)+np.nanstd(x)*1) - (np.nanmean(x)-np.nanstd(x)*1)))

    def start(self):
        b5 = self.image_b5.GetRasterBand(1).ReadAsArray()
        b4 = self.image_b4.GetRasterBand(1).ReadAsArray()
        b3 = self.image_b3.GetRasterBand(1).ReadAsArray()

        b5_CCC = ((b5 - np.nanpercentile(b5, 2))/(np.nanpercentile(b5, 98) - np.nanpercentile(b5,2)))
        b4_CCC = ((b4 - np.nanpercentile(b4, 2))/(np.nanpercentile(b4, 98) - np.nanpercentile(b4,2)))
        b3_CCC = ((b3 - np.nanpercentile(b3, 2))/(np.nanpercentile(b3, 98) - np.nanpercentile(b3,2)))

        final_band = np.dstack((b5_CCC, b4_CCC, b3_CCC))

        plt.figure()
        plt.imshow(final_band)
        plt.colorbar()
        plt.savefig("foo.png",bbox_inches="tight")

        # cmap = plt.cm.jet
        # norm = plt.Normalize(vmin=final_band.min(), vmax=final_band.max())

        # image = cmap(norm(final_band))

        # plt.imsave('foo.png', image, cmap=cmap)

        driver = gdal.GetDriverByName('GTiff')
        dst_filename = '/tmp/x_tmp.tif'
        dst_ds=driver.Create(dst_filename,512,512,1,gdal.GDT_Byte)

        imageio.imwrite('full.tiff', final_band)


        # scipy.misc.imsave('outfile.png', final_band)
        # im = Image.fromarray(final_band)
        # im.save("oilspill.png")

        image = Image.open("foo.png")

        self.luastumpahanLight=((final_band >= 0.02) & (final_band <= 0.07)).sum()
        self.luastumpahanLight = self.luastumpahanLight*900/10000

        self.luastumpahanMedium=((final_band >= 0.07) & (final_band <= 0.12)).sum()
        self.luastumpahanMedium = self.luastumpahanMedium*900/10000

        self.luastumpahanHeavy=((final_band >= 0.12) & (final_band <= 0.17)).sum()
        self.luastumpahanHeavy = self.luastumpahanHeavy*900/10000

        self.luastumpahanTotal=((final_band >= 0.02) & (final_band <= 0.17)).sum()
        self.luastumpahanTotal = self.luastumpahanTotal*900/10000
        
        # raw_img= Image.open("full.tif")
        # array=asarray(raw_img)
        # r,g,b=array[:,:,0],array[:,:,1],array[:,:,2]
        # print(r.shape)
        # print(g.shape)
        # print(b.shape)
        # r=np.where(final_band>=0.2,0,r)
        # g=np.where((final_band >= 0.02) & (final_band <= 0.17),255,g)
        # b=np.where(final_band>=0.2,0,b)
        # newarray=np.array([r,g,b])
        # newarray=np.swapaxes(newarray,0,1)
        # newarray=np.swapaxes(newarray,1,2)
        # im = Image.fromarray(newarray).convert('RGB')
        # im.save("oilcover.png")

        return image

        createOverlayAboveRaster("citra rgb.tif","tutupan lahan gambut.png")