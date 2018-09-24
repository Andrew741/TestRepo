import smbus
import MPU6050
from time import sleep

class offset:
  def  __init__(self, gx, gy, gz, ax, ay, az):
      self.gx = gx
      self.gy = gy
      self.gz = gz
      self.ax = ax
      self.ay = ay
      self.az = az
def calibrate():
   g_xout = 0
   g_yout = 0
   g_zout = 0
   a_xout = 0
   a_yout = 0
   a_zout = 0
   
   NUM_SAMPLES = 20
   Sample_Period = .5
   for i in range(0,NUM_SAMPLES):
      g_xout = g_xout + read_word_2c(0x43)
      g_yout = g_yout + read_word_2c(0x45)
      g_zout = g_zout + read_word_2c(0x47)
      a_xout = a_xout + read_word_2c(0x3b)
      a_yout = a_xout + read_word_2c(0x3d)
      a_zout = a_xout + read_word_2c(0x3f)
      sleep(Sample_Period)
     
   print('calibration complete')
   
   g_xout = g_xout / NUM_SAMPLES
   g_yout = g_yout / NUM_SAMPLES
   g_zout = g_zout / NUM_SAMPLES
   a_xout = a_xout / NUM_SAMPLES
   a_yout = a_yout / NUM_SAMPLES
   a_zout = a_zout / NUM_SAMPLES
   print('x {0} {1}'.format(g_xout,a_xout))
   print('y {0} {1}'.format(g_yout,a_yout))
   print('z {0} {1}'.format(g_zout,a_zout))
   
   offsets = offset(g_xout, g_yout, g_zout, a_xout, a_yout, a_zout)

   return offsets
def run(offsets):
    g_xout = read_word_2c(0x43) - offsets.gx
    g_yout = read_word_2c(0x45) - offsets.gy
    g_zout = read_word_2c(0x47) - offsets.gz
    a_xout = read_word_2c(0x3b) - offsets.ax
    a_yout = read_word_2c(0x3d) - offsets.ay
    a_zout = read_word_2c(0x3f) - offsets.az
    
    print('x {0} {1}'.format(g_xout,a_xout))
    print('y {0} {1}'.format(g_yout,a_yout))
    print('z {0} {1}'.format(g_zout,a_zout))
   
'''


print('Gyroscope')
print('---------')
run(calibrate())
 '''
'''
while(True):
   g_xout = read_word_2c(0x43)
   g_yout = read_word_2c(0x45)
   g_zout = read_word_2c(0x47)
   a_xout = read_word_2c(0x3b)
   a_yout = read_word_2c(0x3d)
   a_zout = read_word_2c(0x3f)

   print('x {0} {1} | {2} {3} : {4}'.format(g_xout, g_xout/131,a_xout,  a_xout /16384 ,get_x_rotation(g_xout, g_yout, g_zout)))
   print('y {0} {1} | {2} {3} : {4}'.format(g_yout, g_yout/131,a_yout,  a_yout /16384 ,get_y_rotation(g_xout, g_yout, g_zout)))
   print('z {0} {1} | {2} {3} : {4}'.format(g_zout, g_zout/131,a_zout,  a_zout /16384,get_y_rotation(g_xout, g_yout, g_zout)))

   sleep(1)
'''
