import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title,size=(250, 250))
        topPanel = wx.Panel(self, -1)
        topPanel.SetBackgroundColour('green')
        panel1 = wx.Panel(topPanel, -1, style=wx.TRANSPARENT_WINDOW)
        panel1.SetTransparent(100)
        panel2 = wx.Panel(topPanel, -1)
        panel2.SetBackgroundColour('gray')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel1,1,flag = wx.EXPAND|wx.ALL)
        sizer.Add(panel2,1,flag = wx.EXPAND|wx.ALL)

        topPanel.SetSizer(sizer)



class MyApp(wx.App):
     def OnInit(self):
         frame = MyFrame(None, -1, 'frame')
         frame.Show(True)
         return True

app = MyApp(0)
app.MainLoop()