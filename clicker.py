import pyautogui as pag
n1 = pag.prompt(text='How many clicks?', title='Enter a number' , default=5)
n=int(n1)
time1 = pag.prompt(text='Time between clicks?', title='Enter a number', default=0.5)
time = float(time1)
pag.alert(text='Move the mouse to click location and press ENTER', title='Set-up', button='OK')
x1,y1 = pag.position()
while n > 0:
    pag.click(x=x1, y=y1, button='left')
    n = n-1
    pag.PAUSE = time
