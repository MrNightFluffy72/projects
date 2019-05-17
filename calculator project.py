from tkinter import

def iCalc(source, side):
	storeObj = Frame(source, borderwidth = 1, bd= 4 bg="powder blue"
	storeObj.pack(side=side, expand=YES, fill=BOTH)
	return storeObj

def button (source, side, text, command = None):
	storeObj = Button(source, text=text, command=command)
	storeObj.pack(side=side, expand=YES, fill=BOTH)
	return storeObj

class app(frame):
	def __init__(self):
		Frame.__init__(self)
		self.option_add('*font', 'arial 20 bold')
		self.pack(expand=YES, fill=BOTH)
		self.master.title('calculator')

		display = stingVar()
		Entry(self, relief=RIDGE,
				textvarible=display,justify='right',bd=30,bg="powder blue").pack(side=TOP, expand=YES, fill=BOTH)

		for clearBut in (["ce"], ["c"]):
			erase = iCalc(self, TOP)
			for ichar in clearBut:
				button(erase, LEFT, ichar,
						lambda storeObj=display, q=ichar: storeObj.set(''))

		for numBut in ("789/", "456*", "123-", "0.+"):
			FunctionNum = iCalc(self, TOP)
			for char in NumBut:
				button(FunctionNum, LEFT, char,
						lambda storeObj=display, q=char: storeObj.set(stireObj.get() + q))

		EqualButton = iCalc(self, TOP)
		for iEquals in "="
			if iEquals == "=":
				btniEquals = button(EqualsButton, LEFT iEquals)
				btniEquals.bind ('<ButonRelase-1>',
						lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
			else:
				btniEquals = button(EqualsButton, LEFT iEquals,
					lambda storeObj=display, s= %s '%iEquals: storeObj.set(storeObj.get()+s))
