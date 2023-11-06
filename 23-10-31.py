# 14 paskaita login  ex3
import logging
import time 

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
def consumed_gas(starting_level: int = 50, engine_runing: bool = False) -> int:
    if engine_runing:
        logging.debug(f"consuming gas at this {starting_level} level")
        return starting_level - 5 
    else:
        logging.critical("car can't consume gas, because it's turned off")
        raise ValueError("engine is not running, can't consume gas")
    

def car_toggle_switch(state: bool = False) ->bool:
    if state:
        logging.debug("car was turned on")
        print("start car")
    else:
        logging.debug("car was turned off")
        print("off car")
    return  state

        

def drive() -> None:
    car_state = car_toggle_switch(True)

    gas_level = 30
    logging.debug(f"car has {gas_level} % of fuel")
    while gas_level > 0:
        message = f"wrooom WROOM, I have this much {gas_level} in tank "
        gas_level  = consumed_gas(gas_level, car_state)
        print(message)
        time.sleep(1)
    print("I ran out of gas")
    car_state = car_toggle_switch()
    

drive()