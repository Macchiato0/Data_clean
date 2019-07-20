__slot__

#ues "__slot__ " to reserve just enough space for every instance and "__dict__" will be not created
#use less memory
#fast attribute access
#inheritace is tricky
#use iterators instead

class sansSlots:
    def __init__(self,red_foo,sky_blu):
    self.red_foo=red_foo
    self.sky_blu= sky_blu

sans=sansSlots(42,3)

class AdvanceSlots:
    __slot__=['red_foo','sky_blu']    
 
    def __init__(self,red_foo,sky_blu):
    self.red_foo=red_foo
    self.sky_blu= sky_blu

avec=AdvanceSlots(42,4)
