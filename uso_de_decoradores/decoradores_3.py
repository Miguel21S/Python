
class Conversor:
    
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return f"Conversión de celsius a fahrenheit: {celsius * 1.8 + 32}"
        
    @staticmethod
    def fahrenheit_a_celsius(fahrenheit):
        return f"Conversión de fahrenheit a celsius: {(fahrenheit - 32) * (5 / 9)}" 
    
fah = Conversor.celsius_a_fahrenheit(5)
cel = Conversor.fahrenheit_a_celsius(5)

print(fah)
print(cel)