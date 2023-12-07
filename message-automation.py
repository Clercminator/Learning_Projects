import pywhatkit as kit
from schedule import every, repeat, run_pending
import time

message1 = 'Hola mi reina, buenos días. Te amo con todo mi corazón, te deseo un maravilloso día.'
message2 = 'hola mi reina, te amo y te extraño.'
num_Vao = "+5491137977477"

@repeat(every(20).seconds)
def send_message():
    # Send a simple message
    kit.sendwhatmsg_instantly(num_Vao, message2, 7, True,7)

# Schedule a message for a specific time
#kit.sendwhatmsg_to_group_instantly("Lx3Zl2ABjMZHdnDjdBzbVy", "Hola comunidad! Este es un mensaje automatizado para ustedes. Besos en el ano.")

#schedule.every().day.at('22:15').do(send_message)
#schedule.every(75).seconds.do(send_message())
while True:
    run_pending()
    time.sleep(1)
