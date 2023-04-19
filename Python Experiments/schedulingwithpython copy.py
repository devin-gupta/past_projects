import schedule, time

def reminder_to_sleep():
    print("this worked on time")

schedule.every().friday.at("01:57").do(reminder_to_sleep)

while True:
    schedule.run_pending()
    time.sleep(1)