
class Configs:
    __intstance = None
    def __new__(cls,*args,**kwargs):
        if cls.__intstance is None:
            cls.__intstance = super(Configs,cls).__new__(cls)
            cls.url = {
                1:'https://www.wilson.com/en-us/explore/basketball/airless-prototype'
            }
        return cls.__intstance
    
    @classmethod
    def get_url(cls,key):
        return cls.__intstance.url.get(key)
    



  def start_browser(self):
        try:
            #for i in Configs.get_url(cls=Configs,key=1):
            val = Configs.get_url(cls=Configs,key=1)
            self.driver.get(val)
            WDW(self.driver,10).until(
            EC.url_to_be(val))
        except (WebDriverException, TimeoutException) as err:
            logging.error(f'Error navigating to URL: {err.args}')
