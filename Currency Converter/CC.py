from tkinter import*
from requests import*

root = Tk()
root.title("Currency Converter App")
root.configure(bg = "light blue")
root.geometry("1200x1000+600+200")
f = ("Arial",40,"bold")

def convert():
	try:
		air = float(ent_amt.get())
		url ="https://api.exchangerate-api.com/v4/latest/INR"
		res = get(url)
		data = res.json()
		rates = data["rates"]["GBP"]
		aip = air*rates
		msg = "£" + str(round(aip,2))
		lab_msg.configure(text=msg)
	except ValueError:
		msg = "invalid amt"
		lab_msg.configure(text=msg)


lab_header = Label(root,text="INR To UK",font=f)
lab_amt = Label(root,text="enter amt in ₹",font=f)
ent_amt = Entry(root,font=f)
btn_convert = Button(root,text="Convert",font=f,command=convert)
lab_msg = Label(root,font=f)

lab_header.pack(pady=10)
lab_amt.pack(pady=10)
ent_amt.pack(pady=10)
btn_convert.pack(pady=10)
lab_msg.pack(pady=10)
root.mainloop()