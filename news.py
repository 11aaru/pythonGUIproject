import io

import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image



class NewsApp:

    def __init__(self):


        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=e55ad4fe10c14e628cac25c4ecf6718d').json()
        # print(data)
        #inital gui load
        self.load_gui()


        # load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.title('Mera News App')
        self.root.resizable(0,0)
        self.root.configure(background='black')
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_item(self,index):


         #clear the screen for new news item
         self.clear()


         #image
         try:
             img_url = self.data['articles'][index]['urlToImage']
             raw_data=urlopen(img_url).read()
             im=Image.open(io.BytesIO(raw_data)).resize((350,250))
             photo=ImageTk.PhotoImage(im)
         except:
             img_url = 'https://th.bing.com/th/id/OIP.VEvRFkyZvqOfPdtaHRdQlgHaHa?w=172&h=180&c=7&r=0&o=5&pid=1.7'
             raw_data = urlopen(img_url).read()
             im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
             photo = ImageTk.PhotoImage(im)

         label = Label(self.root,image=photo)
         label.image=photo
         label.pack()


        #print next news item

         heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
         heading.pack(pady=(10,20))
         heading.config(font=('verdana',15))

         details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,
                         justify='center')
         details.pack(pady=(2, 20))
         details.config(font=('verdana', 12))

         frame = Frame(self.root,bg='black')
         frame.pack(expand=True,fill=BOTH)


         if index != 0:
             prev = Button(frame,text='Prev',width=16,height=3,command=lambda :self.load_news_item(index+1))
             prev.pack(side=LEFT)

         read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
         read.pack(side=LEFT)

         if index != len(self.data['articles'])-1:

             next = Button(frame, text='Next', width=16, height=3,command=lambda :self.load_news_item(index+1))
             next.pack(side=LEFT)


         self.root.mainloop()

    def open_link(self, param):
        pass


obj = NewsApp()


