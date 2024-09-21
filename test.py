
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
                ui.html('''
                                    <iframe src="https://deeredge.github.io/frame1/" width="100%" height="200px"></iframe>
                                ''')
                ui.label('Title 1').classes('text-h6 q-mt-md')
                ui.label('This is a description for the first card. It gives more details about the content.')

            # Card 2: Embedding an HTML iframe and description
            with ui.card().classes('q-pa-md').style('width: 33%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/frame1/" width="100%" height="200px"></iframe>
                ''')
                ui.label('Title 2').classes('text-h6 q-mt-md')
                ui.label('This card contains embedded HTML content, like an iframe or another web app.')

            # Card 3: Another image and description
            with ui.card().classes('q-pa-md').style('width: 33%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/frame1/" width="100%" height="200px"></iframe>
                ''')
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

#!/usr/bin/env python3
from nicegui import ui
from router import Router

ui.add_head_html('<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />')


@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page(
    '/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page
def main():
    router = Router()

    @router.add('/')
    def show_home():
        ui.label('Featured Applications').classes('text-h6 q-px-md q-pt-md')
        with ui.row().classes('q-gutter-md q-px-md'):  # Added q-px-md for left padding
            # Card 1
            with ui.card().classes('q-pa-sm').style('width: 31%'):  # Changed to q-pa-sm for less internal padding
                ui.html('''
                    <iframe src="https://deeredge.github.io/frame1/" width="400px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('Title 1').classes('text-h6 q-mt-sm')
                ui.label('This is a description for the first card. It gives more details about the content.')

            # Card 2
            with ui.card().classes('q-pa-sm').style('width: 31%'):  # Changed to q-pa-sm for less internal padding
                ui.html('''
                            <iframe src="https://deeredge.github.io/frame1/" width="400px" height="200px"></iframe>
                        ''').style('padding: 8px;')
                ui.label('Title 1').classes('text-h6 q-mt-sm')
                ui.label('This is a description for the first card. It gives more details about the content.')

            # Card 3
            with ui.card().classes('q-pa-sm').style('width: 31%'):
                ui.html('''
                            <iframe src="https://deeredge.github.io/frame1/" width="400px" height="200px"></iframe>
                        ''').style('padding: 8px;')
                ui.label('Title 1').classes('text-h6 q-mt-sm')
                ui.label('This is a description for the first card. It gives more details about the content.')

    @router.add('/resources')
    def show_resources():
        with ui.column().classes('w-full'):
            ui.label('Resources Content').classes('text-2xl')

    @router.add('/about')
    def show_about():
        with ui.column().classes('w-full'):
            ui.label('About Content').classes('text-2xl')

    @router.add('/demo')
    def show_demo():
        with ui.column().classes('w-full'):
            ui.label('Demo Content').classes('text-2xl')

    with ui.header().classes(replace='row items-center justify-between') as header:
        ui.icon('auto_stories').classes('q-px-md text-4xl')
        ui.label('Quasar').classes('text-h4 q-mr-n-lg')
        with ui.tabs().classes('ml-auto q-pa-md text-lg') as tabs:
            tab_home = ui.tab('Home').classes('w-32')
            tab_resources = ui.tab('Resources').classes('w-32')
            tab_about = ui.tab('About').classes('w-32')
            tab_demo = ui.tab('Demo').classes('w-32')

    # Define click handlers for tabs
    tab_home.on('click', lambda: router.open('/'))
    tab_resources.on('click', lambda: router.open('/resources'))
    tab_about.on('click', lambda: router.open('/about'))
    tab_demo.on('click', lambda: router.open('/demo'))

    # this places the content which should be displayed
    router.frame().classes('w-full p-4 bg-gray-100')


ui.run()
