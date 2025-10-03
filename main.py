import os
from nicegui import ui, app

MIN_VAL, MAX_VAL = 0, 100

@ui.page('/')
def index():
    with ui.row().classes('items-center gap-4'):
        ui.label('Value (live):')
        live_val = ui.label('50')

        ui.label('Value² (on release):')
        committed_square = ui.label(str(50**2))

    start = app.storage.client.get('value', 50)

    with ui.row().classes('items-center gap-4'):
        value_input = ui.number(
            label='Value', value=start, min=MIN_VAL, max=MAX_VAL, step=1
        ).props('style="width: 8rem"')

        slider = ui.slider(min=MIN_VAL, max=MAX_VAL, value=start).props('label="Demo slider"')

    # --- Handlers ---
    def on_slider_live(e):
        v = int(e.args)
        live_val.set_text(str(v))
        value_input.value = v
        value_input.update()

    def on_slider_release(e):
        v = int(e.args)
        committed_square.set_text(str(v * v))
        app.storage.client.set('value', v)

    def on_input_commit(e):
        v = int(value_input.value)
        # clamp typed value into slider range
        if v < MIN_VAL:
            v = MIN_VAL
        elif v > MAX_VAL:
            v = MAX_VAL
        # reflect clamped value
        value_input.value = v
        value_input.update()
        slider.value = v
        slider.update()
        # treat as commit
        live_val.set_text(str(v))
        committed_square.set_text(str(v * v))
        app.storage.client.set('value', v)

    slider.on('update:model-value', on_slider_live)
    slider.on('change', on_slider_release)
    value_input.on('change', on_input_commit)
    value_input.on('keydown.enter', on_input_commit)

    #ui.timer(20.0, lambda: None)

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 8080)),
        reload=False,
        storage_secret=os.getenv('STORAGE_SECRET', 'change-me'),
    )
