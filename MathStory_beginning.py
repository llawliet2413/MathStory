from manim import *
import numpy as np
import random

class Beginning(Scene):
    def construct(self):
        Indicate.set_default(color=None)

        # ==============================================================
        #  SUBTITLE HELPERS (your \parbox{11cm} style)
        # ==============================================================
        def cue(sa, width_cm=11, scale=0.8, rt=0.5):
            """Show a new subtitle at the bottom."""
            body = rf"\parbox{{{width_cm}cm}}{{\centering {sa}}}"
            sub = Tex(body).scale(scale).to_edge(DOWN)
            self.play(FadeIn(sub), run_time=rt)
            return sub

        def recue(prev_sub, sa, width_cm=11, scale=0.8, rt=0.5):
            """Replace the existing subtitle smoothly."""
            if prev_sub not in self.mobjects:
                # if it was cleared, recreate instead of transforming
                return cue(sa, width_cm=width_cm, scale=scale, rt=rt)
            body = rf"\parbox{{{width_cm}cm}}{{\centering {sa}}}"
            new_sub = Tex(body).scale(scale).to_edge(DOWN)
            new_sub.move_to(prev_sub)
            self.play(Transform(prev_sub, new_sub), run_time=rt)
            return prev_sub

        def hide_cue(sub, rt=0.3):
            """Fade out the current subtitle."""
            if sub in self.mobjects:
                self.play(FadeOut(sub), run_time=rt)

        # helper: filter objects that are still alive on the scene
        def alive(*objs):
            return [o for o in objs if o in self.mobjects]

        # ==============================================================
        #  INTRO: Theorems floating around
        # ==============================================================
        Title = MathTex(r"""
                        \begin{aligned}
                        \text{The }&\text{birth of mathematical Thinking- }\\
                        &\text{and the beginning of \textit{\textbf{Proof}}} 
                        \end{aligned}
                        """)
        
        
        self.play(Write(Title), scale= 1.5, run_time=1)
        self.wait(1)
        self.play(FadeOut(Title), run_time=1)
        
        text1 = Tex(r"Isosceles triangle's angles are equal", font_size=34, color=WHITE).shift(UP * 3.5 + LEFT * 3).scale(.45)
        text2 = Tex(r"Vertical angles are congruent", font_size=34, color=WHITE).shift(UP * 2 + RIGHT * 2).scale(0.5)
        text3 = Tex(r"There exists a right angle inside a semicircle", font_size=34, color=WHITE).shift(LEFT * 2 + UP * 1).scale(0.6)
        text4 = Tex(r"ASA triangle congruence", font_size=34, color=WHITE).shift(DOWN * .5 + LEFT * 5).scale(0.6)
        text5 = Tex(r"\textit{Pythagorean theorem}", font_size=34, color=WHITE).shift(DOWN * 2 + RIGHT * 5)

        textA = Tex(r"\textit{Dirac Delta Function}", font_size=34, color=WHITE).shift(UP * 3.5 + LEFT * 3)
        textB = Tex(r"\textit{Riesz–Fischer Theorem}", font_size=34, color=WHITE).shift(UP * 2 + RIGHT * 2)
        textC = Tex(r"\textit{Minkowski's inequality}", font_size=34, color=WHITE).shift(LEFT * 2 + UP * 1).scale(1.2)
        textD = Tex(r"\textit{Young's inequality}", font_size=34, color=WHITE).shift(DOWN * .5 + LEFT * 5)
        textE = Tex(r"\textit{Fermat's Last Theorem}", font_size=34, color=WHITE).shift(DOWN * 2 + RIGHT * 5).scale(0.8)

        thinking_emoji = SVGMobject("man-thinking-svgrepo-com.svg").shift(DOWN).scale(1.5)

        # 1) Early theorems
        self.play(Write(text1), Write(text2), Write(text3), Write(text4), Write(text5))
        sub = cue(r"We learn plenty of theorems and definitions, but how often do we stop and ask—``\textit{why do we prove?}''")
        self.wait(2)

        # 2) Transform to modern theorems
        self.play(
            Transform(text1, textA),
            Transform(text2, textB),
            Transform(text3, textC),
            Transform(text4, textD),
            Transform(text5, textE),
            run_time=1
        )
        sub = recue(sub, r"In daily life, we usually trust what we can see or measure.")
        self.wait(1)

        # 3) Thinking emoji
        self.play(FadeIn(thinking_emoji))
        sub = recue(sub, r"But for mathematics, \boxed{\textit{seeing}} isn’t enough.")
        self.play(Succession(
            Rotate(thinking_emoji, -5 * DEGREES),
            Rotate(thinking_emoji,  5 * DEGREES),
            Rotate(thinking_emoji, -5 * DEGREES),
            Rotate(thinking_emoji,  5 * DEGREES),
            Rotate(thinking_emoji, -5 * DEGREES)
        ), run_time=.5)
        self.wait(1)

        # ==============================================================
        #  QUESTION: Why do we prove?
        # ==============================================================
        self.clear()
        main_question = Tex(r"Why Do We Prove?")
        self.play(Create(main_question))
        # after clear(), recreate subtitle instead of recue
        sub = cue(r"Proof is something deeper—knowing something \emph{must} be true, not just that it looks true.")
        self.wait(1.5)

        # ==============================================================
        #  TRIANGLE SETUP
        # ==============================================================
        C = LEFT + DOWN * .5
        A = RIGHT + DOWN * .5
        B = UP + LEFT
        triangle = Polygon(A, B, C, color=WHITE)

        self.play(ReplacementTransform(main_question, triangle), run_time=1.5)
        sub = recue(sub, r"Let’s see it in a right triangle.")

        label_A = MathTex("C").next_to(C, DOWN + LEFT * 3, buff=0.1)
        label_B = MathTex("A").next_to(A, DOWN + RIGHT, buff=0.1)
        label_C = MathTex("B").next_to(B, LEFT + UP, buff=0.1)
        base_label = MathTex("b").next_to((A + C) / 2, DOWN)
        height_label = MathTex("a").next_to((B + C) / 2, LEFT)
        hyp_label = MathTex("c").next_to((B + A) / 2, UP)

        self.play(Write(label_A.scale(.7)), Write(label_B.scale(.7)), Write(label_C.scale(.7)), run_time=.5)
        self.play(Write(base_label), Write(height_label), Write(hyp_label), run_time=.5)
        self.wait(.3)
        self.play(FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), run_time=0.5)

        # ==============================================================
        #  SQUARES on the sides
        # ==============================================================
        square_a = Square(side_length=2, color=BLUE, fill_color=BLUE, fill_opacity=0.3).next_to(Line(C, A), DOWN, buff=0)
        square_b = Square(side_length=1.5, color=RED, fill_color=RED, fill_opacity=0.3).next_to(Line(C, B), LEFT, buff=0)
        hyp_len = np.linalg.norm(A - B)
        angle = Line(A, B).get_angle()
        mid = (A + B) / 2
        v = (B - A) / hyp_len
        perp = rotate_vector(v, PI / 2)
        sign = 1 if np.dot(perp, C - mid) < 0 else -1
        center = mid + sign * perp * (hyp_len / 2)
        square_c = Square(side_length=hyp_len, color=PURPLE, fill_color=PURPLE, fill_opacity=0.3).rotate(angle).move_to(center)

        self.play(FadeOut(base_label), FadeOut(height_label), FadeOut(hyp_label), run_time=0.3)
        a_label = MathTex("b^2").next_to(Line(C, A).get_midpoint(), DOWN * .8)
        b_label = MathTex("a^2").next_to(Line(C, B).get_midpoint(), LEFT * .8)
        c_label = MathTex("c^2").next_to(Line(A, B).get_midpoint(), UP + RIGHT)

        self.play(FadeIn(square_a), FadeIn(square_b), FadeIn(square_c), run_time=1)
        sub = recue(sub, r"Areas: \boxed{\text{by our sense}}, the sum of two small squares (\(a^2\) and \(b^2\)) \(\approx\) the large one (\(c^2\)).")
        self.play(Write(a_label), Write(b_label), Write(c_label), run_time=0.6)

        # visual merge cue
        pair = VGroup(square_a.copy(), square_b.copy())
        self.play(Transform(pair, square_c.copy().set_opacity(0.35)), run_time=1.2)
        self.play(Indicate(square_c), run_time=0.6)

        # ==============================================================
        #  EQUATION at the bottom
        # ==============================================================
        hide_cue(sub)
        eq = MathTex(r"\text{So we have found out a claim: }", "a^2", "+", "b^2", r"\approx", "c^2").scale(1.2).to_edge(DOWN)
        self.play(Write(eq), run_time=0.8)
        self.wait(1)

        # ==============================================================
        #  RETURN to question
        # ==============================================================
        self.play(FadeOut(eq), run_time=0.5)
        sub = cue(r"But how can we \textit{\textbf{rationally establish}} this claim, rather than relying solely on \textit{sensory} judgment?")
        self.play(Indicate(sub))
        self.wait(2)
        sub = recue(sub, r"It started with a revolution—\textit{a Greek revolution of reasoning.}")

        # ==============================================================
        #  CULTURAL TRANSITION (Egypt → Babylon → Greece)
        #  Pattern: Fade OUT geometry → Fade IN 'Egyptian' → Transform text
        # ==============================================================
        Egyptian = Tex(r"Ancient Egyptians used practical methods to solve problems.")
        Babylonian = Tex(
            r"Babylonians relied on \textit{empirical observations} and approximations.",
            substrings_to_isolate=["empirical observations"]
        ).scale(0.9)
        Babylonian.set_color_by_tex("empirical observations", RED)
        Greek = Tex(
            r"Greeks developed \textit{deductive reasoning} and formal proofs.",
            substrings_to_isolate=["deductive reasoning"]
        ).scale(0.95)
        Greek.set_color_by_tex("deductive reasoning", RED)

        # collect any geometry still alive
        geom_group = VGroup(*alive(
            triangle, square_a, square_b, square_c,
            a_label, b_label, c_label, pair
        ))
        if len(geom_group) > 0:
            self.play(FadeOut(geom_group, lag_ratio=0.05), run_time=0.8)

        # Fade in first text, then transform chain
        self.play(FadeIn(Egyptian), run_time=0.6)
        sub = recue(sub, r"Egypt: practical rules and procedures that work in practice.")
        self.wait(0.6)

        self.play(Transform(Egyptian, Babylonian), run_time=1.2, rate_func=smooth)
        sub = recue(sub, r"Babylonia: computation guided by observation and approximation.")
        self.wait(0.6)

        self.play(Transform(Egyptian, Greek), run_time=1.2, rate_func=smooth)
        sub = recue(sub, r"Greece: \textit{deductive reasoning} and formal proof become the ideal.")
        self.wait(0.6)

        self.play(FadeOut(Egyptian), run_time=0.6)
        hide_cue(sub)
        self.wait(0.6)

