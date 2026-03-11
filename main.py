from fastapi import FastAPI

app = FastAPI() #object created for fastapi class

@app.get("/hey") #path endpoint defined route.

#now we createa  functions for this endpoint
def hello():
    return {'message: hello world'}



@app.get("/about")

def about():
    return{'message': 'This is my second endpoint for learning fastapi'}

