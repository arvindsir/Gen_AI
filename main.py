from fastapi import FastAPI
app=FastAPI()  #Creating object

@app.get('/home/')    #defines end point function
def home_fun():
    return {'Hello':'Welcome to fast api'}

@app.post('/home/')
def home_fun(name:str,age:int,city:str):      #name may be same or different
    return{"User Name : ":name, "User Age : ":age,"City : ":city}

@app.put('/student_update/')
def student_update(roll_no:int):
    return{'detail':"Studentt update Successfully"}

@app.patch('/student_update/')
def student_update(roll_no:int):
    return {'detail':"student par.. update successfully."}

@app.delete('/student_delete/')
def student_delelte(roll_no:int):
    return{'detail ':" Student Deleted successfully."}

    

