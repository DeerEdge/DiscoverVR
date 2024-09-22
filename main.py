import os

from fastapi.staticfiles import StaticFiles
from nicegui import ui, app
from router import Router

current_dir = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=current_dir), name="static")

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
        with ui.carousel(animated=True, arrows=True, navigation=True).props('height=300px'):
            for i in range(0, 60, 3):
                with ui.carousel_slide():
                    with ui.row(wrap=False):
                            ui.html('''
                                                <iframe src="https://deeredge.github.io/aframeSimulations/Fractals.html" width="1468px" height="200px"></iframe>
                                            ''').style('padding: 8px;')

                            ui.image('https://picsum.photos/id/32/270/180').classes('w-96')
                            ui.image('https://picsum.photos/id/32/270/180').classes('w-96')
                            ui.image('https://picsum.photos/id/32/270/180').classes('w-96')
        ui.label('Featured Applications').classes('text-h5 q-px-md q-pt-md text-primary').style(
            'font-weight: bold; color: #90caf9;')  # Subtle blue
        ui.label('Our pick of amazing WebAR experiences for you to explore — no app required!').classes(
            'text-body1 q-px-md').style('margin-bottom: 16px; color: #ffffff;')
        with ui.row().classes('q-gutter-sm q-px-md'):
            # Card 1
            with ui.card().classes('q-pa-sm').style('width: 31.9%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/aframeSimulations/FreeFallObjects.html" width="425px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('Biology Lab (Cell)').classes('text-h6 q-pl-md').style('margin-top: -10px;')
                ui.label(
                    'Explore the intricate world of biology in our VR Lab, where you can dive into a fully immersive 3D'
                    'representation of a cell. Zoom in to see detailed structures like the nucleus, mitochondria, and'
                    'more, as if you are inside the microscopic world of life itself!'
                ).classes('q-pl-md').style('margin-top: -10px;')
                ui.button('Enter Experience', on_click=lambda: router.open('/experience1')).classes('q-pl-lg').style('width: calc(100% - 10px); display: block; margin-top: -5px; margin-left: 5px; margin-bottom: 5px')

            # Card 2
            with ui.card().classes('q-pa-sm').style('width: 31.9%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/aframeSimulations/Particles.html" width="425px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('Particle Lab').classes('text-h6 q-pl-md').style('margin-top: -10px;')
                ui.label(
                    'WebAR brings augmented reality directly to your browser, eliminating the need for apps. It allows '
                    'users to interact with 3D objects and environments in real-time. With WebAR, businesses can create '
                    'immersive experiences accessible to anyone with a smartphone.'
                ).classes('q-pl-md').style('margin-top: -10px;')
                ui.button('Enter Experience', on_click=lambda: router.open('/experience2')).classes('q-pl-lg').style('width: calc(100% - 10px); display: block; margin-top: -5px; margin-left: 5px; margin-bottom: 5px')

            # Card 3
            with ui.card().classes('q-pa-sm').style('width: 31.9%'):
                ui.html('''
                    <iframe src="https://deeredge.github.io/aframeSimulations/3DShapes.html" width="425px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('3D Shapes Lab').classes('text-h6 q-pl-md').style('margin-top: -10px;')
                ui.label(
                    'Explore the world of geometry in our VR Lab, where you can interact with various 3D shapes and '
                    'discover their volume and surface area formulas. Watch as the shapes come to life, and gain a '
                    'deeper understanding of how these mathematical concepts apply in three dimensions!'
                ).classes('q-pl-md').style('margin-top: -10px;')
                ui.button('Enter Experience', on_click=lambda: router.open('/experience3')).classes('q-pl-lg').style('width: calc(100% - 10px); display: block; margin-top: -5px; margin-left: 5px; margin-bottom: 5px')

    # Full-screen experience pages
    @router.add('/experience1')
    def show_experience1():
        with ui.column().classes('w-full q-pa-md'):
            ui.button('Back', on_click=lambda: router.open('/')).classes('q-mb-md')
            ui.html('''
                <iframe src="https://deeredge.github.io/aframeSimulations/FreeFallObjects.html" width= "1420px" height="700px"></iframe>
            ''')

    @router.add('/experience2')
    def show_experience2():
        with ui.column().classes('w-full q-pa-md'):
            ui.button('Back', on_click=lambda: router.open('/')).classes('q-mb-md')
            ui.html('''
                <iframe src="https://deeredge.github.io/aframeSimulations/Particles.html" width= "1420px" height="700px"></iframe>
            ''')

    @router.add('/experience3')
    def show_experience3():
        with ui.column().classes('w-full q-pa-md'):
            ui.button('Back', on_click=lambda: router.open('/')).classes('q-mb-md')
            ui.html('''
                <iframe src="https://deeredge.github.io/aframeSimulations/3DShapes.html" width= "1420px" height="700px"></iframe>
            ''')

    @router.add('/resources')
    def show_resources():
        with ui.column().classes('w-full q-pa-md'):
            ui.label('Explore/Learn').classes('text-h4 q-mb-md text-primary')
            ui.separator().style(f"background-color: #90D5FF")
            with ui.row():
                ui.button('Art', on_click=lambda: router.open('/art'))
                ui.button('Math', on_click=lambda: router.open('/math'))
                ui.button('Biology', on_click=lambda: router.open('/biology'))
                ui.button('Astronomy', on_click=lambda: router.open('/astronomy'))
            ui.separator().style(f"background-color: #90D5FF")

    @router.add('/art')
    def show_art():
        with ui.column().classes('w-full q-pa-md'):
            ui.label('Explore Art Topics').classes('text-h4 q-mb-md text-primary')



    @router.add('/about')
    def show_about():
        with ui.column().classes('w-full q-pa-md'):
            ui.label('About Us').classes('text-h4 q-mb-md text-primary')
            ui.label('Learn more about our company and mission.').classes('text-body1')

    @router.add('/sandbox')
    def show_sandbox():
        ui.label('SandBox').classes('text-h4 q-mb-md text-primary')
        ui.label('Play around with prompts!').classes('text-body1')
        ui.html('''
            <iframe src="/static/index.html" width="1420px" height="700px"></iframe>
        ''')

    with ui.header().classes(replace='row items-center justify-between q-py-md bg-dark').style(
            'border-bottom: 1px solid #333;'):
        with ui.row().classes('items-center'):
            ui.icon('auto_stories').classes('q-px-md text-4xl text-primary')
            ui.label('Quasar').classes('text-h4 text-weight-bold')
        with ui.tabs().classes('q-px-md').style('border-bottom: none;') as tabs:
            tab_home = ui.tab('Home').classes('text-h6')
            tab_resources = ui.tab('Resources').classes('text-h6')
            tab_about = ui.tab('About').classes('text-h6')
            tab_sandbox = ui.tab('sandbox').classes('text-h6')

    # Define click handlers for tabs
    tab_home.on('click', lambda: router.open('/'))
    tab_resources.on('click', lambda: router.open('/resources'))
    tab_about.on('click', lambda: router.open('/about'))
    tab_sandbox.on('click', lambda: router.open('/sandbox'))

    # this places the content which should be displayed
    router.frame().classes('w-full p-4')


ui.run()
