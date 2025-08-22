class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
    
      """
    def piedra_papel_tijera(self, jugador1, jugador2):
        j1 = str(jugador1).strip().lower()
        j2 = str(jugador2).strip().lower()
        opciones = {"piedra", "papel", "tijera"}

        if j1 not in opciones or j2 not in opciones:
            return "invalid"

        if j1 == j2:
            return "empate"

        if (j1, j2) in {("piedra", "tijera"), ("tijera", "papel"), ("papel", "piedra")}:
            return "jugador1"

        return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
              
    def ta_te_ti_ganador(self, tablero):
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        for col in range(3):
            if tablero[0][col] != " " and tablero[0][col] == tablero[1][col] == tablero[2][col]:
                return tablero[0][col]

        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            if all(" " not in fila for fila in tablero):
                return tablero[0][0]
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            if all(" " not in fila for fila in tablero):
                return tablero[0][2]

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"


        
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        import random
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
   
    def validar_movimiento_torre_ajedrez(self, x1, y1, x2, y2, tablero):
        if not (0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8):
            return False

        if x1 == x2 and y1 == y2:
            return False

        if x1 == x2:
            paso = 1 if y2 > y1 else -1
            for y in range(y1 + paso, y2, paso):
                if tablero[x1][y] != " ":
                    return False
            return True

        if y1 == y2:
            paso = 1 if x2 > x1 else -1
            for x in range(x1 + paso, x2, paso):
                if tablero[x][y1] != " ":
                    return False
            return True
        return False








