from distutils.version import StrictVersion

strEncode = 'utf-8'
luaJITVersion = StrictVersion('2.0.4')

isLe = lambda ver: luaJITVersion > StrictVersion(ver)
isLt = lambda ver: luaJITVersion >=  StrictVersion(ver)