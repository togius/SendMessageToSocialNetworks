from tkinter import Tk, Label, Text, Button, IntVar, Checkbutton, mainloop, END
from tkinter import filedialog as fd
from sender import MessageSender
from threading import Thread

class Tasarim:
    def __init__(self):
        self.tasarim()

    def tasarim(self):
        sender = MessageSender()

        def clickResimSec():
            pickedImage = fd.askopenfilename()
            etiketResim["text"] = pickedImage

        def threadGonder():
            etiketDurum['text'] = "Durum: Gönderim İşlemi Başladı."
            message = mesaj.get(1.0, END)
            image = etiketResim["text"]

            if varTwitter.get() == 1:
                sender.twitterSendMessage(message, image)
                etiketDurum['text'] = "Durum: Tweet gönderildi. İşlem devam ediyor."

            if varFacebook.get() == 1:
                sender.facebookSendMessage(message, image)
                etiketDurum['text'] = "Durum: Facebook'a gönderildi. İşlem devam ediyor."

            if varInstagram.get() == 1:
                sender.instagramSendMessage(message, image)
                etiketDurum['text'] = "Durum: Instagram'a gönderildi. İşlem devam ediyor."

            etiketDurum['text'] = "Durum: Gönderim işlemi tamamlandı."

        def clickGonder():
            thread = Thread(target=threadGonder)
            thread.start()



        def changeKarakterSay(key):
            mesajMetni = mesaj.get(1.0, END)
            karakterSayisi = len(mesajMetni)

            if karakterSayisi>280:
                print(mesajMetni[0:279])
                mesaj.delete(1.0, END)
                mesaj.insert(END,mesajMetni[0:279])
                karakterSayisi = 10
            etiket1['text'] = "Mesaj: ({}/280)".format(karakterSayisi)

        pencere = Tk()
        pencere.geometry("500x400+300+200")
        pencere.title("Sosyal Ağlara Mesaj Yolla")
        etiket1 = Label(text="Mesaj:")
        etiket1.place(x="40", y="10")

        mesaj = Text(height=5, width=50)
        mesaj.bind("<Key>", changeKarakterSay)
        mesaj.place(x="40", y="40")

        buton = Button(text="Resim Seç", command=clickResimSec)
        buton.place(x="40", y="140", width=100, height=40)

        etiketResim = Label(text="Seçilen resim")
        etiketResim.place(x="160", y="140")

        varTwitter = IntVar()
        chkTwitter = Checkbutton(text="Twitter", variable=varTwitter, onvalue=1, offvalue=0)
        chkTwitter.place(x="40", y="200")

        varFacebook = IntVar()
        chkFacebook = Checkbutton(text="Facebook", variable=varFacebook, onvalue=1, offvalue=0)
        chkFacebook.place(x="140", y="200")

        varInstagram = IntVar()
        chkFacebook = Checkbutton(text="Instagram", variable=varInstagram, onvalue=1, offvalue=0)
        chkFacebook.place(x="240", y="200")

        # butonGonder = Button(text="Gönder", command=lambda: clickGonder(sender))
        butonGonder = Button(text="Gönder", command=clickGonder)
        butonGonder.place(x="40", y="240", width=200, height=40)

        etiketDurum = Label(text="Durum: İşlem Bekleniyor")
        etiketDurum.place(x="40", y="320")

        mainloop()
