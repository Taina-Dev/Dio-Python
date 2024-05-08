from datetime import date, datetime, time, timedelta	
#Obtendo date
data = date(2021, 5, 8)
print(data)
print(date.today())

#Obtendo datetime
data_hora = datetime(2021, 5, 8)
print(data_hora.today())


#Obtendo time
horas = time(10,20,0)
print(horas)

#Obtendo a hora atual
hora_atual = datetime.now().time()
print(hora_atual)

tipo_carro = 'G'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou : {data_atual}  e ficara pronto as {data_estimada}")
elif tipo_carro == 'M':
     data_estimada = data_atual + timedelta(minutes=tempo_medio)
     print(f"O carro chegou : {data_atual}  e ficara pronto as {data_estimada}")
   
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou : {data_atual}  e ficara pronto as {data_estimada}")
  
print(date.today() - timedelta(days=2)) 


data_hora_atual = datetime.now()
data_hora_str = "2024-05-08  10:18"
mascar_ptbr = "%d/%m/%Y - %H:%M:%S"

print(datetime.strftime(mascar_ptbr))

print(datetime.strftime(data_hora_str, mascar_ptbr)) 