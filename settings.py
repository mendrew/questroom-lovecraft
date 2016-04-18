class Devices:
    DEVICE = "DEVICE"
    LOVECRAFT_DEVICE_NAME = "LOVECRAFT_DEVICE_NAME"
    LOVECRAFT_USB_SERIAL_NUMBER = "A4033KK5"
    LOVECRAFT_DEVICE_COM_PORT_WIN = "COM3"

class Buttons:
    # CASKET_BOX =  # "Ящик под картиной?"
    pass

class DEVICES_TABLE:
    #ADC
    ADC_LORDS_TABLE_STATUE = 0
    LORDS_TABLE_STATUE_RANGE = (20, 60)

    COIN_1 = 1
    COIN_2 = 2
    COIN_3 = 3
    COIN_4 = 4
    COIN_INSERTED_RANGE = (20, 60)

    RELAY_GODS_TABLE_MOTOR = 2
    RELAY_PUSH = 4

class TASKS_IDS:
    PUT_STATUE_ON_LORDS_TABLE = 1
    PUT_FIRST_COIN = 2


class Global:
    SCENARY_FILE = "full_quest.yml"
    GET_TTY_USB_SCRIPT = "./get_ttyUSB.sh"
    INIT_TASK_ID = 0


