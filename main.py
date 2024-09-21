from nicegui import ui
from router import Router

ui.add_head_html('''
    <link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />
    <style>
        body { background-color: #121212; color: #ffffff; }
        .q-card { background-color: #1e1e1e; }
        .q-tab { color: #ffffff; }
        .q-tab--active { color: #1976d2; }
        .text-h6 { color: #1976d2; }
        .custom-card { transition: transform 0.3s, box-shadow 0.3s; }
        .custom-card:hover { transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
    </style>
''')

@ui.page('/')
@ui.page('/{_:path}')
def main():
    ui.query('body').classes('bg-dark')

    router = Router()

    @router.add('/')
    def show_home():
        ui.label('Featured Applications').classes('text-h5 q-px-md q-pt-md text-primary').style('font-weight: bold; color: #90caf9;')  # Subtle blue
        ui.label('Our pick of amazing WebAR experiences for you to explore — no app required!').classes(
            'text-body1 q-px-md').style('margin-bottom: 16px; color: #ffffff;')
        with ui.row().classes('q-gutter-sm q-px-md'):
            # Card 1
            with ui.card().classes('q-pa-sm').style('width: 31.9%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/frame1/" width="425px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('Experience WebAR').classes('text-h6 q-pl-md').style('margin-top: -10px;')
                ui.label(
                    'WebAR brings augmented reality directly to your browser, eliminating the need for apps. It allows '
                    'users to interact with 3D objects and environments in real-time. With WebAR, businesses can create '
                    'immersive experiences accessible to anyone with a smartphone.'
                ).classes('q-pl-md').style('margin-top: -10px;')
                ui.button('Enter Experience', on_click=lambda: router.open('/experience1')).classes('q-pl-lg').style('width: calc(100% - 10px); display: block; margin-top: -5px; margin-left: 5px; margin-bottom: 5px')

            # Card 2
            with ui.card().classes('q-pa-sm').style('width: 31.9%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/frame1/" width="425px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('Experience WebAR').classes('text-h6 q-pl-md').style('margin-top: -10px;')
                ui.label(
                    'WebAR brings augmented reality directly to your browser, eliminating the need for apps. It allows '
                    'users to interact with 3D objects and environments in real-time. With WebAR, businesses can create '
                    'immersive experiences accessible to anyone with a smartphone.'
                ).classes('q-pl-md').style('margin-top: -10px;')
                ui.button('Enter Experience', on_click=lambda: router.open('/experience2')).classes('q-pl-lg').style('width: calc(100% - 10px); display: block; margin-top: -5px; margin-left: 5px; margin-bottom: 5px')

            # Card 3
            with ui.card().classes('q-pa-sm').style('width: 31.9%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/frame1/" width="425px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('Experience WebAR').classes('text-h6 q-pl-md').style('margin-top: -10px;')
                ui.label(
                    'WebAR brings augmented reality directly to your browser, eliminating the need for apps. It allows '
                    'users to interact with 3D objects and environments in real-time. With WebAR, businesses can create '
                    'immersive experiences accessible to anyone with a smartphone.'
                ).classes('q-pl-md').style('margin-top: -10px;')
                ui.button('Enter Experience', on_click=lambda: router.open('/experience3')).classes('q-pl-lg').style('width: calc(100% - 10px); display: block; margin-top: -5px; margin-left: 5px; margin-bottom: 5px')

    # Full-screen experience pages
    @router.add('/experience1')
    def show_experience1():
        with ui.column().classes('w-full q-pa-md'):
            ui.button('Back', on_click=lambda: router.open('/')).classes('q-mb-md')
            ui.html('''
                <iframe src="https://deeredge.github.io/frame1/" width="100%" height="80%"></iframe>
            ''')

    @router.add('/experience2')
    def show_experience2():
        with ui.column().classes('w-full q-pa-md'):
            ui.button('Back', on_click=lambda: router.open('/')).classes('q-mb-md')
            ui.html('''
                <iframe src="https://deeredge.github.io/frame1/" width="100%" height="80%"></iframe>
            ''')

    @router.add('/experience3')
    def show_experience3():
        with ui.column().classes('w-full q-pa-md'):
            ui.button('Back', on_click=lambda: router.open('/')).classes('q-mb-md')
            ui.html('''
                <iframe src="https://deeredge.github.io/frame1/" width="100%" height="80%"></iframe>
            ''')

    @router.add('/resources')
    def show_resources():
        with ui.column().classes('w-full q-pa-md'):
            ui.label('Resources').classes('text-h4 q-mb-md text-primary')
            ui.label('Here you can find various resources and materials.').classes('text-body1')

    @router.add('/about')
    def show_about():
        with ui.column().classes('w-full q-pa-md'):
            ui.label('About Us').classes('text-h4 q-mb-md text-primary')
            ui.label('Learn more about our company and mission.').classes('text-body1')

    @router.add('/demo')
    def show_demo():
        with ui.column().classes('w-full q-pa-md'):
            ui.label('Demo').classes('text-h4 q-mb-md text-primary')
            ui.label('Explore our product demos and features.').classes('text-body1')

    with ui.header().classes(replace='row items-center justify-between q-py-md bg-dark').style(
            'border-bottom: 1px solid #333;'):
        with ui.row().classes('items-center'):
            ui.icon('auto_stories').classes('q-px-md text-4xl text-primary')
            ui.label('Quasar').classes('text-h4 text-weight-bold')
        with ui.tabs().classes('q-px-md').style('border-bottom: none;') as tabs:
            tab_home = ui.tab('Home').classes('text-h6')
            tab_resources = ui.tab('Resources').classes('text-h6')
            tab_about = ui.tab('About').classes('text-h6')
            tab_demo = ui.tab('Demo').classes('text-h6')

    # Define click handlers for tabs
    tab_home.on('click', lambda: router.open('/'))
    tab_resources.on('click', lambda: router.open('/resources'))
    tab_about.on('click', lambda: router.open('/about'))
    tab_demo.on('click', lambda: router.open('/demo'))

    # this places the content which should be displayed
    router.frame().classes('w-full p-4')


ui.run()
