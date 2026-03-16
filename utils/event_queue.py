import heapq

class Event:
    def __init__(self, y, x, site=None, arc_node=None):
        self.y = y             # Priorità: y del sito o punto più basso del cerchio [cite: 290, 292]
        self.x = x
        self.site = site       # Se presente, è un Site Event [cite: 291]
        self.arc_node = arc_node # Se presente, l'arco che scompare (Circle Event) [cite: 292]
        self.is_valid = True   # Per gestire i "false alarms" [cite: 302, 306]

    def __lt__(self, other):
        return self.y > other.y # Fortune va dall'alto verso il basso

class EventQueue:
    def __init__(self, sites):
        self.queue = []
        # Inizializza con tutti i Site Events noti in anticipo [cite: 291, 330]
        for s in sites:
            heapq.heappush(self.queue, Event(s.y, s.x, site=s))

    def pop(self):
        return heapq.heappop(self.queue)

    def push_circle_event(self, pi, pj, pk, arc_node):
        # Calcola se i tre siti formano un cerchio e aggiungi l'evento [cite: 305, 309]
        pass