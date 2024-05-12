Para el desarrollo del programa se utilizó la siguiente versión de Python: 3.11.2.

Para la realización del programa se utilizaron dos clases, Call y Bill.

La clase Call consta de dos atributos: duration_of_call y type_of_call, los cuales son parámetros que se almacenarán con los valores que se les asignen al crear una instancia del objeto desde el archivo main.py.

La clase Bill consta de 5 atributos: monthly_payment, call, local_call_cost, national_call_cost e international_call_cost, y 4 métodos: add_call, calculate_call_cost, calculate_total_cost y generate_bill. El atributo monthly_payment se recibe como parámetro del valor que se recibirá al crear una instancia del objeto en main.py.

En el archivo bill.py se declararon 7 variables globales que facilitarán la modificación del código si se cambian las condiciones de los valores de la tarifa de las llamadas locales, además de hacer más legible el código.

También se utilizó PrettyTable, que es un módulo de Python que facilita la creación de tablas ASCII con formato en la consola. Este módulo proporciona una forma sencilla de generar tablas legibles y bien formateadas a partir de datos en listas, diccionarios u otros objetos de datos.
