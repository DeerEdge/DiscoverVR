from nicegui import ui
ui.add_head_html('<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />')

with ui.header().classes(replace='row items-center justify-between q-py-md') as header:
    ui.label('My Website').classes('text-h4 q-px-md')
    with ui.tabs().classes('ml-auto text-lg') as tabs:
        ui.tab('Home')
        ui.tab('Resources')
        ui.tab('About')
        ui.tab('Demo')

    ui.button(icon='eva-github')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('Home'):
        ui.label('Content of A')
    with ui.tab_panel('Resources'):
        ui.label('Content of B')
    with ui.tab_panel('About'):
        ui.label('Content of C')
    with ui.tab_panel('Docs'):
        ui.label('Content of C')

ui.run()
