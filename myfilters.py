from app import app
import datetime


x = datetime.datetime(2020, 5, 17)




@app.template_filter('laz')
def laz(x):
    return x.strftime("%b-%d-%y %I:%M %p")
    #return x.strftime("%B %d, %Y") 



laz(x)







#date_without_hour = task.date.strftime("%B %d, %Y")






    