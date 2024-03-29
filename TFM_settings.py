# 
import dynaconf

a=dynaconf.Dynaconf('set.ini')
print(a.configure())