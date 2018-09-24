from time import sleep
#############################
class I2C:

   def __init__(self,address):
	   self.bus = smbus.SMBus(1)
       self.address = address
   def setAddress(self, address)
       self.address = address
   def readReg(self, regNum):
       return self.bus.read_byte_data(self.address,regNum)
	   
   def writeReg(self, regNum, val):
      self.bus.write_byte_data(self.address, regNum, val)  
      
   def read_word(self,reg):
      high = self.bus.read_byte_data(self.address, reg)
      low = self.bus.read_byte_data(self.address, reg + 1)
      return (high << 8) + low
	  
   def read_word_2c(self,reg):
       val = self.read_word(reg)
       if (val >= 0x8000):
          return -((65535 - val) + 1)
       else:
          return val
#############################


#############################          
class MPU6050(I2C):
    def __init__(self):
        I2C.__init__(self,0x68)
    def reset(self):
        devReset = 0x89
        I2C.writeReg(107, devReset):
        # Todo, datasheet says that this should be done for SPI interface... I2C?
     def setGyroConfig(selfTests, FullScallSelect)
        if selfTests > 0:
            # Todo self test logic
        I2C.writeReg(0x1B, 0): # no self test , 250 deg/s
     def performSelfTest():
     # 1B
        I2C.writeReg(0x1B, 0xE0): # Enable self test for gyros
        I2C.writeReg
        self.SelfTestResponse = I2C.readReg(0x0D) & 0x1f
     def get_gyro_FT_Values():
        XG_Test = I2C.readReg(0x0D) & 0x1f
        YG_Test = I2C.readReg(0x0E) & 0x1f
        ZG_Test = I2C.readReg(0x0F) & 0x1f
        
        if XG_Test != 0:
            XG_Test = 25*131*(pow(1.046,(XG_Test - 1)
        
        if YG_Test != 0:
            YG_Test = -25*131*(pow(1.046,(YG_Test - 1)
        
        if ZG_Test != 0:
            ZG_Test = 25*131*(pow(1.046,(ZG_Test - 1)
            
        self.FT_Xg = XG_Test
        self.FT_Yg = YG_Test
        self.FT_Zg = ZG_Test

def dist(a,b):
   return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
   radians = math.atan2(x, dist(y,z))
   return (-math.degrees(radians))

def get_x_rotation(x,y,z):
   radians = math.atan2(y, dist(x,z))
   return math.degrees(radians)

def get_z_rotation(x,y,z):
   radians = math.atan2(z, dist(x,y))
   return math.degrees(radians)
#############################