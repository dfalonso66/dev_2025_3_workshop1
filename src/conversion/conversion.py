class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        return (celsius * 9 / 5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        return (fahrenheit - 32) * 5 / 9
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
    def metros_a_pies(self, metros):
        return metros * 3.28084

    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
    def pies_a_metros(self, pies):
        return pies * 0.3048

    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
    def decimal_a_binario(self, decimal):
        return bin(decimal)[2:]

    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
    def binario_a_decimal(self, binario):
        return int(binario, 2)

    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
    def decimal_a_romano(self, numero):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        romanos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
        resultado = ""
        for i in range(len(val)):
            while numero >= val[i]:
                resultado += romanos[i]
                numero -= val[i]
        return resultado

    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
    def romano_a_decimal(self, romano):
        valores = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        anterior = 0

        for letra in reversed(romano):
            valor = valores[letra]
            if valor < anterior:
                total -= valor
            else:
                total += valor
                anterior = valor

        return total

    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
    def texto_a_morse(self, texto):
        morse = {
            'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.',
            'G': '--.',   'H': '....',  'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
            'M': '--',    'N': '-.',    'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...',   'T': '-',     'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
            'Y': '-.--',  'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---','3': '...--','4': '....-',
            '5': '.....', '6': '-....', '7': '--...','8': '---..','9': '----.'
        }

        texto = texto.upper()
        return ' '.join(morse[c] for c in texto if c in morse)

    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
    def morse_a_texto(self, morse):
        morse_dict = {
            '.-': 'A',    '-...': 'B',  '-.-.': 'C', '-..': 'D',  '.': 'E',    '..-.': 'F',
            '--.': 'G',   '....': 'H',  '..': 'I',   '.---': 'J', '-.-': 'K',  '.-..': 'L',
            '--': 'M',    '-.': 'N',    '---': 'O',  '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S',   '-': 'T',     '..-': 'U',  '...-': 'V', '.--': 'W',  '-..-': 'X',
            '-.--': 'Y',  '--..': 'Z',
            '-----': '0', '.----': '1', '..---': '2','...--': '3','....-': '4',
            '.....': '5', '-....': '6', '--...': '7','---..': '8','----.': '9'
        }

        letras = morse.split()
        return ''.join(morse_dict[codigo] for codigo in letras if codigo in morse_dict)
