from utils.dcel import DCEL
from utils.beach_line import BeachLine
from utils.event_queue import EventQueue

def compute_voronoi(points):
    dcel = DCEL()
    beach_line = BeachLine()
    queue = EventQueue(points) # [cite: 330]

    while not queue.is_empty(): # [cite: 331]
        event = queue.pop() # [cite: 337]
        
        if not event.is_valid:
            continue
            
        if event.site:
            handle_site_event(event.site, beach_line, dcel, queue) # [cite: 338]
        else:
            handle_circle_event(event.arc_node, beach_line, dcel, queue) # [cite: 339]

    # Post-processing: aggiungi bounding box per archi infiniti [cite: 341, 342]
    finalize_dcel(dcel)
    return dcel

def handle_site_event(site, beach_line, dcel, queue):
    # 1. Trova l'arco sopra il sito [cite: 361]
    # 2. Rimuovi eventuali circle events falsi [cite: 362]
    # 3. Dividi l'arco e crea nuovi HalfEdge nella DCEL [cite: 363, 367]
    # 4. Controlla nuovi triple di archi per potenziali circle events [cite: 368]
    pass

def handle_circle_event(arc_node, beach_line, dcel, queue):
    # 1. Crea un nuovo vertice nella DCEL (centro del cerchio) [cite: 374]
    # 2. Elimina l'arco dalla beach line e unisci gli HalfEdge [cite: 371, 375, 376]
    # 3. Controlla le nuove triple adiacenti per nuovi circle events [cite: 377, 378]
    pass