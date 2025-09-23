import os
from nicegui import ui

with ui.row().classes('items-center gap-4'):
    ui.label('Value:')
    val = ui.label('50')
    slider = ui.slider(min=0, max=100, value=50).props('label="Demo slider"')
    slider.on('update:model-value', lambda e: val.set_text(str(int(e.args))))

# keep the websocket alive
ui.timer(20.0, lambda: None)

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 8080)),
        reload=False,
        storage_secret=os.getenv('STORAGE_SECRET', 'change-me'),
    )
