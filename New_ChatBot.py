from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pt
import speech_recognition as s
import threading                 # Give Seperate flow of Execution.(2 Things Runs at once.)


engine=pt.init()

def boy():
    voices= engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

def girl():
    voices= engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()
    

Mybot = ChatBot("New_Bot")
database_1= [
'Hello',
'Hii ',
'what is your name?',
'My name is Auto bot , Thanks.',
'what is your age ?',
'I cannot say , Sorry ,',
'Which language do you speak ?',
'I prefer talking in english ',
'how is your day going ?',
'Its Fine , What about you ?',
'I am doing great ',
'Nice to hear that',
'Where do you live ?',
'Currently here only in this pc',
'I love you ',
'Happy to hear that , Thank you',
'Bye ',
'Bye bye , Come back soon',
'What can you do ?',
'Can talk to you , You want to talk with me ?',
'Who created you ?',
'Aakarsh',
'Nice taking to you',
'i also love talking you',
'How are you doing?',
'Actually great, Thanks for asking'
]
trainer= ListTrainer(Mybot)
trainer.train(database_1)
 
main =Tk()
main.geometry("650x850")
main.title("My Chat_Bot")
main['background']="#2A2C2A"    #"#f2efe7"

def mic():
    t=threading.Thread(target = takequery)
    t.start()
    
# ---- Speech Recognition -------
def takequery():
    sr=s.Recognizer( )
    print("Bot is listening ...")
    with s.Microphone() as m:                                                # .microphone() set microphone to accept sound .
        try:
            sr.adjust_for_ambient_noise(m, duration=5)
            audio=sr.listen(m)                                               # listen from source that is m ( microphone) and stores it in audio.
            query = sr.recognize_google(audio,language='en-in')              # converts audio to string.
            print(query)
            textf.insert(0,query)
            ask_bot()
        except Exception as e:
            print(e)
            
# -------------- Bot Functioning ---------

def ask_bot():
    query=textf.get() 
    bot_answer=Mybot.get_response(query)
    mssgs.insert(END, "You : "+query )
    mssgs.insert(END, "Bot : "+ str(bot_answer))
    speak(bot_answer)
    textf.delete(0,END)
    mssgs.yview(END)
    
img_frame=Frame(main)

img= PhotoImage(file="E:\\Update_ChatBOT\\\image\\abcd.png")
label=Label(main,image=img, background="#2A2C2A")
label.pack(pady=0, padx=50)
img_frame.pack()

# ------ Frame 1  -----
frame=Frame(main, background="#868B86")                                   #  GUI's Main Container .
sb=Scrollbar(frame,background="#868B86")
mssgs=Listbox(frame, width=60, height=15 , borderwidth=0 , font=("Times",12) , background="#868B86")

#-------Working ScrollBar-----
mssgs.config(yscrollcommand=sb.set)
sb.config(command=mssgs.yview)

sb.pack(side=RIGHT ,fill=Y ,padx=10)
mssgs.pack(side=LEFT, fill=BOTH) 
frame.pack()

# --- Frame 2---
frame2= Frame(main, height=20, background="#2A2C2A")

text_img=PhotoImage(file="E:\\Update_ChatBOT\\\image\\text.png")
insertf=Label(frame2,image=text_img,background="#2A2C2A")
insertf.pack(side=LEFT , padx=10) 

textf= Entry(frame2, width=45,font=("Times",14,))
textf.pack(side=LEFT ,padx=20) 

frame2.pack(pady=20)

# ---Button---
frame3=Frame(main, background="#2A2C2A")

talk_btn=PhotoImage(file="E:\\Update_ChatBOT\\\image\\Talk3.png")
talk_label=Label(image=talk_btn,background="#2A2C2A")
btn1=Button(frame3, image=talk_btn, command=ask_bot,borderwidth=0,background="#2A2C2A")
btn1.pack(side=LEFT, padx=80 )

# speaker_btn=PhotoImage(file="D:\\Resume's Projects\\Chat Bot\\Images_1\\Speaker.png")
# speaker_label=Label(image=speaker_btn,background="#2A2C2A")
# btn2=Button(frame3, image=speaker_btn, command=ask_bot ,borderwidth=0,background="#2A2C2A")
# btn2.pack(side=LEFT, padx=20)

mic_btn=PhotoImage(file="E:\\Update_ChatBOT\\\image\\Mic1.png")
mic_label=Label(image=mic_btn,background="#2A2C2A")
btn3=Button(frame3, image=mic_btn, command=mic ,borderwidth=0,background="#2A2C2A")
btn3.pack(side=LEFT, padx=20)

framei=Frame(frame3 , background="#2A2C2A")

rlabel=Label(framei,text="CHOOSE VOICE",font=("Times", 14),background="#868B86", borderwidth=0)
rlabel.pack(pady=5)
a =IntVar()
male=PhotoImage(file="E:\\Update_ChatBOT\\\image\\man.png")
female=PhotoImage(file="E:\\Update_ChatBOT\\\image\\woman.png")
r1 = Radiobutton(framei, image=male, variable=a ,value=1, height=52 ,background="#2A2C2A", command=boy,borderwidth=0)
r1.pack(side=LEFT,pady=10, padx=10)
r2 = Radiobutton(framei, image=female, variable=a ,value=2 ,height=50 ,background="#2A2C2A", command=girl,borderwidth=0)
r2.pack( pady=10)

framei.pack()

frame3.pack(fill= BOTH ,pady=20)

def enter_function(event):
    btn1.invoke()

main.bind('<Return>', enter_function) 


main.mainloop()   