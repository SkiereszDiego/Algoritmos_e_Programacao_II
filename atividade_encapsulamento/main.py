from Pessoa import Pessoa
from Juridica import Juridica
from Fisica import Fisica


pf1 = Fisica(1, 'Cleber', 'POA', 123456789, '12345678910', 28, 65, 1.75)
pf1.imprimeCPF()
pf1.__calculaIMC()

pj1= Juridica(1, 'JojaMart', 'PelicanTown', 666666666, '1366613666', 1234567890, 15)
pj1.imprimeCNPJ()