class Colors:
        grey = (192, 192, 192)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue =  (0, 0, 255)
        pynk = (255, 0 , 255)
        yellow = (255, 255, 0)
        cyan = (0, 255, 255)

        @classmethod
        def get_cell_colors(cls):
    
            return [ cls.grey, cls.red, cls.green, cls.blue,  cls.pynk, cls.yellow, cls.cyan]