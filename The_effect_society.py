from manim import *
from textwrap import fill

class ModernImpactOutro(Scene):
    def construct(self):
        # ================== Scene setup ==================
        part_4 = MathTex(
            r"\textit{\textbf{How}}",
            font_size = 72
        )
        part_5 = MathTex(
            r"\textit{\textbf{Modern Impact}}",
            font_size = 72,
            color=RED
        )
        
        self.play(Write(part_4),
                 run_time=1.0
        )
        self.wait(.5)
        self.play(
            ReplacementTransform(part_4, part_5),
            run_time=1
        )
        self.wait(1.0)
        self.play(
            FadeOut(part_5),
            run_time=1
        )
        self.wait(0.5)
        # ================== Central keyword: RIGOUR ==================
        title = MathTex(
            r"\textit{\textbf{Proof}}",
            font_size=72,
            color=YELLOW
        ).to_edge(UP, buff=.8)
        
        subtitle_title = MathTex(
            r"\text{For the Greeks, proof wasn't just a technique. It was a completely new way of knowing.}",
            font_size=30,
        )
        subtitle_title.to_edge(DOWN, buff=.5)

        self.play(
            FadeIn(title, shift=DOWN*0.3),
            FadeIn(subtitle_title),
            run_time=1.5)
        self.wait(2.0)  # 你可以喺呢度開始講「Greeks invented proof...」
        
        # ================== A few MathTex key phrases in the centre ==================
        stmt1 = MathTex(
            r"\text{Proof} \Rightarrow \text{reliable knowledge}",
            font_size=40
        ).next_to(title, DOWN, buff=.5)

        subtitle_stmt1 = MathTex(
            r"""
            \begin{aligned}
            \text{A \textit{proof} turn an obsevation into } &\text{reliable knowledge-something that stays true,}\\
            \text{no matter \textit{who} checks it,} &\text{ or \textit{when and where} they check it.}
            \end{aligned}
            """,
            font_size=36,
        )
        subtitle_stmt1.to_edge(DOWN, buff=.5)
        
        stmt2 = MathTex(
            r"\text{Logical structure} \Rightarrow \text{trustworthy models}",
            font_size=40
        ).next_to(stmt1, DOWN, buff=.5)
        
        subtitle_stmt2 = MathTex(
            r"""
            \begin{aligned}
            \text{With that logical structure,math} &\text{ematics becomes one of a new language,}\\
            \textit{a mathematician’s} &\textit{ finest tools even nowadays},\\
            \end{aligned}
            """,
            font_size=36,   
        )
        subtitle_stmt2.to_edge(DOWN, buff=.5)

        stmt3 = MathTex(
            r"\text{Abstract rigor} \Rightarrow \text{real-world certainty}",
            font_size=40
        ).next_to(stmt2, DOWN, buff=.5)
        
        subtitle_stmt3 = MathTex(
            r"""
            \begin{aligned}
            \text{Their abstract rigor became the found} &\text{ation for the certainty we depend on}\\
            \text{in modern science} &\text{ and technology.}
            \end{aligned}  
            """,
            font_size=36,
        )
        subtitle_stmt3.to_edge(DOWN, buff=.5)

        # 顯示第一句
        self.play(
            Write(stmt1),
            ReplacementTransform(subtitle_title, subtitle_stmt1),
            run_time=1.5
        )
        self.wait(3.0)  # 可以配合你講「They invented proof as a method...」

        # 轉第二句
        self.play(Write(stmt2),
                ReplacementTransform(subtitle_stmt1, subtitle_stmt2),
                run_time=1.5
        )
        self.wait(4.0)  # 你講「That logical structure is what lets us build models...」

        # 轉第三句
        self.play(
            Write(stmt3),
            ReplacementTransform(subtitle_stmt2, subtitle_stmt3),
            run_time=1.5
        )
        self.wait(2.0)  # 你講「Abstract rigor turning into certainty in practice...」

        # ================== Bottom row: modern fields cards ==================

        # Generic card factory
        def make_card(label_text):
            card = RoundedRectangle(
                corner_radius=0.2,
                width=3.6,
                height=1.5,
                stroke_width=2,
                color=GREY_B
            )
            label = Text(label_text, font_size=30).move_to(card.get_center())
            return VGroup(card, label)

        eng_card = make_card("Modern engineering").scale(.8)
        subtitle_eng_card = MathTex(
            r"\text{Modern engineering depends on mathematically proven models to keep structures safe. }",
            font_size=30,
        )
        subtitle_eng_card.to_edge(DOWN, buff=.5)
        
        crypto_card = make_card("Cryptography").scale(.8)
        subtitle_cyptyo_card = MathTex(
            r"\text{Cryptography uses number- theoretic proofs to protect digital security and privacy.}",
            font_size=30,
        )
        subtitle_cyptyo_card.to_edge(DOWN, buff=.5)
        
        cs_card = make_card("Computer science").scale(.8)
        subtitle_cs_card = MathTex(
            r"""
            \begin{aligned}
            \text{Computer science} &\text{ relies on proofs to guarantee correction and to understand}\\
            &\text{ what algorithms can and cannot do.}
            \end{aligned}
            """,
            font_size=30,
        )
        subtitle_cs_card.to_edge(DOWN, buff=.5)
        
        phys_card = make_card("Physics").scale(.8)
        subtitle_phys_card = MathTex(
            r"\text{Physics and other sciences use mathematical proofs to build reliable models of reality.}",
            font_size=30,
        )
        subtitle_phys_card.to_edge(DOWN, buff=.5)
        
        # Arrange in a row at the bottom
        cards = VGroup(eng_card, crypto_card, cs_card, phys_card)
        cards.arrange(RIGHT, buff=0.6)
        cards.to_edge(DOWN, buff=0.7).shift(UP*1.5)

        # 依次出現四個範疇（你可以喺旁白逐個講）
        self.play(
            FadeIn(eng_card),
            ReplacementTransform(subtitle_stmt3, subtitle_eng_card),
            run_time=1.0
        )
        self.wait(2)  # 「In modern engineering...」

        self.play(
            FadeIn(crypto_card),
            ReplacementTransform(subtitle_eng_card, subtitle_cyptyo_card),
            run_time=1.0
        )
        self.wait(2)  # 「In cryptography...」

        self.play(
            FadeIn(cs_card),
            ReplacementTransform(subtitle_cyptyo_card, subtitle_cs_card),
            run_time=1.0
        )
        self.wait(2)  # 「In computer science...」

        self.play(
            FadeIn(phys_card),
            ReplacementTransform(subtitle_cs_card, subtitle_phys_card),
            run_time=1.0
        )
        self.wait(1.5)  # 「In physics and beyond...」

        # ================== Optional: lines from RIGOUR to each card ==================
        lines = VGroup()
        for card in [eng_card, crypto_card, cs_card, phys_card]:
            line = Line(
                title.get_bottom() + DOWN*0.1,
                card.get_top() + UP*0.1,
                stroke_width=2
            ).set_color(GREY_D)
            lines.add(line)

        subtitle_line = MathTex(
            r"\text{All of these rely on Greek-style proof to ensure certainty and reliability.}",
            font_size=30,
        ).to_edge(DOWN, buff=.5)
        
        self.play(
            Create(lines),
            ReplacementTransform(subtitle_phys_card, subtitle_line),
            run_time=2
        )
        self.wait(2.0)  # 呢段你可以講總結：「All of these rely on Greek-style proof...」

        # ================== Final closing text ==================
        closing = Text(
            "From Greek proof to the modern world",
            font_size=42,
            color=WHITE
        ).move_to(ORIGIN)
        
        substitle_closing = MathTex(
            r"""
            \begin{aligned}
            \text{From \textbf{\textit{Greek proof}} to the modern world, our e} &\text{ntire scientific and technological landscape}\\
            \text{is still shaped} &\text{ by \textbf{\textit{proof}}}
            \end{aligned}
            """,
            font_size=30,
        )
        substitle_closing.to_edge(DOWN, buff=.5)
        
         # Fade out previous elements and show closing text

        self.play(
            FadeOut(stmt1, run_time=1.0),
            FadeOut(lines, run_time=1.0),
            FadeOut(title, run_time=1.0),
            FadeOut(stmt2, run_time=1.0),
            FadeOut(stmt3, run_time=1.0),
            run_time=3
        )
        self.play(
            FadeIn(closing, shift=UP*0.3),
            ReplacementTransform(subtitle_line, substitle_closing),
            run_time=1.5
        )
        self.wait(2.0)  # 你最後一句總結可以喺呢度講完

        # Fade everything out
        self.play(
            FadeOut(closing),
            FadeOut(cards),
            run_time=1.2
        )
        self.play(substitle_closing.animate.move_to(ORIGIN).scale(1.05),
                  run_time=1.0
        )
        self.wait(1.5)
        self.play(FadeOut(substitle_closing, run_time=1.0))
        self.wait(0.5)
        
        end_text = Text(
            "The End",
            font="Zapfino",
            font_size=80,
        )

        self.play(Write(end_text, run_time=2))
        self.wait(5)
        self.play(Unwrite(end_text))
