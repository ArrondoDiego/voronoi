class BeachNode:
    def __init__(self, site, is_leaf=False):
        self.is_leaf = is_leaf
        self.site = site        # Se foglia: il sito della parabola [cite: 274]
        self.sites = None       # Se nodo interno: coppia <pi, pj> per il breakpoint [cite: 276]
        
        self.left = None
        self.right = None
        self.parent = None
        
        self.edge = None        # Pointer all'HalfEdge della DCEL tracciato dal breakpoint [cite: 288, 289]
        self.circle_event = None # Pointer all'evento nel Q se l'arco deve sparire [cite: 286]



    def get_breakpoint_x(self, p_left, p_right, sweep_y):
        """
        Risolve l'intersezione tra la parabola del sito p_left e p_right
        data la posizione attuale della sweep line (sweep_y).
        """
        s1 = p_left
        s2 = p_right
        
        # Caso degenere: se la sweep line è esattamente sul sito
        # (Capita spesso all'inizio di un Site Event)
        if s1.y == sweep_y:
            return s1.x
        if s2.y == sweep_y:
            return s2.x

        # Coefficienti per la formula risolutiva dell'equazione di 2° grado: ax^2 + bx + c = 0
        # Derivati dall'uguaglianza delle due equazioni paraboliche
        
        # h1 e h2 sono le distanze verticali dai fuochi alla direttrice
        h1 = 2.0 * (s1.y - sweep_y)
        h2 = 2.0 * (s2.y - sweep_y)
        
        # Trasformiamo l'uguaglianza in forma quadratica
        a = 1.0/h1 - 1.0/h2
        b = -2.0 * (s1.x/h1 - s2.x/h2)
        c = (s1.x**2 + s1.y**2 - sweep_y**2)/h1 - (s2.x**2 + s2.y**2 - sweep_y**2)/h2
        
        # Risolviamo l'equazione: x = (-b +/- sqrt(b^2 - 4ac)) / 2a
        if a != 0:
            disc = b**2 - 4*a*c
            if disc < 0: disc = 0 # Tolleranza numerica
            sqrt_disc = math.sqrt(disc)
            
            x1 = (-b + sqrt_disc) / (2*a)
            x2 = (-b - sqrt_disc) / (2*a)
            
            # Scegliamo la radice corretta:
            # Se il sito di sinistra è più in alto di quello di destra,
            # il breakpoint che ci interessa è quello con la coordinata x corretta
            # rispetto all'ordine dei nodi nell'albero.
            if s1.y < s2.y:
                return max(x1, x2)
            else:
                return min(x1, x2)
        else:
            # Se a == 0, le parabole hanno la stessa apertura (s1.y == s2.y)
            # L'equazione diventa lineare: bx + c = 0
            return -c / b

class BeachLine:
    def __init__(self):
        self.root = None

    def find_arc_above(self, new_site):
        # Cerca nell'albero l'arco (foglia) verticalmente sopra il nuovo sito [cite: 282, 361]
        pass

    def split_arc(self, arc_node, new_site):
        # Quando un nuovo sito colpisce un arco, questo si divide in tre [cite: 363, 364]
        # Esempio: arc(pi) diventa arc(pi) - arc(new) - arc(pi)
        pass

    def remove_arc(self, arc_node, vertex):
        # Rimuove un arco quando scatta un Circle Event [cite: 371]
        pass