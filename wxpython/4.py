import wx
app=wx.App()
win = wx.Frame(None, title="Hello", pos = (10,10), size = (300,200),style = wx.DEFAULT_FRAME_STYLE, name = "frame")
#win=wx.Frame(None,title="asdasd",size=(500,500))
panel=wx.Panel(win)
lable=wx.StaticText(panel,label="sadfsdf",style=wx.ALIGN_CENTER)
win.Show(True)
app.MainLoop()

