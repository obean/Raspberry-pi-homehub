from guizero import App, Text, TextBox, PushButton, Slider,  Box
from sensorhub.hub import SensorHub
app = App( title="HomeHub", width=425)
app.full_screen = True
hub = SensorHub()

def how_hot_is_chip():
    current_temp = str(hub.get_temperature())
    chip_temp.value = "Onboard Temp \n" + current_temp +"°C"
    
def how_bright():
    current_lumens = str(hub.get_brightness())
    light.value = "Brightness: \n" + current_lumens + " Lumens"
    
def gone_dark():
    current_lumens = hub.get_brightness()
    if current_lumens == 0:
        light.value = "hey, who turned out the lights"
        
def how_hot_is_room():
    env_temp = str(hub.get_off_board_temperature())
    room_temp.value = "Room Temp: \n" + env_temp+"°C"

def are_you_too_hot():
    if hub.get_off_board_temperature < 25
        app.yesno("temp is above normal", "Do you want to turn on the fan?")
    
    

welcome_message_box = Box(app, align='top', width='fill')# border=True)
cur_env_box =Box(app, border=True, width='fill')

#text_size = Slider(app, command=change_text_size, start=10, end=80)

chip_temp = Text(cur_env_box, text="Checking...", align='right', size=15, color="black")

light = Text(cur_env_box, text="Checking...",align='left', size=15)#, color='red'

room_temp = Text(cur_env_box, text='Checking...', size=15)

#check_temp = PushButton(app, command=how_hot_is_chip, align='left', text="Check Chip Temp")



#my_name = TextBox(app)
chip_temp.repeat(5000, how_hot_is_chip)
light.repeat(1000, how_bright)
light.repeat(1000, gone_dark)
room_temp.repeat(5000, how_hot_is_room)





app.display()
