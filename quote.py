# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 23:46:39 2020

@author: 33667
"""

class Quote:
    def __init__(self, close, coupon, date, gross, high, low, nav, ope, pl, ret, volume):
        self.close = close
        self.coupon = coupon  
        self.gross = gross
        self.high = high
        self.low = low 
        self.nav = nav
        self.ope = ope
        self.pl = pl
        self.ret = ret
        self.volume = volume

#gets      
    def get_close(self):
        return self.close
    
    def get_coupon(self):
        return self.coupon
    
    def get_date(self):
        return self.date
    
    def get_gross(self):
        return self.gross
    
    def get_high(self):
        return self.high
    
    def get_low(self):
        return self.low
    
    def get_nav(self):
        return self.nav
    
    def get_ope(self):
        return self.ope
    
    def get_pl(self):
        return self.pl
    
    def get_ret(self):
        return self.ret
    
    def get_volume(self):
        return self.volume 
    
#sets
    def set_close(self, close):
        self.close = close
    
    def set_coupon(self, coupon):
        self.coupon = coupon
        
    def set_date(self, date):
        self.date = date
        
    def set_gross(self, gross):
        self.gross = gross
    
    def set_high(self, high):
        self.high = high
        
    def set_low(self, low):
        self.low = low
        
    def set_nave(self, nave):
        self.nave = nave
    
    def set_ope(self, ope):
        self.ope = ope
        
    def set_pl(self, pl):
        self.pl = pl
        
    def set_ret(self, ret):
        self.ret = ret
    
    def set_volume(self, volume):
        self.volume = volume
        
        
#dels     
    def del_id(self):
        del(self.id)
    
    def del_close(self):
        del(self.close)
    
    def del_coupon(self):
        del(self.coupon)
        
    def del_date(self):
        del(self.date)
        
    def del_gross(self, gross):
        del(self.gross)
    
    def del_high(self):
        del(self.high)
        
    def del_low(self):
        del(self.low)
        
    def del_nave(self):
        del(self.nave)
    
    def del_ope(self):
        del(self.ope)
        
    def del_pl(self):
        del(self.pl)
        
    def del_ret(self):
        del(self.ret)
    
    def del_volume(self):
        del(self.volume)
