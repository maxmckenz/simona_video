from manim import *
import numpy as np

class HumanAlgorithm3(Scene):

    # Scene to provide visualisations for a video about humans as an algorithm (the black box method)

    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"The Black Box Method",
            tex_template=myTemplate,
            font_size=100,
        )

        self.wait(1.3)
        self.play(Write(tex), run_time=4)

        # Shift and shrink the text to the top of the screen
        self.play(tex.animate.to_edge(UP), run_time=1)

        self.wait(2.5)

        # Animate a box in the middle of the screen with the text '?' inside
        box = Rectangle(width=2, height=3, fill_opacity=0.5, fill_color=WHITE)
        text_inside_box = Tex("?")
        box_with_text = VGroup(box, text_inside_box)
        box_with_text.move_to(ORIGIN)
        self.play(Create(box_with_text),run_time=4)

        # Wait a second
        self.wait(0)

        # Animate multiple arrows (inputs) coming from the left that feed into the box

        arrow1 = Arrow(LEFT-np.array([3,0,0])+np.array([0,1,0]), box_with_text.get_left()+np.array([0,1,0]), buff=2)
        arrow2 = Arrow(LEFT-np.array([3,0,0]), box_with_text.get_left(), buff=2)
        arrow3 = Arrow(LEFT-np.array([3,0,0])-np.array([0,1,0]), box_with_text.get_left()-np.array([0,1,0]), buff=2)

        self.play(Create(arrow1))
        self.wait(0.5)
        self.play(Create(arrow2))
        self.wait(0.5)
        self.play(Create(arrow3))

        self.wait(5)
