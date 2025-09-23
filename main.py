# main.py
import os
from nicegui import ui

@ui.page('/')  # each visitor gets an isolated component tree
def index():
    with ui.row().classes('items-center gap-4'):
        ui.label('Value:')
        val = ui.label('50')

        # per-client initial value (optional: remember per browser)
        start = ui.storage.client.get('value', 50)

        slider = ui.slider(min=0, max=100, value=start).props('label="Demo slider"')

        def on_change(e):
            v = int(e.args)
            val.set_text(str(v))
            ui.storage.client.set('value', v)  # persists per browser (cookie-based)

        slider.on('update:model-value', on_change)

    # keep the websocket alive (helps on some hosts)
    ui.timer(20.0, lambda: None)

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 8080)),
        reload=False,
        storage_secret=os.getenv('STORAGE_SECRET', 'change-me'),
    )
