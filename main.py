import os
import re
import time
import aiohttp
from fastapi.staticfiles import StaticFiles
from nicegui import ui, app
from router import Router
from openai import OpenAI
import shutil

# API setup
client = OpenAI(
    api_key="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",
    base_url="https://api.perplexity.ai"
)

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
                    <iframe src="https://deeredge.github.io/aframeSimulations/solarSystem.html" width="425px" height="200px"></iframe>
                ''').style('padding: 8px;')
                ui.label('Solar System Lab').classes('text-h6 q-pl-md').style('margin-top: -10px;')
                ui.label(
                    'Embark on an awe-inspiring journey through our Solar System in this immersive VR experience!'
                    'Explore the stunning beauty of planets, moons, and asteroids, while learning about their unique '
                    'characteristics and the dynamics of our cosmic neighborhood. Discover the wonders of space like'
                    'never before!"'
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
                <iframe src="https://deeredge.github.io/aframeSimulations/solarSystem.html" width= "1420px" height="700px"></iframe>
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
            ui.label('Explore & Learn').classes('text-h4 q-mb-md text-primary').tailwind.font_weight('extrabold')
            ui.separator().style(f"background-color: #90D5FF")
            with ui.row():
                ui.button('Art', on_click=lambda: art_info()).style('width: 481px')
                ui.button('Math', on_click=lambda: math_info()).style('width: 481px')
                ui.button('Biology', on_click=lambda: bio_info()).style('width: 481px')


    def art_info():
        ui.add_head_html('''
            <style type="text/tailwindcss">
                h2 {font-size: 200%;}
            </style>
        ''')
        ui.add_head_html('''
            <style type="text/tailwindcss">
                h3 {font-size: 175%;}
            </style>
        ''')
        with ui.card().style('width: 692px'):
            ui.html('<h3>Modern Art:</h3>')
            ui.label(
                'Modern Art is a movement that emerged in the late 19th century, characterized by a break from'
                'traditional techniques and a focus on innovation and experimentation. It spans a wide range of'
                'styles, including Impressionism, Cubism, Surrealism, and Abstract Expressionism, with artists like'
                'Claude Monet, Pablo Picasso, and Jackson Pollock pushing boundaries. Modern art emphasizes'
                'abstraction, non-representational forms, and the exploration of new ideas, reflecting the rapidly'
                'changing social, technological, and cultural landscapes of the time. This movement laid the'
                'foundation for contemporary art, continuing to influence artistic expression today.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                        <iframe src="https://deeredge.github.io/aframeSimulations/modernArt.html" width="738px" height="200px"></iframe>
                    ''').style('padding: 8px;')
            ui.label('Modern Art Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes('text-h6 q-pl-md').style('margin-top: -10px;')

        with ui.card().style('width: 692px'):
            ui.html('<h3>Classical Art:</h3>')
            ui.label(
                'Classical Art refers to the artistic traditions of ancient Greece and Rome, emphasizing harmony,'
                'proportion, and idealized beauty. Flourishing between the 5th century BCE and the fall of the'
                'Roman Empire, it set the foundation for Western art through its focus on naturalistic'
                'representation, balanced compositions, and mastery of the human form. Classical artists strove'
                'for perfection, creating sculptures, paintings, and architecture that celebrated the human body'
                'and intellect. This periods emphasis on order and symmetry heavily influenced the Renaissance'
                'and Neoclassical movements, making it a lasting cornerstone of Western artistic heritage.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                        <iframe src="https://deeredge.github.io/aframeSimulations/classicalArt.html" width="738px" height="200px"></iframe>
                    ''').style('padding: 8px;')
            ui.label('Classical Art Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes('text-h6 q-pl-md').style('margin-top: -10px;')

        with ui.card().style('width: 692px'):
            ui.html('<h3>Pop Art:</h3>')
            ui.label(
                'Pop Art is an artistic movement that emerged in the 1950s and 1960s, primarily in the UK and the'
                'U.S., characterized by its use of imagery from popular culture, mass media, and consumer goods.'
                'It challenged traditional fine art by incorporating everyday objects and symbols, often drawing'
                'from advertising, comic books, and celebrity culture. Artists like Andy Warhol and Roy Lichtenstein'
                'used bright colors, bold outlines, and repetition to blur the boundaries between "high" art and'
                'commercial art. Pop Art sought to reflect and critique modern consumerism, making art'
                'accessible while commenting on societys obsession with mass production and materialism.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                        <iframe src="https://deeredge.github.io/aframeSimulations/popArt.html" width="738px" height="200px"></iframe>
                    ''').style('padding: 8px;')
            ui.label('Pop Art Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes('text-h6 q-pl-md').style('margin-top: -10px;')



    def math_info():
        ui.add_head_html('''
                    <style type="text/tailwindcss">
                        h2 {font-size: 200%;}
                    </style>
                ''')
        ui.add_head_html('''
                    <style type="text/tailwindcss">
                        h3 {font-size: 175%;}
                    </style>
                ''')
        with ui.card().style('width: 692px'):
            ui.html('<h3>Properties of 2D Shapes:</h3>')
            ui.label(
                '2D shapes are flat, having only length and width, and are defined by their sides, angles, and'
                'vertices. Key properties include the number of sides, the measure of internal angles, perimeter'
                '(the total length of all sides), and area (the space enclosed by the shape). Common classifications'
                'of 2D shapes include polygons, which have straight sides, and non-polygons, like circles.'
                'Symmetry, tessellation, and congruence are also important properties, determining how shapes'
                'relate to each other and fit together in space. These properties help define the geometry of each'
                'shape.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                                <iframe src="https://deeredge.github.io/aframeSimulations/properties2DShapes.html" width="738px" height="200px"></iframe>
                            ''').style('padding: 8px;')
            ui.label('2D Shapes Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes(
                'text-h6 q-pl-md').style('margin-top: -10px;')

        with ui.card().style('width: 692px'):
            ui.html('<h3>Properties of 3D Shapes:</h3>')
            ui.label(
                '3D shapes, also known as solid shapes, have three dimensions: length, width, and height (or'
                'depth). Their key properties include faces (flat or curved surfaces), edges (where two faces'
                'meet), and vertices (corners where edges meet). Volume measures the space inside the shape,'
                'while surface area is the total area of all the faces. 3D shapes can be classified into various types,'
                'such as polyhedra (with flat faces) and curved solids like spheres and cylinders. Understanding'
                'these properties is essential in studying how objects occupy space and relate to their'
                'surroundings.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                                <iframe src="https://deeredge.github.io/aframeSimulations/3DShapes.html" width="738px" height="200px"></iframe>
                            ''').style('padding: 8px;')
            ui.label('3D Shapes Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes(
                'text-h6 q-pl-md').style('margin-top: -10px;')

        with ui.card().style('width: 692px'):
            ui.html('<h3>Right Triangle Properties:</h3>')
            ui.label(
                'A 30-60-90 triangle is a right triangle with angles of 30°, 60°, and 90°, characterized by a side'
                'ratio of 1:√3:2, where the shortest side is opposite the 30° angle. In contrast, a 45-45-90 triangle'
                'has two 45° angles and one 90° angle, with sides in a 1:1:√2 ratio, where the legs are equal in'
                'length and the hypotenuse is √2 times the length of each leg. These triangles are essential in'
                'geometry for their predictable side relationships.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                                <iframe src="https://deeredge.github.io/aframeSimulations/rightTriangleProperties.html" width="738px" height="200px"></iframe>
                            ''').style('padding: 8px;')
            ui.label('Right Triangle Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes(
                'text-h6 q-pl-md').style('margin-top: -10px;')

        with ui.card().style('width: 692px'):
            ui.html('<h3>Unit Circle Properties:</h3>')
            ui.label(
                'The unit circle is a circle with a radius of one, centered at the origin of a coordinate plane. It'
                'serves as a fundamental tool in trigonometry, where the coordinates of any point on the circle'
                'correspond to the cosine and sine of the angle formed with the positive x-axis. The unit circle'
                'allows for easy visualization of the relationships between angles and their sine and cosine values,'
                'helping to define trigonometric functions for all real numbers. It also plays a crucial role in'
                'understanding periodicity, symmetry, and the behavior of trigonometric graphs.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                                <iframe src="https://deeredge.github.io/aframeSimulations/unitCircleProperties.html" width="738px" height="200px"></iframe>
                            ''').style('padding: 8px;')
            ui.label('Unit Circle Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes(
                'text-h6 q-pl-md').style('margin-top: -10px;')
    def bio_info():
        ui.add_head_html('''
                            <style type="text/tailwindcss">
                                h2 {font-size: 200%;}
                            </style>
                        ''')
        ui.add_head_html('''
                            <style type="text/tailwindcss">
                                h3 {font-size: 175%;}
                            </style>
                        ''')
        with ui.card().style('width: 692px'):
            ui.html('<h3>Plant Cell:</h3>')
            ui.label(
                'A plant cell is characterized by its rigid cell wall, which provides structure and support, as well as a'
                'large central vacuole that stores water, nutrients, and waste products. Plant cells contain'
                'chloroplasts, the organelles responsible for photosynthesis, allowing them to convert sunlight into'
                'energy. Additionally, they have a nucleus, which houses genetic material, and various organelles'
                'such as mitochondria, endoplasmic reticulum, and Golgi apparatus, essential for cellular functions.'
                'The presence of plastids and a unique arrangement of cytoplasm contribute to the overall'
                'functionality and efficiency of plant cells.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                                        <iframe src="https://deeredge.github.io/aframeSimulations/plantCell.html" width="738px" height="200px"></iframe>
                                    ''').style('padding: 8px;')
            ui.label('Plant Cell Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes(
                'text-h6 q-pl-md').style('margin-top: -10px;')


        with ui.card().style('width: 692px'):
            ui.html('<h3>DNA Strand:</h3>')
            ui.label(
                'DNA (deoxyribonucleic acid) is a double-stranded helical molecule that carries the genetic'
                'instructions essential for the growth, development, and functioning of all living organisms.'
                'Composed of nucleotide units, each containing a sugar, phosphate group, and a nitrogenous base'
                '(adenine, thymine, cytosine, or guanine), DNA sequences encode genes that determine traits. The'
                'specific pairing of bases—adenine with thymine and cytosine with guanine—facilitates accurate'
                'replication during cell division. DNA is organized into structures called chromosomes within the'
                'cell nucleus, playing a crucial role in heredity and the transmission of genetic information.'
            )
        with ui.card().style('width: 784px'):
            ui.html('''
                                                <iframe src="https://deeredge.github.io/aframeSimulations/DNAStrand.html" width="738px" height="200px"></iframe>
                                            ''').style('padding: 8px;')
            ui.label('DNA Strand Visual (Move around with WASD or Arrow Keys. Drag to look around)').classes(
                'text-h6 q-pl-md').style('margin-top: -10px;')


    @router.add('/sandbox')
    def show_sandbox():
        ui.label('SandBox').classes('text-h4 q-mb-md text-primary')
        iframe = ui.html('''
                <iframe id="aframe-scene" src="static/index.html" width="1420px" height="700px"></iframe>
            ''')

        # Add chat input and buttons in a card
        with ui.card().classes('w-3/4 mx-auto q-pa-md q-mt-md').style('background-color: #dae0e3;'):
            with ui.row().classes('w-full items-center relative'):
                prompt_input = ui.input(placeholder='Enter your idea here!                                    '
                                                    '                                    Use the arrow button to start your creation, reload your model to render it!    ------>    ').props('outlined').classes(
                    'w-full pr-24')
                with ui.button(icon='arrow_forward', on_click=lambda: process_prompt(prompt_input.value, iframe)).props(
                        'round color=primary').classes('absolute right-12 top-1/2 -translate-y-1/2'):
                    ui.tooltip('Generate')
                with ui.button(icon='refresh', on_click=lambda: reload_iframe(iframe)).props(
                        'round color=secondary').classes('absolute right-0 top-1/2 -translate-y-1/2'):
                    ui.tooltip('Reload View')

        ui.add_head_html('''
            <style>
                .q-field__native {
                    color: black !important;
                }
                .q-field--outlined .q-field__control {
                    background: #edf3f5 !important; /* Creme color */
                    border-color: #D2B48C !important; /* Slightly darker border */
                }
                .q-field--outlined .q-field__control:hover {
                    border-color: #A0522D !important; /* Darker on hover */
                }
            </style>
            ''')

    async def process_prompt(prompt: str, iframe):
        print(f"Processing prompt: {prompt}")
        new_html = await generate_aframe_scene(prompt)

        static_file_path = os.path.abspath(os.path.join('static', 'index.html'))
        root_file_path = os.path.abspath('index.html')

        try:
            # Write the new HTML to static/index.html
            with open(static_file_path, 'w') as f:
                f.write(new_html)
            print(f"Successfully wrote new HTML to {static_file_path}")

            # Copy static/index.html to index.html in the root directory
            shutil.copy2(static_file_path, root_file_path)
            print(f"Copied {static_file_path} to {root_file_path}")

            ui.notify('Scene generated. Click "Reload View" to see changes.')
        except Exception as e:
            print(f"Error writing to file: {e}")
            ui.notify('Error generating scene', color='negative')

    def reload_iframe(iframe):
        timestamp = int(time.time() * 3000)
        ui.run_javascript(f'''
            var iframe = document.getElementById('aframe-scene');
            iframe.src = "/static/index.html?t={timestamp}";
        ''')
        ui.notify('View reloaded')

    async def generate_aframe_scene(prompt: str) -> str:
        try:
            messages = [
                {"role": "system",
                 "content": "You are an AI assistant that generates simple and error-free A-Frame scenes based on user "
                            "prompts. Respond only with the complete HTML code for the A-Frame scene, including necessary "
                            "scripts, HTML, and physics mechanics if needed."},
                {"role": "user", "content": f"Generate a clean A-Frame scene with white background with this prompt:: {prompt}"}
            ]

            print("Sending request to Perplexity API")
            response = client.chat.completions.create(
                model="llama-3.1-sonar-large-128k-online",
                messages=messages,
            )
            print("Received response from Perplexity API")

            # Get the generated HTML
            generated_html = response.choices[0].message.content
            pattern = r'(<!DOCTYPE.*?>.*</html>)'
            match = re.search(pattern, generated_html, re.DOTALL | re.IGNORECASE)

            if match:
                clean_html = match.group(1)
            else:
                clean_html = generated_html

            return clean_html

        except Exception as e:
            print(f"Error generating A-Frame scene: {e}")
            return "<html><body><a-scene><a-box position='0 1 -3' rotation='0 45 0' color='#4CC3D9'></a-box></a-scene></body></html>"

    with ui.header().classes(replace='row items-center justify-between q-py-md bg-dark').style(
            'border-bottom: 1px solid #333;'):
        with ui.row().classes('items-center'):
            ui.icon('auto_stories').classes('q-px-md text-4xl text-primary')
            ui.label('Quasar').classes('text-h4 text-weight-bold')
        with ui.tabs().classes('q-px-md').style('border-bottom: none;') as tabs:
            tab_home = ui.tab('Home').classes('text-h6')
            tab_explorelearn = ui.tab('Explore & Learn').classes('text-h6')

            tab_sandbox = ui.tab('sandbox').classes('text-h6')

    # Define click handlers for tabs
    tab_home.on('click', lambda: router.open('/'))

    tab_explorelearn.on('click', lambda: router.open('/resources'))

    tab_sandbox.on('click', lambda: router.open('/sandbox'))

    # this places the content which should be displayed
    router.frame().classes('w-full p-4')


ui.run()
