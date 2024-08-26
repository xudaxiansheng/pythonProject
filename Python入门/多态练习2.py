# 空调AC的抽象类
class AC:
    # 冷风
    def cool_wind(self):
        pass

    # 热风
    def hot_wind(self):
        pass

    # 左右吹风
    def wind_l_r(self):
        pass


# 美的空调子类实现
class Meidi(AC):
    def cool_wind(self):
        print('美的空调，科技制冷')

    def hot_wind(self):
        print('美的空调，快速制热')

    def wind_l_r(self):
        print('美的空调，左右吹风')


# 格力空调子类实现
class Gree(AC):
    def cool_wind(self):
        print('格力空调，玄学制冷')

    def hot_wind(self):
        print('格力空调，迅速制热')

    def wind_l_r(self):
        print('格力空调，左右摆风')


# 多态实现函数

def ac_coll(ac: AC):
    ac.cool_wind()

meidi = Meidi()
gree = Gree()
ac_coll(meidi)
ac_coll(gree)