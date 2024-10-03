from event import EventEmitter,NotificationService, Order

event_emitter = EventEmitter()

notfication_service = NotificationService(event_emitter)
order = Order(event_emitter)

#złożenie zamówinia
order.place_order(456)
