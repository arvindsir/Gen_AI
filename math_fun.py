from fastapi import FastAPI
app=FastAPI()  #Creating object

@app.get('/home/')    #defines end point function
def show_fun():
    return {'Maths_operations':'This is maths function api'}

@app.post('/home/')
def Mahts_fun(n:int,x:int):      #name may be same or different
    f=1
    for i in range(1,n+1):
        f=f*i
    if x % 2 == 0:
        ans='Even'
    else:
        ans='Odd'
    return{"Factorial : ":f, "No. is  : ":ans}