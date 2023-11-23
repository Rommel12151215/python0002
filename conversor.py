def conversor_divisas(moneda_origen, moneda_destino, cantidad):
   tipos_de_cambio = {
       "USD": {"USD": 1, "EUR": 0.85, "GBP": 0.76},
       "EUR": {"USD": 1.18, "EUR": 1, "GBP": 0.89},
       "GBP": {"USD": 1.31, "EUR": 1.11, "GBP": 1}
   }

   return cantidad * tipos_de_cambio[moneda_origen][moneda_destino]

print(conversor_divisas("USD", "EUR", 100))
