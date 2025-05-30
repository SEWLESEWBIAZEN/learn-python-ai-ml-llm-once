from datetime import datetime
import time
# Accept the event date from the user
def get_event_date():
    try:
        event_date = input("Enter event date: (YYYY-MM-DD HH:MM:SS)")     
        return datetime.strptime(event_date, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print("error occured: ", e)
        return None

# get time remaining
def get_time_left(event_time):              
        today = datetime.now()        
        time_left = event_time - today
        return time_left

# display counting down
def get_counting_down(time_left):   
        days=time_left.days    
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder,60)        
        print(f"Time Remaining: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")

# main function, entry of th app
def main(): 
    event_date = get_event_date()
    if not event_date:
        print("Invalid format please enter again.")
        main()
    while True:
        time_left = get_time_left(event_date) 
        if time_left.total_seconds() <=0:
            return            
        get_counting_down(time_left)
        time.sleep(1)       

# calling the main function
main()
