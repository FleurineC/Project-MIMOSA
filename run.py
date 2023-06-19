from model.mimosa import MIMOSA

from model.common.config import parseconfig

params = parseconfig.load_params()
params["emissions"]["carbonbudget"] = False
params["emissions"]["burden_sharing_regime"] = "GF"

model1 = MIMOSA(params)
model1.solve()
model1.save("GF")