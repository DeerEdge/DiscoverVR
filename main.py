from nicegui import ui
import time
ui.add_head_html('<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />')

# Create the header
with ui.header().classes(replace='row items-center justify-between') as header:
    ui.icon('auto_stories').classes('q-px-md text-4xl')
    ui.label('Quasar').classes('text-h4 q-mr-n-lg')
    with ui.tabs().classes('ml-auto q-pa-md text-lg') as tabs:
        ui.tab('Home')
        ui.tab('Resources')
        ui.tab('About')
        ui.tab('Demo')

    ui.button(icon='eva-github')

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('Home'):
        ui.label('Featured Applications').classes('text-h6 q-px-md')
        with ui.row().classes('q-gutter-md'):
            # Card 1: Embedding an image and description
            with ui.card().classes('q-pa-md').style('width: 33%'):  # Ensure 3 cards wide
                ui.image('https://example.com/image1.jpg').classes('thumbnail')
                ui.label('Title 1').classes('text-h6 q-mt-md')
                ui.label('This is a description for the first card. It gives more details about the content.')

            # Card 2: Embedding an HTML iframe and description
            with ui.card().classes('q-pa-md').style('width: 33%'):
                ui.html('''
                    <iframe src="https://yourcontent.com" width="100%" height="150px"></iframe>
                ''')
                ui.label('Title 2').classes('text-h6 q-mt-md')
                ui.label('This card contains embedded HTML content, like an iframe or another web app.')

            # Card 3: Another image and description
            with ui.card().classes('q-pa-md').style('width: 33%'):
                ui.image('https://example.com/image3.jpg').classes('thumbnail')
                ui.label('Title 3').classes('text-h6 q-mt-md')
                ui.label('This is the third card, which features another image and a short description.')

        # Footer
    with ui.tab_panel('Resources'):
        ui.label('Content of B')
    with ui.tab_panel('About'):
        ui.label('Content of C')
    with ui.tab_panel('Docs'):
        ui.label('Content of C')

ui.run()


# with ui.footer(value=False) as footer:
#     ui.label('Footer')
#
# with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
#     ui.button(on_click=footer.toggle, icon='contact_support').props('fab')