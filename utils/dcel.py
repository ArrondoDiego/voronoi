class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.incident_edge = None # Un HalfEdge che ha questo vertice come origine

class Face:
    def __init__(self, site):
        self.site = site # Il punto generatore (Point)
        self.outer_component = None # Un HalfEdge che delimita questa cella [cite: 352]

class HalfEdge:
    def __init__(self, face):
        self.origin = None      # Vertice di partenza
        self.twin = None        # L'half-edge opposto
        self.incident_face = face 
        self.next = None        # Successivo in senso antiorario [cite: 477]
        self.prev = None        # Precedente
        
        # Nota: l'equazione del bisettore è implicita tra la faccia attuale 
        # e la faccia del twin [cite: 476]

class DCEL:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.faces = []

    def create_vertex(self, x, y):
        # Crea e aggiunge un vertice alla lista
        pass

    def create_edge_pair(self, face_left, face_right):
        # Metodo fondamentale: crea una coppia di HalfEdge (twin) 
        # e li collega alle rispettive facce [cite: 367]
        pass