# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import numpy

from PIL import Image

from logic import OilSpill

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 957,648 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Aplikasi Deteksi Tumpahan Minyak", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		bSizer12.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer28.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer12.Add( bSizer28, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer12, 0, wx.EXPAND, 0 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Band 5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer7.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap3 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 120,120 ), 0 )
		self.m_bitmap3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_bitmap3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer7.Add( self.m_bitmap3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer7.Add( self.m_filePicker1, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer7, 1, 0, 5 )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Band 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer71.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap31 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 120,120 ), 0 )
		self.m_bitmap31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_bitmap31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer71.Add( self.m_bitmap31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer71.Add( self.m_filePicker2, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer71, 1, 0, 5 )

		bSizer711 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText311 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Band 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )

		bSizer711.Add( self.m_staticText311, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap311 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 120,120 ), 0 )
		self.m_bitmap311.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_bitmap311.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer711.Add( self.m_bitmap311, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_filePicker3 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer711.Add( self.m_filePicker3, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer711, 1, 0, 5 )


		bSizer2.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 0, wx.ALL, 5 )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Composite False Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer31.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap15 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		self.m_bitmap15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer31.Add( self.m_bitmap15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"Proses", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer30.Add( bSizer31, 1, 0, 5 )

		bSizer311 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText161 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Oil Spill Area", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		bSizer311.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap151 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		self.m_bitmap151.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer311.Add( self.m_bitmap151, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button11 = wx.Button( self.m_panel2, wx.ID_ANY, u"Proses", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer311.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer30.Add( bSizer311, 1, 0, 5 )


		self.m_panel2.SetSizer( bSizer30 )
		self.m_panel2.Layout()
		bSizer30.Fit( self.m_panel2 )
		bSizer29.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Penghitungan Luas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer19.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer19.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Light Oil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer19.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer19.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer19.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Medium Oil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		bSizer19.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer19.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer19.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Heavy Oil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer19.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer19.Add( self.m_staticText15, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer19 )
		self.m_panel3.Layout()
		bSizer19.Fit( self.m_panel3 )
		bSizer18.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer29.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer29, 1, 0, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker1OnFileChanged )
		self.m_filePicker2.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker2OnFileChanged )
		self.m_filePicker3.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker3OnFileChanged )

		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.m_button11.Bind( wx.EVT_BUTTON, self.m_button31OnButtonClick )

	def __del__( self ):
		pass

	oilSpill =  OilSpill()

	def m_filePicker1OnFileChanged( self, event ):
		path = event.GetPath()
		isImage = self.oilSpill.openImage_b5(path)
		if isImage:
			# loadImage = Image.open(path)
			# arrayimg = numpy.array(loadImage)
			# img = self.convertToImage(arrayimg, 120, 120, False)
			# bitmapImage = wx.Bitmap(img)
			# self.m_bitmap3.SetBitmap(bitmapImage)
			bitmap = wx.Bitmap(event.GetPath(), wx.BITMAP_TYPE_TIF)
			image = wx.ImageFromBitmap(bitmap)
			image = image.Scale(120, 120, wx.IMAGE_QUALITY_HIGH)
			result = wx.BitmapFromImage(image)
			self.m_bitmap3.SetBitmap(result)
		event.Skip()

	def m_filePicker2OnFileChanged( self, event ):
		path = event.GetPath()
		isImage = self.oilSpill.openImage_b4(path)
		if isImage:
			# loadImage = Image.open(path)
			# arrayimg = numpy.array(loadImage)
			# img = self.convertToImage(arrayimg, 120, 120, False)
			# bitmapImage = wx.Bitmap(img)
			# self.m_bitmap31.SetBitmap(bitmapImage)
			bitmap = wx.Bitmap(event.GetPath(), wx.BITMAP_TYPE_TIF)
			image = wx.ImageFromBitmap(bitmap)
			image = image.Scale(120, 120, wx.IMAGE_QUALITY_HIGH)
			result = wx.BitmapFromImage(image)
			self.m_bitmap31.SetBitmap(result)
		event.Skip()

	def m_filePicker3OnFileChanged( self, event ):
		path = event.GetPath()
		isImage = self.oilSpill.openImage_b3(path)
		if isImage:
			# loadImage = Image.open(path)
			# arrayimg = numpy.array(loadImage)
			# img = self.convertToImage(arrayimg, 120, 120, False)
			# bitmapImage = wx.Bitmap(img)
			# self.m_bitmap311.SetBitmap(bitmapImage)
			bitmap = wx.Bitmap(event.GetPath(), wx.BITMAP_TYPE_TIF)
			image = wx.ImageFromBitmap(bitmap)
			image = image.Scale(120, 120, wx.IMAGE_QUALITY_HIGH)
			result = wx.BitmapFromImage(image)
			self.m_bitmap311.SetBitmap(result)
		event.Skip()

	def m_button31OnButtonClick(self,event):
		event.skip()


	def convertToImage(self, array, w_in, h_in, isFloat):
		newW = w_in
		newH = h_in
		# print(self.segmen.TAG, "Declaring RGB")

		if isFloat:
			rgb = array * 32
			# print(self.segmen.TAG, "Convert Image to RGB")
			pilImage = Image.fromarray(rgb).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
			
		else:
			# print(self.segmen.TAG, "Convert Image to RGB")
			pilImage = Image.fromarray(array).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
		
		# print(self.segmen.TAG, "Resize Image")
		H = image.GetHeight()
		W = image.GetWidth()
		if (W > H):
			newH = newH * H / W
		else:
			newW = newW * W / H
		image = image.Scale(newW, newH, wx.IMAGE_QUALITY_HIGH)
		return image

	def m_button3OnButtonClick( self, event ):
		gambar = self.oilSpill.start()
		arrayimg = numpy.array(gambar)
		# arrayimg = gambar.GetRasterBand(1).ReadAsArray()
		img = self.convertToImage(arrayimg, 320, 320, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap15.SetBitmap(bitmapImage)


		luas_fix_light = self.oilSpill.luastumpahanLight
		luas_fix_medium = self.oilSpill.luastumpahanMedium
		luas_fix_heavy = self.oilSpill.luastumpahanHeavy
		luas_fix_total = self.oilSpill.luastumpahanTotal

		self.m_staticText12.SetLabelText(str(luas_fix_light) + " Hektar")
		self.m_staticText13.SetLabelText(str(luas_fix_medium) + " Hektar")
		self.m_staticText15.SetLabelText(str(luas_fix_heavy) + " Hektar")
		self.m_staticText10.SetLabelText("Total luasan tumpahan minyak sebesar " +str(luas_fix_total) + " Hektar" + ". Rincian dapat dilihat dibawah ini!")

		event.Skip()

class MainApp(wx.App):
    def OnInit(self):
        myframe = MyFrame1(None)
        myframe.Show(True)
        return True


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
