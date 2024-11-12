class Camera:
    def camera_method(self):
        print(f"This is parent camera")
    

class Radio:
    def radio_method(self):
        print(f"This is parent radio")


class MobilePhone(Camera, Radio):
    def mobile_method(self):
        print(f"This is child mobile phone")

