import os
from nicegui import ui, app

@ui.page('/')
def index():
    with ui.row().classes('items-center gap-4'):
        ui.label('Value:')

        # get per-client initial value (default 50 if not set)
        start = app.storage.client.get('value', 50)
        val = ui.label(str(start))

        slider = ui.slider(min=0, max=100, value=start).props('label="Demo slider"')

        def on_change(e):
            v = int(e.args)
            val.set_text(str(v))
            app.storage.client.set('value', v)

        slider.on('update:model-value', on_change)

    # keep the websocket alive
    ui.timer(20.0, lambda: None)

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 8080)),
        reload=False,
        storage_secret=os.getenv('STORAGE_SECRET', 'change-me'),
    )
