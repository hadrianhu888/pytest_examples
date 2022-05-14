import vehicle_behavior as vb 

def test_vehicle_start():
    assert vb.vehicle_start() == 1
    
def test_vehicle_accessories():
    assert vb.vehicle_accessories() == 2

def test_vehicle_crank(): 
    assert vb.vehicle_crank() == 3

def test_vehicle_power_mode(): 
    assert vb.vehicle_power_mode('neutral') == 'neutral'
    
def test_vehicle_speed(): 
    assert vb.vehicle_speed(7) == 70

def test_vehicle_soc(): 
    assert vb.vehicle_soc() == 0.7
    
def test_vehicle_charge(): 
    assert vb.vehicle_charge() == True

def test_vehicle_drive():
    assert vb.vehicle_drive() == True 

