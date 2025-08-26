class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        resultado = ""
        for caracter in texto:
            resultado = caracter + resultado
        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
        contador = 0
        for char in texto:
            if char in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
        contador = 0
        for char in texto:
            if char.isalpha() and char not in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        t1 = sorted(c.lower() for c in texto1 if c.isalnum())
        t2 = sorted(c.lower() for c in texto2 if c.isalnum())
        return t1 == t2
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """

        resultado = ''
        en_palabra = False
    
        for char in texto:
            if char.isalpha():
                if not en_palabra:
                    resultado += char.upper()
                    en_palabra = True
                else:
                    resultado += char
            else:
                resultado += char
                en_palabra = False

        return resultado



    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        tiene_espacio_inicio = texto.startswith(' ')
        tiene_espacio_final = texto.endswith(' ')
        texto_central = ' '.join(texto.strip().split())
        if tiene_espacio_inicio:
            texto_central = ' ' + texto_central
        if tiene_espacio_final:
            texto_central = texto_central + ' '
        return texto_central
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if not texto:
            return False
    
        texto = texto.strip()
        if texto[0] in ('-', '+'):
            texto = texto[1:]
    
        if texto == '':
            return False

        for char in texto:
            if char < '0' or char > '9':
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = []

        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
            
                desplazado = (ord(char) - base + desplazamiento) % 26 + base
                resultado.append(chr(desplazado))
            else:
                resultado.append(char)

        return ''.join(resultado)
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        resultado = ''
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - base - desplazamiento) % 26 + base)
            else:
                resultado += char
        return resultado
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posiciones = []
        len_sub = len(subcadena)
        len_texto = len(texto)
    
        if len_sub == 0 or len_sub > len_texto:
            return posiciones
    
        for i in range(len_texto - len_sub + 1):
            if texto[i:i+len_sub] == subcadena:
                posiciones.append(i)
            
        return posiciones